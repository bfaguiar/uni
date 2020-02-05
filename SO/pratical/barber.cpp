#include <stdlib.h>
#include "dbc.h"
#include "global.h"
#include "utils.h"
#include "box.h"
#include "timer.h"
#include "logger.h"
#include "barber-shop.h"
#include "barber.h"

enum State
{
	NONE = 0,
	CUTTING,
	SHAVING,
	WASHING,
	WAITING_CLIENTS,
	WAITING_BARBER_SEAT,
	WAITING_WASHBASIN,
	REQ_SCISSOR,
	REQ_COMB,
	REQ_RAZOR,
	DONE
};

#define State_SIZE (DONE - NONE + 1)

static pthread_mutex_t barberbenches = PTHREAD_MUTEX_INITIALIZER;
static pthread_mutex_t barberchairs = PTHREAD_MUTEX_INITIALIZER;
static pthread_mutex_t washbasins = PTHREAD_MUTEX_INITIALIZER;
static pthread_mutex_t scissors = PTHREAD_MUTEX_INITIALIZER;    //
static pthread_mutex_t combs = PTHREAD_MUTEX_INITIALIZER;       //    nao sei se estes podem ser substituidos por um para o toolpot inteiro
static pthread_mutex_t razors = PTHREAD_MUTEX_INITIALIZER;

static pthread_cond_t barberchairsnotfull  = PTHREAD_COND_INITIALIZER;
static pthread_cond_t barberchairsnotempty = PTHREAD_COND_INITIALIZER;
static pthread_cond_t washbasinsnotfull     = PTHREAD_COND_INITIALIZER;
static pthread_cond_t washbasinsnotempty    = PTHREAD_COND_INITIALIZER;
static pthread_cond_t barberbenchesnotfull  = PTHREAD_COND_INITIALIZER;
static pthread_cond_t barberbenchesnotempty = PTHREAD_COND_INITIALIZER;

static pthread_cond_t scissorsnotfull = PTHREAD_COND_INITIALIZER;
static pthread_cond_t combsnotfull = PTHREAD_COND_INITIALIZER;
static pthread_cond_t scissorsnotempty = PTHREAD_COND_INITIALIZER;
static pthread_cond_t combsnotempty = PTHREAD_COND_INITIALIZER;
static pthread_cond_t razorsnotfull = PTHREAD_COND_INITIALIZER;
static pthread_cond_t razorsnotempty = PTHREAD_COND_INITIALIZER;



static const char* stateText[State_SIZE] =
{
	"---------",
	"CUTTING  ",
	"SHAVING  ",
	"WASHING  ",
	"W CLIENT ", // Waiting for client
	"W SEAT   ", // Waiting for barber seat
	"W BASIN  ", // Waiting for washbasin
	"R SCISSOR", // Request a scissor
	"R COMB   ", // Request a comb
	"R RAZOR  ", // Request a razor
	"DONE     ",
};

static const char* skel =
"@---+---+---@\n"
"|B##|C##|###|\n"
"+---+---+-+-+\n"
"|#########|#|\n"
"@---------+-@";
static int skel_length = num_lines_barber()*(num_columns_barber()+1)*4; // extra space for (pessimistic) utf8 encoding!

static void life(Barber* barber);

static void sit_in_barber_bench(Barber* barber);
static void wait_for_client(Barber* barber);
static int work_available(Barber* barber);
static void rise_from_barber_bench(Barber* barber);
static void process_resquests_from_client(Barber* barber);
static void release_client(Barber* barber);
static void done(Barber* barber);
static void process_haircut_request(Barber* barber);
static void process_shave_request(Barber* barber);
static void process_hairwash_request(Barber* barber);

static char* to_string_barber(Barber* barber);

size_t sizeof_barber()
{
	return sizeof(Barber);
}

int num_lines_barber()
{
	return string_num_lines((char*)skel);
}

int num_columns_barber()
{
	return string_num_columns((char*)skel);
}

