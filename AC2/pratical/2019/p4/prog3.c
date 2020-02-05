#include <detpic32.h>

int main() {

  LATB = LATB & 0x00FF;
  //LATD = LATD & 0xFF9F;
  LATDbits.LATD5 = 1;
  // tambem se pode fazer assim: LATDbits.LATD5 = 0;

  TRISB = TRISB & 0x00FF;
  TRISD = TRISD & 0xFF9F;

  while(1) {

    char ch = getChar();
    putChar(ch);

    if ((ch > 'b') || (ch < 'f') || (ch == '.') ) {

      switch(ch ) {

        case 'B':
        LATB = (LATB & 0x00FF) | 0x7C00;
        break;

        case 'b':
        LATB = (LATB & 0x00FF) | 0x7C00;
        break;

        case 'c':
        LATB = (LATB & 0x00FF) | 0x3900;
        break;

        case 'd':
          LATB = (LATB & 0x00FF) | 0x5E00;
        break;

        case 'e':
          LATB = (LATB & 0x00FF) | 0x7900;
        break;

        case 'f':
          LATB = (LATB & 0x00FF) | 0x7100;
        break;

      }
    } else  exit(0);
  }

}
/*

N DP  G F E D C B A 0x...


*/
