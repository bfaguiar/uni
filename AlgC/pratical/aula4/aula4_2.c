#include <stdio.h>
#include <stdlib.h>

/* alusão da função que implementa o algoritmo pretendido */
/* allusion to the function that implements the algorithm */
int NumberOfSequences (int [], int);

/* variável global para contar as operações aritméticas executadas pelo algoritmo */
/* global variable for counting the arithmetic operations executed by the algorithm */
int Count = 0;

int main (void)
{
	/* declaração dos arrays de teste - usar o pretendido para cada execução */
	/* declaration of the test arrays - use each one for each execution */

	int Array[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
	// int Array[] = { 1, 2, 2, 2, 2, 3, 3, 5, 8, 8 };
	// int Array[] = { 1, 2, 2, 2, 3, 3, 3, 5, 8, 8 };
	//int Array[] = { 2, 2, 2, 2, 2, 2, 2, 3, 3, 3 };
 
	
		int NElem = sizeof (Array) / sizeof (int); int Result;

	/* invocação do algoritmo pretendido - algorithm invocation */ 
	Result = NumberOfSequences (Array, NElem);

	/* apresentação do resultado e do número de operações de comparação executadas pelo algoritmo */
	/* presenting the result and the number of comparation operations executed by the algorithm */

	fprintf (stdout, "Resultado = %3d N. de operacoes = %3d\n", Result, Count);

	exit (EXIT_SUCCESS);
}

/* implementação do algoritmo pretendido */
/* não se esqueça de contar as operações aritméticas executadas pelo algoritmo usando a variável global */

/* implementation of the pretended algorithm */
/* do not forget to count the arithmetic operations using the global variable */

int NumberOfSequences (int array[], int n)
{
	/* acrescentar o código do algoritmo - insert your code */
	if (n < 3) return 0;
	int contador = 0;
	int i;
	for (i = 0; i < n-2; i++) {
		Count++;
		if ((array[i] == array[i+1])) {
		Count++;
			if (array[i] == array[i+2]) {
				contador++;
		}
	}
}
	return contador;
}