void init_barber(Barber* barber, int id, BarberShop* shop, int line, int column)
{
	require (barber != NULL, "barber argument required");
	require (id > 0, concat_3str("invalid id (", int2str(id), ")"));
	require (shop != NULL, "barber shop argument required");
	require (line >= 0, concat_3str("Invalid line (", int2str(line), ")"));
	require (column >= 0, concat_3str("Invalid column (", int2str(column), ")"));

	barber->id = id;
	barber->state = NONE;
	barber->shop = shop;
	barber->clientID = 0;
	barber->reqToDo = 0;
	barber->benchPosition = -1;
	barber->chairPosition = -1;
	barber->basinPosition = -1;
	barber->tools = 0;
	barber->internal = NULL;
	barber->logId = register_logger((char*)("Barber:"), line ,column,
	num_lines_barber(), num_columns_barber(), NULL);
}

void term_barber(Barber* barber)
{
	require (barber != NULL, "barber argument required");

	if (barber->internal != NULL)
	{
		mem_free(barber->internal);
		barber->internal = NULL;
	}
}

void log_barber(Barber* barber)
{
	require (barber != NULL, "barber argument required");

	spend(random_int(global->MIN_VITALITY_TIME_UNITS, global->MAX_VITALITY_TIME_UNITS));
	send_log(barber->logId, to_string_barber(barber));
}

void* main_barber(void* args)
{

	Barber* barber = (Barber*)args;
	require (barber != NULL, "barber argument required");
	life(barber);
	return NULL;
}

static void life(Barber* barber)
{
	require (barber != NULL, "barber argument required");


	sit_in_barber_bench(barber);
	wait_for_client(barber);
	while(work_available(barber)) // no more possible clients and closes barbershop
	{
		rise_from_barber_bench(barber);
		process_resquests_from_client(barber);
		release_client(barber);
		sit_in_barber_bench(barber);
		wait_for_client(barber);
	}
	done(barber);
}

static void sit_in_barber_bench(Barber* barber)
{
	/** TODO:
	* 1: sit in a random empty seat in barber bench (always available)
	**/

	require (barber != NULL, "barber argument required");
	require (num_seats_available_barber_bench(barber_bench(barber->shop)) > 0, "seat not available in barber shop");
	require (!seated_in_barber_bench(barber_bench(barber->shop), barber->id), "barber already seated in barber shop");

	mutex_lock(&barberbenches); //-----------------------------------------------------------------------------------------------

	while (num_seats_available_barber_bench(barber_bench(barber->shop))<=0)
	cond_wait(&barberbenchesnotfull, &barberbenches);

	barber->benchPosition = random_sit_in_barber_bench(barber_bench(barber->shop), barber->id);                                           //mutex locked
	log_barber(barber);

	pthread_cond_signal(&barberbenchesnotempty);

	pthread_mutex_unlock(&barberbenches); //-----------------------------------------------------------------------------------------------

	barber->clientID = 0;

	for(int i=1;i<MAX_CLIENTS;i++){
		if(barber->shop->ClientBarberAssoc[i] == barber->id){
			barber->shop->ClientBarberAssoc[i] = 0;
		}
	}

	log_barber(barber);

}

static void wait_for_client(Barber* barber)
{
	/** TODO:
	* 1: set the client state to WAITING_CLIENTS
	* 2: get next client from client benches (if empty, wait) (also, it may be required to check for simulation termination)
	* 3: receive and greet client (receive its requested services, and give back the barber's id)
	**/

	require (barber != NULL, "barber argument required");
	barber->state = WAITING_CLIENTS;
	log_barber(barber);
	/*if((RQItem cl = next_client_in_benches(client_benches(barber->shop))) != NULL){ 		//?????
	receive_and_greet_client(barber->shop, barber->id, cl->id);
	}else{

	}*/
	int count = 0;
	int clFound = 0;
	while(clFound==0 and (work_available(barber))){
		/*if(count >= global->MAX_OUTSIDE_TIME_UNITS){
		close_shop(barber->shop);
	}*/
	count++;
	RQItem cl = next_client_in_benches(client_benches(barber->shop));
	if(cl.clientID==0){
		spend(random_int(global->MIN_VITALITY_TIME_UNITS, global->MAX_VITALITY_TIME_UNITS));
	}else{
		clFound = 1;
		barber->clientID = cl.clientID;
		barber->reqToDo = cl.request;
		receive_and_greet_client(barber->shop,barber->id,barber->clientID);
		log_barber(barber);
		for(int i=1;i<MAX_CLIENTS;i++){
			if(i == cl.clientID){
				barber->shop->ClientBarberAssoc[i] = barber->id;
				break;
			}
		}

	}
	}

	log_barber(barber);  // (if necessary) more than one in proper places!!!
}

