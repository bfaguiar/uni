/*******************************************************************************

 Graphical program for simulate the ADT Priority Queue (Max Oriented)

 Autor : António Manuel Adrego da Rocha    Data : May 2017

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "pqueue.h" /* ADT Interface file */

#define MAX_PQUEUES 12
#define MAX_OPTIONS 9

void Menu (void);
void ReadOption (int *);
void ReadPQueueIndex (int *, char *);
int ActivePQueue (PtPQueue *, int);
int NotActivePQueue (PtPQueue *, int);
void ReadDimensionPQueue (unsigned int *);
void ReadFilename (char *);
void WriteErrorMessage (char *, int);
void ReadElement (int *);
void ReadNewElement (int *);
void DisplayPQueue (PtPQueue);

int main (void)
{
  PtPQueue PQueueArray[MAX_PQUEUES];
  int Option, l, PQueue, Element, NewValue, Error; unsigned int NElements, Dimension; 
  char NomeFicheiro[21];

  for (l = 0; l < MAX_PQUEUES; l++) PQueueArray[l] = NULL;
  
  do
  {

    /* cleaning the screen and presenting the menu */
    Menu ();

    /* presenting the active prioriyt queues */
    for (l = 0; l < MAX_PQUEUES; l++)
      if (PQueueArray[l] != NULL)
      {
        PQueueDimension (PQueueArray[l], &Dimension);
        PQueueSize (PQueueArray[l], &NElements);
        printf ("\e[1m\e[%d;47f (D = %3d / N = %3d)", 5+l, Dimension, NElements);
        printf ("\e[0m");
      }

    /* reading the user option */
    ReadOption (&Option);


    switch (Option)
    {
        case 1 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (ActivePQueue (PQueueArray, PQueue)) break;
                  ReadFilename (NomeFicheiro); 
                  if ((PQueueArray[PQueue] = PQueueCreateFile (NomeFicheiro)) == NULL)
                     WriteErrorMessage ("The reading", NO_FILE);
                  break;

        case 2 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (ActivePQueue (PQueueArray, PQueue)) break;
                  ReadDimensionPQueue (&Dimension);
                  if ((PQueueArray[PQueue] = PQueueCreate (Dimension)) == NULL)
                     WriteErrorMessage ("The creation", NO_MEM);
                  break;

        case 3 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  ReadElement (&Element);
                  Error = PQueueInsert (PQueueArray[PQueue], Element);
                  if (Error != OK) WriteErrorMessage ("The insertion", Error);
                  break;

        case 4 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  Error = PQueueDeleteMax (PQueueArray[PQueue], &Element);
                  if (Error != OK) WriteErrorMessage ("The deletion", Error);
                  else
                  {
                    printf("\e[24;1f| \e[1mThe maximum element deleted from the priority queue -> %d", Element);
                    printf("\e[0m\e[25;1f| Press a key to continue ");
                    scanf ("%*[^\n]"); scanf ("%*c");
                  }
                  break;

        case 5 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  ReadElement (&Element);
                  ReadNewElement (&NewValue);
                  Error = PQueueIncrease (PQueueArray[PQueue], Element, NewValue);
                  if (Error != OK) WriteErrorMessage ("The promotion", Error);
                  break;

        case 6 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  ReadElement (&Element);
                  ReadNewElement (&NewValue);
                  Error = PQueueDecrease (PQueueArray[PQueue], Element, NewValue);
                  if (Error != OK) WriteErrorMessage ("The despromotion", Error);
                  break;

        case 7 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  DisplayPQueue (PQueueArray[PQueue]);
                  break;

        case 8 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  ReadFilename (NomeFicheiro);
                  Error = PQueueStoreFile (PQueueArray[PQueue], NomeFicheiro);
                  if (Error != OK) WriteErrorMessage ("The storing", Error);
                  break;

        case 9 :  ReadPQueueIndex (&PQueue, "priority queue");
                  if (NotActivePQueue (PQueueArray, PQueue)) break;
                  PQueueDestroy (&PQueueArray[PQueue]);
                  break;
    }

  } while (Option != 0);

  for (l = 0; l < MAX_PQUEUES; l++) 
    if (PQueueArray[l] != NULL) PQueueDestroy (&PQueueArray[l]);

    printf ("\e[27;1f");

  return 0;
}

