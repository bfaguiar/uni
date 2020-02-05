#include <detpic32.h>

int main() {

  // Prescaler >= 20 * 10⁶ /  (2¹⁶ - 1 + 1) * 2 >= 152, logo o prescaler vai ser o 256.
  T3CONbits.TCKS = 7; // ir ao manual do PIC32MX, ver o prescale value... 256 == 111(2) == 7(10)
  // PR3 = ( ( 20 000 000 / 256 ) / 2 ) - 1 = 390615 < 2¹⁶
  PR3 = 390615 ;
  // reset T3 count register.
  TMR3 = 0 ;
  // enable register counter.
  T2CONbits.TON = 1;

  while ( 1 ) {

    while(IFS0bits.T3IF == 0);
    //reset
    IFS0bits.T3IF = 0;
    putChat('.');
  }
}
