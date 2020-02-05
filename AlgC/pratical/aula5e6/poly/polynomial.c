/*******************************************************************************

 Ficheiro de implementaÃ§Ã£o do Tipo de Dados Abstrato POLINOMIO (polynomial.c).
 A estrutura de dados de suporte do polinÃ³mio Ã© uma estrutura, constituÃ­da pelo
 campo de tipo inteiro Degree para armazenar o grau do polinÃ³mio e o campo de
 tipo ponteiro Poly, para representar a sequÃªncia atribuÃ­da dinamicamente, que
 vai armazenar os seus coeficientes reais.

 Nome : Bruno Filipe Oliveira Aguiar                   NMec: 80177

 Implementation file of the abstract data type Poly (polynomial.c). The data
 structure to store the polynomial is composed with the integer field Degree for
 keeping the polynomial's degree and the pointer field Poly, that represents the
 allocated array in dynamic memory, for storing the polynomial's real coefficients.

*******************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include "polynomial.h"    /* Ficheiro de interface do TDA - ADT Interface file */

/************ DefiniÃ§Ã£o da Estrutura de Dados Interna do POLINOMIO ************/

struct poly
{
  unsigned int Degree;  /* grau do polinÃ³mio - polynomial degree */
  double *Poly;      /* ponteiro para os coeficientes do polinÃ³mio - pointer to polynomial's coefficients */
};

/*********************** Controlo Centralizado de Erro ************************/

static unsigned int Error = OK;  /* inicializaÃ§Ã£o do erro */

static char *ErrorMessages[] = {
                                 "sem erro - Without Error",
                                 "polinomio(s) inexistente(s) - Polynomial(s) do not exist",
                                 "memoria esgotada - Out of memory",
                                 "ficheiro inexistente - File does not exist",
                                 "grau do polinomio errado - Wrong degree",
                                 "coeficiente inexistente no polinomio - Coefficient does not exist"
                               };

static char *AbnormalErrorMessage = "erro desconhecido - Unknown error";

/************** NÃºmero de mensagens de erro previstas no mÃ³dulo ***************/

#define N (sizeof (ErrorMessages) / sizeof (char *))

/************************ AlusÃ£o Ã s FunÃ§Ãµes Auxiliares ************************/

static int ValidPolys (PtPoly, PtPoly);
static void ReducePoly (PtPoly);

/*************************** DefiniÃ§Ã£o das FunÃ§Ãµes ****************************/

void PolyClearError (void)
{
  Error = OK;
}

int PolyError (void)
{
  return Error;
}

char *PolyErrorMessage (void)
{
  if (Error < N) return ErrorMessages[Error];
  else return AbnormalErrorMessage;    /* nÃ£o hÃ¡ mensagem de erro - no error message */
}

PtPoly PolyCreate (unsigned int pdegree)
{
  /* insira o seu cÃ³digo - insert your code */
	PtPoly Poly;

	if (pdegree < 0){ Error = BAD_DEGREE; return NULL;}

	if ((Poly = (PtPoly) malloc (sizeof (struct poly))) == NULL){
      free (Poly); Error = NO_MEM; return NULL;
  }
  if ((Poly->Poly = (double *) calloc (pdegree+1, sizeof (double))) == NULL){
      free (Poly); Error = NO_MEM; return NULL;
  }


  Poly->Degree = pdegree;     /* armazenamento do grau - storing the size */

  Error = OK;
  return Poly;

}

void PolyDestroy (PtPoly *ppoly)
{
  PtPoly TmpPoly = *ppoly;

  /* verifica se o poly existe - verifies if poly exists */
  if (TmpPoly == NULL) { Error = NO_POLY; return ; }

  /* libertaÃ§Ã£o da memÃ³ria dinÃ¢mica - free dynamic memory */
  free (TmpPoly->Poly);  /* liberta a memÃ³ria ocupada pelas componentes  - free the supporting array */
  free (TmpPoly);    /* liberta a memÃ³ria ocupada pelo poly - free the supporting record */

  Error = OK;
  *ppoly = NULL;  /* coloca a referÃªncia a nulo - free the pointer pointing it to null */
}

PtPoly PolyCopy (PtPoly ppoly)
{
 PtPoly Copy; int I;

  /* verifica se o poly existe - verifies if poly exists */
  if (ppoly == NULL) { Error = NO_POLY; return NULL; }

  /* criaÃ§Ã£o do poly copia nulo - creating an empty poly */
  if ((Copy = PolyCreate (ppoly->Degree)) == NULL) return NULL;

  /* fazer a copia do poly - copying the components */
  for (I = 0; I < ppoly->Degree; I++) Copy->Poly[I] = ppoly->Poly[I];

  return Copy;  /* devolve o poly copia - returning the new poly */
}

