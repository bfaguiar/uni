int main() {

  LATB = LATB & 0x00FF;
  LATD = LATD & 0xFF9F;
  // tambem se pode fazer assim: LATDbits.LATD5 = 0;

  TRISB = TRISB & 0x00FF;
  TRISD = TRISD & 0xFFBF;

  while(1) {

    char ch = getchar();

    switch(ch < 'a' || ch > 'g' || ch == '.') {

      case 'B':
      LATEB = (LATB & 0x00FF) | 0x7C;
      break;

      case 'b':
      LATEB = (LATB & 0x00FF) | 0x7C;
      break;

      case 'c':
      LATEB = (LATB & 0x00FF) | 0x39;
      break;

      case 'd':
        LATEB = (LATB & 0x00FF) | 0x5E;
      break;

      case 'e':
        LATEB = (LATB & 0x00FF) | 0x79;
      break;

      case 'f':
        LATEB = (LATB & 0x00FF) | 0x71;
      break;

    }
  }

}
/*

N DP  G F E D C B A 0x...


*/
