#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#include "abp.h"

int main (void)
{
	PtABPNode abp, node; int value, error, sum; unsigned int count; char op;

	system ("clear");
	abp = ABPCreate ();

  	do
	{
		printf ("Inserir-Inserting/Remover-Removing/Terminar-Terminating-> ");
		scanf ("%c", &op);
		scanf ("%*[^\n]"); scanf ("%*c");
		op = toupper (op);
	} while (op != 'I' && op != 'R' && op != 'T');

	while (op != 'T')
	{
  		printf ("Valor (Value) -> ");
		scanf ("%d", &value);
		scanf ("%*[^\n]"); scanf ("%*c");

		if (op == 'I')
		{
			ABPInsertRec (&abp, value);
			if ((error = ABPErrorCode ()) != OK) printf ("Erro a inserir (Error in inserting) -> %s\n", ABPErrorMessage ());
		}
		else	if (op == 'R')
			{
				ABPDeleteRec (&abp, value);
				if ((error = ABPErrorCode ()) != OK) printf ("Erro a remover (Error in removing) -> %s\n", ABPErrorMessage ());
			}
			else
			{
				printf ("Erro na operacao escolhida - Error on the chosen operation\n");
				error = OK;
			}

		if (!error)
		{
			printf ("--------------------------------------------------------------------------------------------\n");
			if (ABPEmpty (abp)) printf ("\nArvore vazia! - Empty tree!\n");
			else ABPDisplay (abp);
  			printf ("--------------------------------------------------------------------------------------------\n");
		}

  		printf ("Inserir-Inserting/Remover-Removing/Terminar-Terminating-> ");
		scanf ("%c", &op);
		scanf ("%*[^\n]"); scanf ("%*c");
		op = toupper (op);
	}

	printf ("--------------------------------------------------------------------------------------------\n");
	if (ABPEmpty (abp)) printf ("Arvore vazia! - Empty tree!\n");
	else 
	{
		ABPDisplay (abp);
		printf ("--------------------------------------------------------------------------------------------\n");
		printf ("Numero de nos da arvore (number of nodes) = %d\n", ABPSize (abp));
		printf ("Altura da arvore (tree height) = %d\n", ABPHeight (abp));
	}
	printf ("--------------------------------------------------------------------------------------------\n");

	node = ABPMinRep (abp);
	if (ABPErrorCode ()) printf ("Menor elemento da arvore (minimum element) = %s\n", ABPErrorMessage ());
	else printf ("Menor elemento da arvore (minimum element) = %d\n", ABPElement (node));

	node = ABPMaxRep (abp);
	if (ABPErrorCode ()) printf ("Maior elemento da arvore (maximum element) = %s\n", ABPErrorMessage ());
	else printf ("Maior elemento da arvore (maximum element) = %d\n", ABPElement (node));

	sum = ABPOddSum (abp);
	if (ABPErrorCode ()) printf ("Soma dos elementos ímpares da arvore (sum of the odd elements) = %s\n", ABPErrorMessage ());
	else printf ("Soma dos elementos ímpares da arvore (sum of the odd elements) = %d\n", sum);

	count = ABPMultCount (abp, 5);
	if (ABPErrorCode ()) printf ("Contagem dos elementos da arvore multiplos de 5 (number of elements multiple of 5) = %s\n", ABPErrorMessage ());
	else printf ("Contagem dos elementos da arvore multiplos de 5 (number of elements multiple of 5) = %d\n", count);

	count = ABPLeavesCount (abp);
	if (ABPErrorCode ()) printf ("Contagem das folhas da arvore (number of leaves) = %s\n", ABPErrorMessage ());
	else printf ("Contagem das folhas da arvore (number of leaves) = %d\n", count);

	count = ABPEvenCount (abp);
	if (ABPErrorCode ()) printf ("Contagem dos elementos pares da arvore (number of even elements) = %s\n", ABPErrorMessage ());
	else printf ("Contagem dos elementos pares da arvore (number of even elements) = %d\n", count);

	printf ("--------------------------------------------------------------------------------------------\n");
    printf ("Arvore listada em ordem (inorder traversal) ");
	ABPInOrderRec (abp);
	printf ("\n");
	printf ("--------------------------------------------------------------------------------------------\n");

	sum = ABPOddOrderSum (abp);
	if (ABPErrorCode ()) printf ("Soma dos elementos com numero de ordem ímpar da arvore (sum of elements with odd order number) = %s\n", ABPErrorMessage ());
	else printf ("Soma dos elementos com numero de ordem ímpar da arvore (sum of elements with odd order number) = %d\n", sum);

	printf ("--------------------------------------------------------------------------------------------\n");
    printf ("Elementos pares da arvore por ordem crescente (even elements by increasing order) ");
	ABPEvenPrint (abp);
	printf ("\n");
	printf ("--------------------------------------------------------------------------------------------\n");

	printf ("\n");

	ABPDestroy (&abp);

	return 0;
}