static int work_available(Barber* barber)
{
	/** TODO:
	* 1: find a safe way to solve the problem of barber termination
	**/

	require (barber != NULL, "barber argument required");

	return (shop_opened(barber->shop) == 1 || barber->shop->numClientsInside >0);
}

static void rise_from_barber_bench(Barber* barber)
{
	/** TODO:
	* 1: rise from the seat of barber bench
	**/

	require (barber != NULL, "barber argument required");
	require (seated_in_barber_bench(barber_bench(barber->shop), barber->id), "barber not seated in barber shop");

	pthread_mutex_lock(&barberbenches); //-------------------------------------------------------------------------

	rise_barber_bench(barber_bench(barber->shop), barber->benchPosition);    							 //mutex locked

	pthread_cond_signal(&barberbenchesnotfull);

	pthread_mutex_unlock(&barberbenches); //------------------------------------------------------------------------

	barber->benchPosition = -1;
	log_barber(barber);
}

static void process_resquests_from_client(Barber* barber)
{
	/** TODO:
	* Process one client request at a time, until all requests are fulfilled.
	* For each request:
	* 1: select the request to process (any order is acceptable)
	* 2: reserve the chair/basin for the service (setting the barber's state accordingly)
	*    2.1: set the client state to a proper value
	*    2.2: reserve a random empty chair/basin
	*    2.2: inform client on the service to be performed
	* 3: depending on the service, grab the necessary tools from the pot (if any)
	* 4: process the service (see [incomplete] process_haircut_request as an example)
	* 3: return the used tools to the pot (if any)
	*
	*
	* At the end the client must leave the barber shop
	**/


	require (barber != NULL, "barber argument required");
	int serviceTermFlag = 0;
	int breakOutFlag = 0;
	Service s;
	int req = barber->reqToDo;
	ToolsPot* pot= tools_pot(barber->shop);


	while(req > 0 and barber->clientID > 0){

		if((req & SHAVE_REQ) and (num_available_barber_chairs(barber->shop)>0) and (pot->availRazors > 0)){
			barber->state = WAITING_BARBER_SEAT;
			log_barber(barber);

			pthread_mutex_lock(&barberchairs); //--------------------------------------------------------------------

			barber->chairPosition = reserve_random_empty_barber_chair(barber->shop, barber->id);			//mutex locked

			pthread_cond_signal(&barberchairsnotempty);

			pthread_mutex_unlock(&barberchairs); //--------------------------------------------------------------------

			set_barber_chair_service(&s,barber->id,barber->clientID,barber->chairPosition,SHAVE_REQ);
			inform_client_on_service(barber->shop,s);

			pthread_mutex_lock(&razors);

			while(pot->availRazors <=0)
			pthread_cond_wait(&razorsnotempty, &razors);

			pick_razor(tools_pot(barber->shop));

			pthread_cond_signal(&razorsnotfull);

			pthread_mutex_unlock(&razors);

			barber -> tools += RAZOR_TOOL;

			while(breakOutFlag == 0){

				//mutex_lock(&barber->shop->barberchairs); //--------------------------------------------------------------------

				if(client_seated_in_barber_chair(barber_chair(barber->shop, barber->chairPosition), barber->clientID)){		//nao tenho a certeza deste

					//mutex_unlock(&barber->shop->barberchairs); //--------------------------------------------------------------------

					set_tools_barber_chair(barber_chair(barber->shop,s.pos), barber->tools);
					barber -> state = SHAVING;
					process_shave_request(barber);
					breakOutFlag = 1;
				}else{
					spend(random_int(global->MIN_WORK_TIME_UNITS,global->MAX_WORK_TIME_UNITS));
				}
			}
			while(serviceTermFlag == 0){

				//mutex_lock(&barber->shop->barberchairs); //--------------------------------------------------------------------

				if((barber_chair_service_finished(barber_chair(barber->shop,barber->chairPosition)))==1){		//nao tenho a certeza deste

					//mutex_unlock(&barber->shop->barberchairs); //--------------------------------------------------------------------

					serviceTermFlag = 1;
					barber->tools = barber->tools - RAZOR_TOOL;

					pthread_mutex_lock(&razors);

					return_razor(tools_pot(barber->shop));

					pthread_mutex_unlock(&razors);

					req = req - SHAVE_REQ;

					pthread_mutex_lock(&barberchairs); //--------------------------------------------------------------------

					release_barber_chair(barber_chair(barber->shop,barber->chairPosition), barber->id);  		//mutex locked

					pthread_cond_signal(&barberbenchesnotfull);

					pthread_mutex_unlock(&barberchairs); //--------------------------------------------------------------------

					barber->chairPosition += -1;
					log_barber(barber);
				}
			}
			serviceTermFlag = 0;
			breakOutFlag = 0;
		}

		//-------------------------------------------------------------------------------------------------------------


		else if((req & HAIRCUT_REQ) and (num_available_barber_chairs(barber->shop)>0) and (pot->availScissors > 0) and (pot->availCombs >0)){	//nao tenho a certeza deste

			//mutex_unlock(&barber->shop->barberchairs); //----------------------------------------------------------------------------------------------------

			barber->state = WAITING_BARBER_SEAT;
			log_barber(barber);

			mutex_lock(&barberchairs); //--------------------------------------------------------------------

			barber->chairPosition = reserve_random_empty_barber_chair(barber->shop, barber->id);				//mutex locked

			pthread_cond_signal(&barberchairsnotfull);

			mutex_unlock(&barberchairs); //--------------------------------------------------------------------

			set_barber_chair_service(&s,barber->id,barber->clientID,barber->chairPosition,HAIRCUT_REQ);
			inform_client_on_service(barber->shop,s);

			pthread_mutex_lock(&scissors);	//--------------------------------------------------------------------------

			while(pot->availScissors <=0)
			pthread_cond_wait(&scissorsnotempty, &scissors);

			pick_scissor(tools_pot(barber->shop));				//mutex locked


			pthread_cond_signal(&razorsnotfull);


			pthread_mutex_unlock(&scissors);	//--------------------------------------------------------------------------

			pthread_mutex_lock(&combs);	//--------------------------------------------------------------------------

			pick_comb(tools_pot(barber->shop));				//mutex locked

			pthread_mutex_unlock(&combs);	//--------------------------------------------------------------------------

			barber-> tools += SCISSOR_TOOL;
			barber-> tools += COMB_TOOL;
			while(breakOutFlag == 0){

				if(client_seated_in_barber_chair(barber_chair(barber->shop, barber->chairPosition), barber->clientID)){
					set_tools_barber_chair(barber_chair(barber->shop,s.pos), barber->tools);
					barber -> state = CUTTING;
					process_haircut_request(barber);
					breakOutFlag = 1;
				}else{
					spend(random_int(global->MIN_WORK_TIME_UNITS,global->MAX_WORK_TIME_UNITS));
				}
			}

			while(serviceTermFlag == 0){

				//	mutex_lock(&barber->shop->barberchairs); //--------------------------------------------------------------------

				if((barber_chair_service_finished(barber_chair(barber->shop,barber->chairPosition)))==1){		//nao tenho a certeza deste

					//  		mutex_unlock(&barber->shop->barberchairs); //--------------------------------------------------------------------

					serviceTermFlag = 1;
					barber->tools = barber->tools - SCISSOR_TOOL;
					barber->tools = barber->tools - COMB_TOOL;
					return_scissor(tools_pot(barber->shop));
					return_comb(tools_pot(barber->shop));
					req = req - HAIRCUT_REQ;

					pthread_mutex_lock(&barberchairs); //--------------------------------------------------------------------

					release_barber_chair(barber_chair(barber->shop,barber->chairPosition), barber->id);				//mutex locked

					pthread_cond_signal(&barberchairsnotfull);

					pthread_mutex_unlock(&barberchairs); //--------------------------------------------------------------------

					barber->chairPosition += -1;
					log_barber(barber);
					//mutex_lock(&barber->shop->barberchairs);

				}else{
					spend(random_int(global->MIN_WORK_TIME_UNITS,global->MAX_WORK_TIME_UNITS));
				}
			}

			breakOutFlag = 0;
			serviceTermFlag = 0;
		}

		else if((req & WASH_HAIR_REQ) and (num_available_washbasin(barber->shop)>0)){
			barber->state = WAITING_WASHBASIN;

			pthread_mutex_lock(&washbasins); //--------------------------------------------------------------------

			while(num_available_washbasin(barber->shop) <= 0)
			pthread_cond_wait(&washbasinsnotfull, &washbasins);

			log_barber(barber);

			barber->basinPosition = reserve_random_empty_washbasin(barber->shop, barber->id); 		//mutex locked

			pthread_cond_signal(&washbasinsnotempty);

			pthread_mutex_unlock(&washbasins); //--------------------------------------------------------------------

			set_washbasin_service(&s,barber->id,barber->clientID,barber->basinPosition);
			inform_client_on_service(barber->shop,s);
			while(breakOutFlag == 0){

				if(client_seated_in_washbasin(washbasin(barber->shop, barber->basinPosition), barber->clientID)){
					barber -> state = WASHING;
					process_hairwash_request(barber);
					breakOutFlag = 1;
				}else{
					spend(random_int(global->MIN_WORK_TIME_UNITS,global->MAX_WORK_TIME_UNITS));
				}
			}

			while(serviceTermFlag == 0){

				//	mutex_lock(&barber->shop->washbasins); //--------------------------------------------------------------------

				if((washbasin_service_finished(washbasin(barber->shop,barber->basinPosition)))==1){				//nao tenho a certeza deste

					//    		mutex_unlock(&barber->shop->washbasins); //--------------------------------------------------------------------

					req = req - WASH_HAIR_REQ;
					serviceTermFlag = 1;
					req = req - WASH_HAIR_REQ;

					mutex_lock(&washbasins); //--------------------------------------------------------------------

					release_washbasin(washbasin(barber->shop,barber->basinPosition), barber->id); 			//mutex locked

					pthread_cond_signal(&washbasinsnotfull);

					mutex_unlock(&washbasins); //--------------------------------------------------------------------

					barber->basinPosition += -1;
					serviceTermFlag = 1;
					log_barber(barber);
				}
			}
			breakOutFlag = 0;
			serviceTermFlag = 0;
		}

	}

	barber->reqToDo = 0;
	barber->state = WAITING_CLIENTS;
	log_barber(barber);  // (if necessary) more than one in proper places!!!
}