int PolyDegree (PtPoly ppoly)
{
  if (ppoly == NULL){
   Error = NO_POLY; return 0;
  }

  Error = OK;

  return ppoly->Degree;
}

void PolyModifyCoefficient (PtPoly ppoly, unsigned int ppos, double pvalue)
{
    /* verifica se o polinÃ³mio existe  */
  if (ppoly == NULL) { Error = NO_POLY; return  ; }
  /*  */
  if (ppos > ppoly -> Degree ){Error = BAD_INDEX; return ; }

  Error = OK;

  /* escrita do valor na componente pretendida do polinomio */
  ppoly->Poly[ppos] = pvalue;

}

double PolyObserveCoefficient (PtPoly ppoly, unsigned int ppos)
{
    /* verifica se o polinÃ³mio existe  */
  if (ppoly == NULL) { Error = NO_POLY; return 0; }
    /* validar o elemento */
  if (ppos > ppoly -> Degree ){Error = BAD_INDEX; return 0; }

  Error = OK;

  /* devolve o valor armazenado no coeficiente do grau indicado */
  return ppoly->Poly[ppos];
}

int PolyIsNull (PtPoly ppoly)
{
  int I;

  /* verifica se o á¹”OLY existe  */
  if (ppoly == NULL) { Error = NO_POLY; return 0; }
  Error = OK;

  /* verificaÃ§Ã£o das componentes do á¹”OLY  */
  for (I = 0; I < ppoly->Degree; I++)
    if (ppoly->Poly[I]) return 0;

  return 1;  /* o á¹”OLY Ã© um á¹”OLY nulo  */

}

PtPoly PolySymmetrical (PtPoly ppoly)
{
  PtPoly Sim; int I;

  /* verifies if poly exists */
  if (ppoly == NULL) { Error = NO_POLY; return NULL; }

  /* creating an empty poly */
  if ((Sim = PolyCreate (ppoly->Degree)) == NULL) return NULL;

  /* copying the components */
  for (I = 0; I <= ppoly->Degree; I++){
    Sim->Poly[I] = -(ppoly->Poly[I]);
  }

  return Sim;
}

PtPoly PolyAddition (PtPoly ppoly1, PtPoly ppoly2)
{
  /* insira o seu cÃ³digo - insert your code */
  PtPoly Add; int I; int max; int j;

  /* valid poly */
  if (!ValidPolys (ppoly1, ppoly2)) return NULL;

  /* poly soma nulo - criacao */


  if (ppoly1->Degree > ppoly2->Degree){
 	 max = ppoly1->Degree;
  }
  else max = ppoly2->Degree;
  if ((Add = PolyCreate (max)) == NULL) { Error = NO_MEM; return NULL; }

  /* soma */
  for (I = 0; I <= ppoly1->Degree; I++){
   	   Add->Poly[I] = ppoly1->Poly[I];
  }


   for (j = 0; j <= ppoly2->Degree; ++j){
   	Add->Poly[j] += ppoly2->Poly[j];
   }

  ReducePoly(Add);

  return Add;

}

PtPoly PolySubtraction (PtPoly ppoly1, PtPoly ppoly2)
{
  PtPoly Sub; int I;int max; int j;
  /* validacao  */
  if (!ValidPolys (ppoly1, ppoly2)) return NULL;


  if (ppoly1->Degree > ppoly2->Degree){
 	 max = ppoly1->Degree;
  }
  else max = ppoly2->Degree;

  if ((Sub = PolyCreate (max)) == NULL) { Error = NO_MEM; return NULL; }

  /* soma   */
  for (I = 0; I <= ppoly1->Degree; I++){
   	   Sub->Poly[I] = ppoly1->Poly[I];
  }


   for (j = 0; j <= ppoly2->Degree; ++j){
   	Sub->Poly[j] -= ppoly2->Poly[j];
   }

  ReducePoly(Sub);

  return Sub;

}


