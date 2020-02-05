#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count;
int countDinamico;

int main( int argc, char **argv) {

    for (int i = 0; i < 13; i++) {
      count = 0;
      printf ( "\n n = %d Motzkin ( n ) = %d\n", i , Motzkin ( i ) ) ;
      printf ("count = %d\n", count) ;
    }

    printf ( "--------------------\n n = %d Motzkin Dinamico ( n ) = %d\n", 2 , MotzkinDinamico ( 2 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 3 , MotzkinDinamico ( 3 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "-\n n = %d Motzkin Dinamico ( n ) = %d\n", 4 , MotzkinDinamico ( 4 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin  Dinamico ( n ) = %d\n", 5 , MotzkinDinamico ( 5 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin  Dinamico ( n ) = %d\n", 6 , MotzkinDinamico ( 6 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 7 , MotzkinDinamico ( 7 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 8 , MotzkinDinamico ( 8 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 9 , MotzkinDinamico ( 9 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 10 , MotzkinDinamico ( 10 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 11 , MotzkinDinamico ( 11 ) ) ;
    printf ("count = %d\n", countDinamico) ;
    printf ( "\n n = %d Motzkin Dinamico ( n ) = %d\n", 12 , MotzkinDinamico ( 12 ) ) ;
    printf ("count = %d\n", countDinamico) ;
  }

int Motzkin (int n) {

  if (n == 1) return 1;

  if (n == 0) return 1;

  if (n > 1) {

    int MotzkinVariable = 0;

    for (int k = 0; k <= n - 2; k++) {
          count++;
          MotzkinVariable += Motzkin(k) * Motzkin(n-2-k);
    }

    return Motzkin(n - 1) + MotzkinVariable;
  }

  }

  int MotzkinDinamico (int n) {

    countDinamico = 0;

    if (n < 1) {
        return 1;
    }

    int array[n + 1];
    array[0] = 1;
    array[1] = 1;

    int MotzkinVariable;

    for (int i = 2; i <= n ; i++) {
      MotzkinVariable = 0;
      for (int k = 0; k <= i - 2; k++) {
        countDinamico++;
        MotzkinVariable += array[k] * array[i - 2 - k];
      }
      array[i] = array[i - 1] + MotzkinVariable;
    }
    return array[n];
  }
