#include <detpic32.h>


void delay(int ms) {

   for(; ms > 0; ms--) {

     resetCoreTimer();
     while (readCoreTimer() < 20000);

   }

}

vo2id main(void) {

  /*
  *
  * TRISxn = 0 sair, 1 entrar
  * LATxn = configurar  outsair
  * PORTxn = configurar entrada
  *
  */

   TRISDbits.TRISD0 = 0; // RD0 configured as output

   LATDbits.LATD0 = 0; // The initial value should be set


   while(1) {

     delay(500); // half period = 0.5s
     LATDbits.LATD0 = !LATDbits.LATD0;

   }

}




