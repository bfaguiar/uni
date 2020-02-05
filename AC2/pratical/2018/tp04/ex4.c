#include <detpic32.h>

void delay(int ms);


void main(void) {

  unsigned char segment;

  LATDbits.LATD6 = 1; // dis6 = play high active.
  LATDbits.LATD5 = 0; // display low inactive.

  // configure RB8-RB14 as outputs.
  // confgure RD5-RD6 as outputs.

  TRISB = TRISB & 0x00FF; // para configurar os portos RB8-RB14.  0000 0000 para os meter a zero. 1111 1111 para os ????
  TRISDbits.TRISD5 = 0;
  TRISDbits.TRISD6 = 0;
  LATB  = LATB  & 0x800F;



  while(1) {

    LATDbits.LATD6 = !LATDbits.LATD6;
    LATDbits.LATD5 = !LATDbits.LATD5; // toggle display selection

    segment = 1;
    int i;
    for(i = 0; i < 7; i++) {

      LATB = (LATB & 0x00FF) | segment << 8;
      delay(500);
      segment = segment << 1;

    }

  }

}

void delay(int ms) {

  for(; ms > 0; ms--) {

    resetCoreTimer();
    while (readCoreTimer() < 20000);

  }

}
