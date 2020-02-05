#include "delay.h" // se for na directoria de includes é <> se não for (nesta directoria, por exemplo, "");
#include <detpic32.h>

int main () {

  LATE = LATE &0xf0; // o porto tem que ser configurado com um valor inicializado antes de configurarmos como output.
  TRISE = TRISE & 0xFFF0; // tem que estar a 1

  while(1) {

    delay(1000);
    LATE = (LATE + 0x01) & 0x0F; // para nao exceder para mais que 4 bits.

  }

}
