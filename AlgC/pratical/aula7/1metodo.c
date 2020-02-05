#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count = 0;

int main ( int argc, char **argv ) {
  printf ( "n = %d x^n = %d\n", 4, powCalculator( 2.0,4 ) ) ;
  printf ("count = %d", count) ;
}

int powCalculator ( double x, int n ) {

  if ( n == 0 ) {
    return 1.0;
  }

  if ( n == 1 ) {
    return x * 1;
    count++;
  }

  x = x * powCalculator ( x, n-1 );
  count++;

  return x;
}

int powCalculator2 ( double x, int n ) {

  if ( n == 0 ) {
    return 1;
  }

  if ( n % 2 == 0 ) {
    return (powCalculator2 ( x , n/2 )) * (powCalculator2 ( x , n/2 ));
    count ++;
  }

  if ( n % 2 != 0 ) {
    return (powCalculator2 ( x , n )) * ((powCalculator2 ( x , n/2 )) * (powCalculator2 ( x , n/2 )));
  }

}