static void release_client(Barber* barber)
{
	/** TODO:
	* 1: notify client the all the services are done
	**/

	require (barber != NULL, "barber argument required");
	client_done(barber->shop, barber->clientID);


	barber->clientID = 0;

	log_barber(barber);
	for(int i=1;i<MAX_CLIENTS;i++){
		if(barber->shop->ClientBarberAssoc[i] == barber->id){
			barber->shop->ClientBarberAssoc[i] = 0;
		}
	}

	log_barber(barber);
}

static void done(Barber* barber)
{
	/** TODO:
	* 1: set the client state to DONE             				 DONE
	**/

	require (barber != NULL, "barber argument required");
	barber->state = DONE;
	for(int i=1;i<MAX_CLIENTS;i++){
		if(barber->shop->ClientBarberAssoc[i] == barber->id){
			barber->shop->ClientBarberAssoc[i] = 0;
		}
	}

	log_barber(barber);

	barber->clientID = 0;
	term_barber(barber);


	log_barber(barber);
}

static void process_haircut_request(Barber* barber)
{
	/** TODO:
	* ([incomplete] example code for task completion algorithm)
	**/
	require (barber != NULL, "barber argument required");
	require (barber->tools & SCISSOR_TOOL, "barber not holding a scissor");
	require (barber->tools & COMB_TOOL, "barber not holding a comb");


	barber->state = CUTTING;
	log_barber(barber);
	int steps = random_int(5,20);
	int slice = (global->MAX_WORK_TIME_UNITS-global->MIN_WORK_TIME_UNITS+steps)/steps;
	int complete = 0;
	while(complete < 100)
	{
		spend(slice);
		complete += 100/steps;
		if (complete > 100)
		complete = 100;
		set_completion_barber_chair(barber_chair(barber->shop, barber->chairPosition), complete);
	}

	log_barber(barber);  // (if necessary) more than one in proper places!!!
}

