#include <detpic32.h>

void main(void) {
  static const char display7Scodes[] = { 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x70, 0x07, 0x7F, 0x6F, 0x77, 0x7C, 0x39, 0x5E, 0x7C, 0x71 };

  int dpswitch;

  TRISB = (TRISB & 0x80FF) | 0x000F; /*
                                                15 14 13 12     11 10 9 8      7 6 5 4    3 2 1 0

                                                                            	???? ???? ???? ????
                                                                            and 1000 0000 1111 1111
                                                                            	--------------------
                                                                                ?000 0000 ???? ????    # 80FF
                                                                            or  0000 0000 0000 1111
                                                                                -------------------
                                                                                ?000 0000 ???? 1111    #000F

                                            */

 PORTB = PORTB & 0xF0;    // valor inicial a zero configura entrada
 /* ?000 0000 ???? 1111
   and        1111 0000
   --------------------
   ?000 0000 ???? 0000    PORTB[0-3] = 0;
*/


 LATB  = LATB  & 0x80FF; //  valor inicial. a zero. configura saída.

 /* ?000 0000 ???? 1111
and 1000 0000 1111 1111
   --------------------
   ?000 0000 ???? 1111   PORT[14-8] = 0;
*/


 TRISDbits.TRISD5 = 0;
 TRISDbits.TRISD6 = 0;

 LATDbits.LATD6 = 0; // disp. inativo
 LATDbits.LATD5 = 1; // disp. activo

  while(1) {

    dpswitch = PORTB & 0x0F;
    /* ?000 0000 ???? 0000
    and          0000 1111
     --------------------
      ?000 0000 0000 0000  dp = 0;
     */

     LATB = (LATB & 0x00FF)|(display7Scodes[dpswitch] << 8); // vai dar shift para o valor do dp ir para o final porque a saída é nos mais significativos.

     /* ?000 0000 ???? 1111
    and ?000 0000 1111 1111
        -------------------
        ?000 0000 ???? 1111  para nao fazer conflito com os anteriores.
    */  /* restaura o zero. */

    /* ?000 0000 ???? 1111
       ???? ???? 0000 0000 dp
or     -------------------
       ???? ???? ???? 1111   1º's ???? ???? são para ir os displays7scores. xD.

      */


  }


}
