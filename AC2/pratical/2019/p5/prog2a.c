#include <detpic32.h>

int main () {

  int xx = 1;
  
  TRISBbits.TRISB4 = 1; // configura o porto input e disconecta a parte digital, para ser um input analógico.
  AD1PCFGbits.PCFG4 = 0;  // configurado como porto analógico.
  AD1CON1bits.SSRC = 7;
  AD1CHSbits.CH0SA = 4;
  AD1CON1bits.CLRASAM = 1;
  AD1CON3bits.SAMC = 16; //
  AD1CON2bits.SMPI = xx-1;
  AD1CON1bits.ON = 1;


  while(1) {
    
    AD1CON1bits.ASAM = 1; // starts conve rsion
    while(IFS1bits.AD1IF == 0);
    int *p = (int *) &ADC1BUF0;int i;
    for ( i = 0; i < 16; i++) {
      printInt(p[i*4], 16 | 3 << 16); // o segundo argumento é a base 
      //é o numero de caracteres com que o numero é representado, em hexadecimal.
      // vai imprimir 3 deles e o "<<16" significa que ele está a ir buscar os 
      //16 mlost significantes bits.}
    IFS1bits.AD1IF = 0;

     }

  }

  return 0;

}