static void process_hairwash_request(Barber* barber)
{
	/** TODO:
	* ([incomplete] example code for task completion algorithm)
	**/
	require (barber != NULL, "barber argument required");
	//require (barber->tools & SCISSOR_TOOL, "barber not holding a scissor");
	//require (barber->tools & COMB_TOOL, "barber not holding a comb");


	barber->state = WASHING;
	log_barber(barber);
	int steps = random_int(5,20);
	int slice = (global->MAX_WORK_TIME_UNITS-global->MIN_WORK_TIME_UNITS+steps)/steps;
	int complete = 0;
	while(complete < 100)
	{
		spend(slice);
		//log_barber(barber);
		complete += 100/steps;
		if (complete > 100)
		complete = 100;
		set_completion_washbasin(washbasin(barber->shop, barber->basinPosition), complete);
		//log_barber(barber);
	}

	log_barber(barber);  // (if necessary) more than one in proper places!!!
}

static void process_shave_request(Barber* barber)
{
	/** TODO:
	* ([incomplete] example code for task completion algorithm)
	**/
	require (barber != NULL, "barber argument required");
	require (barber->tools & RAZOR_TOOL, "barber not holding a razor");


	barber->state = SHAVING;
	log_barber(barber);
	int steps = random_int(5,20);
	int slice = (global->MAX_WORK_TIME_UNITS-global->MIN_WORK_TIME_UNITS+steps)/steps;
	int complete = 0;
	while(complete < 100)
	{
		spend(slice);
		complete += 100/steps;
		if (complete > 100)
		complete = 100;
		set_completion_barber_chair(barber_chair(barber->shop, barber->chairPosition), complete);
	}

	log_barber(barber);  // (if necessary) more than one in proper places!!!
}

static char* to_string_barber(Barber* barber)
{
	require (barber != NULL, "barber argument required");

	if (barber->internal == NULL)
	barber->internal = (char*)mem_alloc(skel_length + 1);

	char tools[4];
	tools[0] = (barber->tools & SCISSOR_TOOL) ? 'S' : '-',
	tools[1] = (barber->tools & COMB_TOOL) ?    'C' : '-',
	tools[2] = (barber->tools & RAZOR_TOOL) ?   'R' : '-',
	tools[3] = '\0';

	char* pos = (char*)"-";
	if (barber->chairPosition >= 0)
	pos = int2nstr(barber->chairPosition+1, 1);
	else if (barber->basinPosition >= 0)
	pos = int2nstr(barber->basinPosition+1, 1);

	return gen_boxes(barber->internal, skel_length, skel,
		int2nstr(barber->id, 2),
		barber->clientID > 0 ? int2nstr(barber->clientID, 2) : "--",
		tools, stateText[barber->state], pos);
	}