PtPoly PolyMultiplication (PtPoly ppoly1, PtPoly ppoly2)
{
  PtPoly Mult; int I; int j;

  if (!ValidPolys (ppoly1, ppoly2)) return NULL;

  /*  create null poly */
  if ((Mult = PolyCreate ((ppoly1->Degree) + (ppoly2->Degree))) == NULL) { Error = NO_MEM; return NULL; }

  /* determinar array size do resultado */
  for (I = 0; I <= ppoly1->Degree; I++){
  	for (j = 0; j <= ppoly2->Degree; ++j){
  		Mult ->Poly[I+j] += (ppoly1 ->Poly[I])*(ppoly2->Poly[j]);
  	}
  }



  ReducePoly(Mult);
  return Mult;
}


int PolyEquals (PtPoly ppoly1, PtPoly ppoly2)
{
   int I;


  if (!ValidPolys(ppoly1, ppoly2)) return 0;
  Error = OK;

  /* comparacao dos poly */
  for (I = 0; I <= ppoly1->Degree; I++)
    if (ppoly1->Poly[I] != ppoly2->Poly[I]) return 0;

  return 1;
}

void PolyStoreFile (PtPoly ppoly, char *pnomef)
{
  FILE *PtF; unsigned int I;

  /* verifies if poly exists */
  if (ppoly == NULL) { Error = NO_POLY; return ; }

  /*  opening the text file for writing */
  if ((PtF = fopen (pnomef, "w")) == NULL) { Error = NO_FILE; return ; }

  /*  writing the poly size */
  fprintf (PtF, "%u\n", ppoly->Degree);

  /*  writing the poly components */
  for (I = 0; I <= ppoly->Degree; I++) fprintf (PtF, "%lf\n", ppoly->Poly[I]);

  Error = OK;
  fclose (PtF);
}

PtPoly PolyCreateFile (char *pnomef)
{
  PtPoly Poly; FILE *PtF; unsigned int Degree, I;

  /* opening file */
  if ( (PtF = fopen (pnomef, "r")) == NULL) { Error = NO_FILE; return NULL; }

  /* leitura da size do poly  do ficheiro*/
  fscanf (PtF, "%u", &Degree);
  if (Degree < 1) { Error = BAD_INDEX; fclose (PtF); return NULL; }

  /* criação do poly nulo */
  if ((Poly = PolyCreate (Degree)) == NULL) { fclose (PtF); return NULL; }

  /* leitura do poly */
  for (I = 0; I <= Degree; I++){
  	fscanf (PtF, "%lf", Poly->Poly+I);
	}
  fclose (PtF);
  return Poly;

}




double PolyEvaluation (PtPoly ppoly, double px)
{
  int I; double soma = 0; double pot=1;


/* verifica se existe */
  if (ppoly == NULL) { Error = NO_POLY; return 0.0; }
  Error = OK;

  for (I = 0; I <= ppoly->Degree; I++){
  	  soma += ppoly->Poly[I]*pot;
      pot *= px;
  }


  return soma;

}

/*******************************************************************************
 FunÃ§Ã£o auxiliar que verifica se os dois polinÃ³mios existem. Devolve 1 em caso
 afirmativo e 0 em caso contrÃ¡rio. Valores de erro: OK ou NO_POLY.

 Auxiliary function to verify if the two polynomials exist. Returns 1 in
 affirmative case and 0 otherwise. Error codes: OK or NO_POLY.
*******************************************************************************/

static int ValidPolys (PtPoly ppoly1, PtPoly ppoly2)
{
  /* verifica se os dois polinÃ³mios existem - verifies if the two polynomials exist */
  if ((ppoly1 == NULL) || (ppoly2 == NULL)) { Error = NO_POLY; return 0; }

  Error = OK;
  return 1;  /* os dois polinÃ³mios existem - they exist */
}

/*******************************************************************************
 FunÃ§Ã£o auxiliar que reduz o polinÃ³mio ao menor grau possÃ­vel. Valores de erro:
 NO_POLY.

 Auxiliary function to reduce the polynomial to its least degree. Error codes: NO_POLY.

*******************************************************************************/

static void ReducePoly (PtPoly ppoly)
{
  unsigned int Degree;

  /* verifica se o polinÃ³mio existe - verifies if the polynomial exists */
  if (ppoly == NULL) { Error = NO_POLY; return ; }

  Degree = ppoly->Degree;

  while (Degree > 0 && ppoly->Poly[Degree] == 0.0) Degree--;

  if (Degree != ppoly->Degree)
     ppoly->Poly = (double *) realloc (ppoly->Poly, (Degree+1) * sizeof (double));

  ppoly->Degree = Degree;
  Error = OK;
}
