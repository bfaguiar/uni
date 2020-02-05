/******* Implementa��o da Fila com Prioridade com um Amontoado Bin�rio ********/
/***** Fila com Prioridade orientada aos m�nimos Nome: pqueue_dijkstra.c  *****/

#include <stdio.h>
#include <stdlib.h>

#include "pqueue_dijkstra.h"  /* Interface */

/******* Defini��o do Estrutura de Dados da Fila com Prioridade ********/

struct pqueue  /* defini��o da Fila com Prioridade */
{
  unsigned int HeapSize;  /* capacidade de armazenamento da Fila - capacity of the priority queue */
  unsigned int NumElem;  /* n�mero de elementos armazenados na Fila - number of elements stored in the priority queue */
  VERTEX *Heap;  /* ponteiro para o monte a alocar dinamicamente - pointer to the priority queue array */
};

/********************** Defini��o dos Subprogramas *********************/

PtPQueue PQueueCreate (unsigned int pdim) {

  PtPQueue NewPQueue;

  if(pdim == 0)
    return NULL;

  if((NewPQueue = (PtPQueue) malloc (sizeof (struct pqueue))) == NULL)
    return NULL;

  if ((NewPQueue->Heap = (VERTEX *) calloc (pdim, sizeof (VERTEX))) == NULL) {
    free(NewPQueue);
    return NULL;
  }

    NewPQueue->NumElem = 0;
    NewPQueue->HeapSize = pdim;

    return NewPQueue;

}


int PQueueDestroy (PtPQueue *ppqueue) {

  PtPQueue AuxPQueue = *ppqueue;

  if (AuxPQueue == NULL)
    return NO_PQUEUE;

  free (AuxPQueue->Heap);
  free (AuxPQueue);

  *ppqueue = NULL;

  return OK;

}


int PQueueInsert (PtPQueue ppqueue, VERTEX *pelem) {

  if (ppqueue == NULL)
    return NO_PQUEUE;

  if ((ppqueue->NumElem) == (ppqueue->HeapSize))
    return PQUEUE_FULL;

  unsigned int i;

  for (i = ppqueue->NumElem; i > 0 && ppqueue->Heap[(i-1)/2].Cost > pelem->Cost; i = (i-1)/2)
    ppqueue->Heap[i] = ppqueue->Heap[(i-1)/2];

  ppqueue->Heap[i] = *pelem;
  ppqueue->NumElem++;

  return OK;

}


int PQueueDeleteMin (PtPQueue ppqueue, VERTEX *pelem) {

  if (ppqueue == NULL)
    return NO_PQUEUE;

  if (pelem == NULL)
    return NULL_PTR;

  if (ppqueue->NumElem == 0)
    return PQUEUE_EMPTY;

  unsigned int i;
  unsigned int count;

  *pelem = ppqueue->Heap[0];

  ppqueue->NumElem--;

  for (i = 0; i*2+1 <= ppqueue->NumElem; i = count) {
    count = 2*i+1;
    if (count < ppqueue->NumElem && ppqueue->Heap[count].Cost > ppqueue->Heap[count+1].Cost)
      count++;
    if (ppqueue->Heap[count].Cost < ppqueue->Heap[ppqueue->NumElem].Cost)
      ppqueue->Heap[i] = ppqueue->Heap[count];
    else break;
  }

  ppqueue->Heap[i] = ppqueue->Heap[ppqueue->NumElem];

  return OK;
}


int PQueueDecrease (PtPQueue ppqueue, VERTEX *pelem) {

  unsigned int i;

  if (ppqueue == NULL)
    return NO_PQUEUE;

  if (ppqueue->NumElem == 0)
    return PQUEUE_EMPTY;

  for (i = 0; i < ppqueue->NumElem; i++)
    if (ppqueue->Heap[i].Vertex == pelem->Vertex)
      break;

  if (i == ppqueue->NumElem)
        return NO_ELEM;

  for ( ; i > 0 && ppqueue->Heap[(i-1)/2].Cost > pelem->Cost; i = (i-1)/2)
    ppqueue->Heap[i] = ppqueue->Heap[(i-1)/2];

  ppqueue->Heap[i] = *pelem;

  return OK;

}


int PQueueIsEmpty (PtPQueue ppqueue) {
  if (ppqueue == NULL) return NO_PQUEUE;
  if (ppqueue->NumElem == 0) return PQUEUE_EMPTY;
  return OK;
}

int PQueueDisplay (PtPQueue ppqueue)
{
  int I;

  if (ppqueue == NULL) return NO_PQUEUE;
  if (ppqueue->NumElem == 0) return PQUEUE_EMPTY;

  for (I = 0; I < ppqueue->NumElem; I++)
    printf ("(%d-%d)  ", ppqueue->Heap[I].Vertex, ppqueue->Heap[I].Cost);
  printf ("\n");

  return OK;
}
