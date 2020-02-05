#include <detpic32.h>

int main() {

  // Prescaler >= 20 * 10⁶ /  (2¹⁶ - 1 + 1) * 2 >= 152, logo o prescaler vai ser o 256.
  T3CONbits.TCKS = 7; // ir ao manual do PIC32MX, ver o prescale value... 256 == 111(2) == 7(10)
  // PR3 = ( ( 20 000 000 / 256 ) / 2 ) - 1 = 390615 < 2¹⁶
  PR3 = 39061 ;
  // reset T3 count register.
  TMR3 = 0 ;
  // enable register counter.
  T2CONbits.TON = 1;

  IPC3bits.T3IP = 2; // interrupt.
  IEC0bits.T3IE = 1; // enable timer t3 interrupts.
  IFS0bits.T3IF = 0; // reset timer t3 interrupt flag.

  EnableInterrupts();
  while(1);
  // while ( 1 ) {
  //
  //   while(IFS0bits.T3IF == 0);
  //   EnableInterrupts();
  //   //reset
  //   IFS0bits.T3IF = 0;
  //   putChat('.');
  // }
}
      // T3  == posicao 12 do array.
void _int_(12) isr_T3(void) {

  IFS0bits.T3IF = 0;
  putChar('.');

}
