#include <detpic32.h>

char receive = '\0';
void delay(int ms) {

  for(; ms > 0; ms--) {

    resetCoreTimer();
    while (readCoreTimer() < 20000);

  }

}

void main(void) {

  TRISDbits.TRISD5 = 0;
  TRISDbits.TRISD6 = 0;
  TRISB = TRISB & 0x00FF; // ???? ???? ???? ???? & 0000 0000 1111 1111 ==  0000 0000 ???? ????

  LATDbits.LATD5 = 1;
  LATDbits.LATD6 = 0;
  LATB = LATB & 0x00FF; // ???? ???? ???? ???? & 0000 0000 1111 1111 ==  0000 0000 ???? ????

  while(1) {

    do {

      printStr("Escreva um char [a-gA-G] ou o '.': ");
      receive = getChar();

    } while (!((receive >= 'a' && receive <= 'g') || (receive == '.')));

    switch (receive) {
      case 'a':
      LATBbits.LATB8 = 1;
      break;

      case 'b':
      LATBbits.LATB9 = 1;
      break;

      case 'c':
      LATBbits.LATB10 = 1;
      break;

      case 'd':
      LATBbits.LATB11 = 1;
      break;

      case 'e':
      LATBbits.LATB12 = 1;
      break;

      case 'f':
      LATBbits.LATB13 = 1;
      break;

      case 'g':
      LATBbits.LATB14 = 1;
      break;

      case '.':
      LATBbits.LATB15 = 1;
      break;

    }

   }

}
