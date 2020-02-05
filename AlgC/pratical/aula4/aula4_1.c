#include <stdio.h>
#include <stdlib.h>

/* alus�o da fun��o que implementa o algoritmo pretendido */
/* allusion to the function that implements the algorithm */
int OnlyEvenNumbers (int [], int);

/* vari�vel global para contar as opera��es aritm�ticas executadas pelo algoritmo */
/* global variable for counting the arithmetic operations executed by the algorithm */
int Count = 0;

int main (void)
{
	/* declara��o dos arrays de teste - usar o pretendido para cada execu��o */
	/* declaration of the test arrays - use each one for each execution */

	// int Array[] = { 1, 2, 6, 8, 4, 8, 2, 2, 6, 4 };
	// int Array[] = { 2, 3, 6, 8, 8, 4, 6, 2, 6, 4 };
	/* int Array[] = { 2, 4, 5, 6, 8, 2, 4, 6, 6, 8 }; */
	/* int Array[] = { 2, 4, 6, 1, 8, 6, 2, 4, 6, 8 }; */
	// int Array[] = { 2, 4, 6, 8, 1, 6, 2, 5, 6, 7 };
	// int Array[] = { 2, 4, 6, 8, 4, 1, 8, 2, 6, 7 };  
	/* int Array[] = { 2, 6, 6, 4, 8, 2, 1, 6, 7, 4 }; */
	/* int Array[] = { 2, 2, 6, 8, 4, 2, 8, 3, 4, 9 }; */
	 int Array[] = { 4, 2, 6, 8, 4, 2, 8, 6, 5, 4 }; 
	/* int Array[] = { 2, 2, 6, 8, 4, 2, 8, 6, 4, 9 }; */
	/* int Array[] = { 4, 2, 6, 8, 4, 2, 8, 6, 2, 4 }; */

	int NElem = sizeof (Array) / sizeof (int); int Result;

	/* invoca��o do algoritmo pretendido - algorithm invocation */ 
	Result = OnlyEvenNumbers (Array, NElem);

	/* apresenta��o do resultado e do n�mero de opera��es aritm�ticas executadas pelo algoritmo */
	/* presenting the result and the number of arithmetic operations executed by the algorithm */
	if (Result) fprintf (stdout, "Verifica ");
	else fprintf (stdout, "Nao verifica ");

	fprintf (stdout, "Resultado = %3d N. de operacoes = %3d\n", Result, Count);

	exit (EXIT_SUCCESS);
}

/* implementa��o do algoritmo pretendido */
/* n�o se esque�a de contar as opera��es aritm�ticas executadas pelo algoritmo usando a vari�vel global */

/* implementation of the pretended algorithm */
/* do not forget to count the arithmetic operations using the global variable */

int OnlyEvenNumbers (int array[], int n)
{
	int i; 
 	if (n <= 0) return 0; 
	for (i = 0; i < n; i++) {
		Count++;
		if (array[i] % 2 != 0)
			return 0;
		
	}
	return 1;
}

