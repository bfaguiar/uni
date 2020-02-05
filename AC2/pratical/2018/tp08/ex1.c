#include <detpic32.h>

void putc(char byte2send);

void delay(int ms);

int main() {

    U1BRG = (20000000 +8*115200)/ (16*115200)-1;

    U1MODEbits.BRGH   =  0;
    U1MODEbits.STSEL  =  0;
    U1MODEbits.PDSEL  =  0x00;

    U1STAbits.UTXEN   =  1;
    U1STAbits.URXEN   =  1;
    U1MODEbits.ON     =  1;


     // Configure UART1 (115200, N, 8, 1)
     while(1) {

         putc('+');
         // wait 1 s
         delay(1000);

     }

}

void putc(char byte2send) {

    while(U1STAbits.UTXBF == 1);
    U1TXREG = byte2send;

}

void delay(int ms) {
    for(; ms > 0; ms --) {
        resetCoreTimer();
        while(readCoreTimer() < 20000);
    }
}
