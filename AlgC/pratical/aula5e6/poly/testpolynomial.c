/*******************************************************************************

 Programa simples de simulação da funcionalidade do TDA POLY


 Autor : António Manuel Adrego da Rocha    Data : Março de 2017

*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "polynomial.h"

void WritePoly (PtPoly);

int main (void)
{
	PtPoly poly0 = NULL, poly1 = NULL, poly2 = NULL, poly3 = NULL, poly4 = NULL; double res;

	system ("clear");
	poly0 = PolyCreateFile ("p0.txt");
	printf ("\nPolinomio lido do ficheiro\n");
	WritePoly (poly0);

	poly1 = PolyCreateFile ("p1.txt");
	printf ("\nPolinomio lido do ficheiro\n");
	WritePoly (poly1);
	
	poly3 = PolySymmetrical (poly1);
	printf ("\nPolinomio simetrico\n");
	WritePoly (poly3);

	poly2 = PolyCreateFile ("p2.txt");
	printf ("\nPolinomio lido do ficheiro\n");
	WritePoly (poly2);

	poly4 = PolyAddition (poly0, poly1);
	printf ("\nPolinomio soma\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	poly4 = PolyAddition (poly1, poly0);
	printf ("\nPolinomio soma\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	poly4 = PolySubtraction (poly0, poly1);
	printf ("\nPolinomio diferenca\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	poly4 = PolySubtraction (poly1, poly0);
	printf ("\nPolinomio diferenca\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	poly4 = PolyMultiplication (poly0, poly1);
	printf ("\nPolinomio produto\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	poly4 = PolyMultiplication (poly1, poly0);
	printf ("\nPolinomio produto\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);
	
	poly4 = PolyAddition (poly1, poly3);
	printf ("\nPolinomio soma com o simetrico\n");
	WritePoly (poly4);
	PolyDestroy (&poly4);

	res = PolyEvaluation (poly0, 0.5);
	printf ("\nResultado = %f\n", res);

	printf ("\nDestruir os polinomios\n");
	PolyDestroy (&poly1);
	PolyDestroy (&poly2);
	PolyDestroy (&poly3);

	WritePoly (poly3);

	return 0;
}

void WritePoly (PtPoly ppol)
{
  int i, degree = PolyDegree (ppol); double coef;

  if (ppol != NULL)
  {
    /* escrita no monitor do coeficiente x^n */
    /* writing on screen the x^n coefficient */
    coef = PolyObserveCoefficient (ppol, degree);
    if (degree > 1) printf ("%5.2f x^%d", coef, degree);
    else if (degree == 1) printf ("%5.2f x", coef);

    /* escrita no monitor dos coeficientes x^n-1 ... x^2 para polinomios com grau > 1 */
    /* writing on screen the x^n-1 ... x^2 coefficients for polynomials with degree > 1 */
    if (degree > 1)
      for (i = degree-1; i > 1; i--)
      {
        coef = PolyObserveCoefficient (ppol, i);
        if (coef >= 0.0) printf (" + %5.2f x^%d", coef, i);
        else printf (" - %5.2f x^%d", fabs(coef), i);
      }

    /* escrita no monitor do coeficiente x para polinomios com grau > 1 */
    /* writing on screen the x coefficient for polynomials with degree > 1 */
    
    if (degree > 1)
    {
      coef = PolyObserveCoefficient (ppol, 1);
      if (coef >= 0.0) printf (" + %5.2f x", coef);
      else printf (" - %5.2f x", fabs(coef));
    }

    /* escrita no monitor do coeficiente independente */
    /* writing on screen the independent coefficient */
    if (degree > 0)
    {
      coef = PolyObserveCoefficient (ppol, 0);
      if (coef >= 0.0) printf (" + %5.2f\n", coef);
      else printf (" - %5.2f\n", fabs(coef));
    }
    else printf ("%5.2f\n", coef);
  }
}

