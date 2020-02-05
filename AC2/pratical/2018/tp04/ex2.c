#include <detpic32.h>

int contador = 0x00;

void delay(int ms) {

   for(; ms > 0; ms--) {

     resetCoreTimer();
     while (readCoreTimer() < 20000);

   }

}

void main(void) {
  
   LATE  = LATE  & 0xf0;
   TRISE = TRISE & 0xf0; // Re3 até Re0 configurado como output.

   while(1) {

     contador = (contador + 1) & 0x0F; // para não exceder (contar mais do que) 4 bits. F == 16 == 16 combinações. O primeiro zero é para prever o complemento para dois, para não ser negativo.
     delay(500); // half period = 0.5s
     LATE = (LATE & 0xf0) | contador; // o "|" é equivalente ao "OR OPERATOR", transferindo o contador para o LATE.

   }

}
