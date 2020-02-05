#include <stdio.h>
#include <stdlib.h>

/* alusão da função que implementa o algoritmo pretendido */
/* allusion to the function that implements the algorithm */
int PairOfEqualElements (int [], int);

/* variável global para contar as operações aritméticas executadas pelo algoritmo */
/* global variable for counting the arithmetic operations executed by the algorithm */
int Count = 0;

int main (void)
{
	/* declaração dos arrays de teste - usar o pretendido para cada execução */
	/* declaration of the test arrays - use each one for each execution */

	/* int Array[] = { 1, 2, 2, 8, 3, 4, 5, 3, 8, 2 }; */
	/* int Array[] = { 1, 2, 4, 7, 6, 3, 9, 5, 0, 8 }; */
	/* int Array[] = { 2, 1, 0, 4, 3, 5, 7, 9, 8, 6 }; */
	/* int Array[] = { 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 }; */

	int Array[] = {   1, 2, 2, 8, 3, 4, 5, 3, 8, 2  };
	int NElem = sizeof (Array) / sizeof (int); int Result;

	/* invocação do algoritmo pretendido - algorithm invocation */
	Result = PairOfEqualElements (Array, NElem);

	/* apresentação do resultado e do número de operações de comparação executadas pelo algoritmo */
	/* presenting the result and the number of comparation operations executed by the algorithm */

	fprintf (stdout, "Resultado = %3d N. de operacoes = %3d\n", Result, Count);

	exit (EXIT_SUCCESS);
}

/* implementação do algoritmo pretendido */
/* não se esqueça de contar as operações aritméticas executadas pelo algoritmo usando a variável global */

/* implementation of the pretended algorithm */
/* do not forget to count the arithmetic operations using the global variable */

int PairOfEqualElements (int array[], int n)
{
	int num = 0;
	for (int i = 0; i < n; i++) {
		for (int k = 0; k < i; k++) {
			if (array[i] == array[k]) {
				num++;
			}
			Count++;
		}
	}
	/* acrescentar o código do algoritmo - insert your code */
	return num;
}
