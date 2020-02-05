#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count = 0;
int count2 = 0;

int main ( int argc, char **argv ) {

  printf (" --------------------- \n");


  printf ("Recursivo: \n");
  printf ( "n = %d p ( n ) = %d\n", 1 ,  p ( 1 ) ) ;
  printf ("count = %d\n", count) ;

  printf (" --------------------- \n");

  printf("Dinamico:\n");
  printf ( "n = %d pDinamico ( n ) = %d\n", 1 ,  pDinamico( 1 ) ) ;
  printf ("count = %d\n", count2) ;

  printf (" --------------------- \n");


}

int p ( int n ) {

  if ( n <= 1 ) {
    //count++;
    return 0;
  }

  if ( n > 1 ) {
    count = count + 3; // cantar  p ( n / 3 )
                      // contar p ( ( n + 1 ) / 3 )
                      // counter p ( ( n + 2 ) / 3 )
    return n + p ( n / 3 ) + p ( ( n + 1 ) / 3 ) + p ( ( n + 2 ) / 3 ) ;
  }
}

int pDinamico ( int n ) {

  if ( n <= 1 ) return 0 ;

	int tmp = ( n + 2 ) / 3 ;
	int aux [ tmp + 1 ] ;

	aux [ 0 ] = 0 ;
	aux [ 1 ] = 0 ;

	for( int i = 2 ; i <= tmp ; i++ ) {
		count2 = count2 + 3 ;
		aux [ i ] = i + aux [ i / 3 ] + aux [ ( i + 1 ) / 3 ] + aux [ ( i + 2 ) / 3 ] ;
	}

	count2 = count2 + 3 ;
	return n + aux [ n / 3 ] + aux [ ( n + 1 ) / 3 ] + aux [ tmp ];

}