void Menu (void)
{
  system ("clear");

  printf("\e[2;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[3;1f|                            Graphical Program for Simulate Operations with Priority Queues                           |\n");
  printf("\e[4;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[5;1f|  1 - Read queue (from file)    | PQueue  0 =                    |                                                   |\n");
  printf("\e[6;1f|  2 - Create an empty queue     | PQueue  1 =                    |                                                   |\n");
  printf("\e[7;1f|  3 - Insert element            | PQueue  2 =                    |                                                   |\n");
  printf("\e[8;1f|  4 - Deleting the maximum      | PQueue  3 =                    |                                                   |\n");
  printf("\e[9;1f|  5 - Promoting element         | PQueue  4 =                    |                                                   |\n");
  printf("\e[10;1f|  6 - Despromoting element      | PQueue  5 =                    |                                                   |\n");
  printf("\e[11;1f|  7 - Display priority queue    | PQueue  6 =                    |                                                   |\n");
  printf("\e[12;1f|  8 - Store priority queue      | PQueue  7 =                    |                                                   |\n");
  printf("\e[13;1f|  9 - Erase priority queue      | PQueue  8 =                    |                                                   |\n");
  printf("\e[14;1f|  0 - Terminate program         | PQueue  9 =                    |                                                   |\n");
  printf("\e[15;1f|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| PQueue 10 =                    |                                                   |\n");
  printf("\e[16;1f| Option ->                      | PQueue 11 =                    |                                                   |\n");
  printf("\e[17;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[18;1f|                                             Window for Data Acquisition                                             |\n");
  printf("\e[19;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[20;1f|                                                                                                                     |\n");
  printf("\e[21;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[22;1f|                                       Window for Error Messages and Results                                         |\n");
  printf("\e[23;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
  printf("\e[24;1f|                                                                                                                     |\n");
  printf("\e[25;1f|                                                                                                                     |\n");
  printf("\e[26;1f~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
}

void ReadPQueueIndex (int *pnfp, char *pmsg)
{
  int MsgLen = strlen (pmsg);

  do
  {
    *pnfp = -1;
    printf("\e[20;1f| Index of %s ->                              ", pmsg);
    printf("\e[20;%df", 16+MsgLen); scanf ("%d", pnfp);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (*pnfp < 0 || *pnfp >= MAX_PQUEUES);
}

int ActivePQueue (PtPQueue pgrupofp[], int pnfp)
{
  char car;

  if (pgrupofp[pnfp] != NULL)
  {
    do
    {
      printf("\e[1m\e[24;1f| The priority queue %d already exist!                    ", pnfp);
      printf("\e[0m\e[25;1f| Wish to erase it (y/n)? ");
      scanf ("%c", &car); car = tolower (car);
      scanf ("%*[^\n]"); scanf ("%*c");
    } while (car != 'n' && car != 'y');

    if (car == 's') { PQueueDestroy (&pgrupofp[pnfp]); return 0; }
    else  return 1;
  }
  else return 0;
}

int NotActivePQueue (PtPQueue pgrupofp[], int pnfp)
{
  if (pgrupofp[pnfp] == NULL)
  {
    printf("\e[1m\e[24;1f| The priority queue %d does not exist!                    ", pnfp);
    printf("\e[0m\e[25;1f| Press a key to continue ");
    scanf ("%*[^\n]"); scanf ("%*c");
    return 1;
  }
  else return 0;
}

void ReadDimensionPQueue (unsigned int *pdim)
{
  do
  {
    *pdim = 0;
    printf("\e[20;1f| Dimension of the priority queue ->                               ");
    printf("\e[20;38f"); scanf ("%d", pdim);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (*pdim <= 0);
}


void ReadFilename (char *pnf)
{
  int Status;

  do
  {
    printf("\e[20;1f| Filename ->                               ");
    printf("\e[20;15f"); Status = scanf ("%20[^\n]", pnf);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (Status == 0);
}

void ReadOption (int *popc)
{
  do
  {  
    *popc = 0;
    printf("\e[16;1f| Option ->                      |");
    printf("\e[16;13f"); scanf ("%d", popc);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (*popc < 0 || *popc > MAX_OPTIONS);
}

void WriteErrorMessage (char *pmsg, int perro)
{
  printf("\e[24;1f| %s not executed because -> \e[1m", pmsg);
  
  switch (perro)
  {
    case NO_PQUEUE    : printf ("priority queue does not exist"); break ;
    case NO_MEM       : printf ("out of memory"); break ;
    case NULL_PTR     : printf ("null pointer"); break ;
    case PQUEUE_EMPTY : printf ("priority queue empty"); break ;
    case PQUEUE_FULL  : printf ("priority queue full"); break ;
    case NO_ELEM      : printf ("element does not exist in the priority queue"); break ;
    case WRONG_VALUE  : printf ("new value of the element incorrect"); break ;
    case NO_FILE      : printf ("file does not exist"); break ;
  }

  printf("\e[0m\e[25;1f| Press a key to continue ");
  scanf ("%*[^\n]"); scanf ("%*c");
}


void ReadElement (int *pelem)
{
  int Status;

  do
  {
    printf("\e[20;1f| Element ->                                       ");
    printf("\e[20;14f"); Status = scanf ("%d", pelem);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (Status == 0);
}

void ReadNewElement (int *pval)
{
  int Status;

  do
  {
    printf("\e[20;1f| New value ->                                       ");
    printf("\e[20;16f"); Status = scanf ("%d", pval);
    scanf ("%*[^\n]"); scanf ("%*c");
  } while (Status == 0);
}

void DisplayPQueue (PtPQueue ppqueue)
{
	int l, c, t, valor, i = 0, inicial; unsigned nelem;

	if (PQueueSize (ppqueue, &nelem) == PQUEUE_EMPTY)
	{
		printf ("\e[1m\e[24;1f| The priority queue is empty\n");
		printf ("\e[0m\e[25;1f| Press a key to continue "); scanf ("%*[^\n]"); scanf ("%*c");
		return;
	}

	while (i < nelem)
	{
		inicial = i;
		printf ("\e[1m");
		for (l = 0; l < 12 && i < nelem; l++)
		{
			printf ("\e[%d;68f ", 5+l);
			for (c = 0; c < 5 && i < nelem; c++)
			{
				PQueueElement (ppqueue, &valor, i);  printf ("%9d ", valor); i++;
			}
			if (i == nelem) for (t = c; t < 5; t++) printf ("          ");
		}
		if (i == nelem)
			for (t = l; t < 12; t++)
			{
				printf ("\e[%d;68f ", 5+t);
				for (c = 0; c < 5; c++) printf ("          ");
			}
		printf ("\e[0m");
		printf ("\e[1m\e[24;1f| Elements [%d-%d] of the Priority Queue\n", inicial, i-1);
		printf ("\e[0m\e[25;1f| Press a key to continue "); scanf ("%*[^\n]"); scanf ("%*c");
	}
}

