.equ SFR_BASE_HI, 0xBF88        # 16 MSbits of SFR area
.equ TRISE, 0x6100              # TRISE address is 0xBF886100
.equ PORTE, 0x6110             # PORTE address is 0xBF886110
.equ LATE,  0x6120              # LATE  address is 0xBF886120

.equ TRISB, 0x6040
.equ SFR_BASE_HI, 0xBF88        # 16 MSbits of SFR area
.equ TRISE, 0x6100              # TRISE address is 0xBF886100
.equ PORTE, 0x6110             # PORTE address is 0xBF886110
.equ LATE,  0x6120              # LATE  address is 0xBF886120

.equ TRISB, 0x6040
.equ PORTB, 0x6050
.equ LATB,  0x6060


.data
.text
.globl main

main:   li $t1, 0

lui $t2, SFR_BASE_HI
lw  $t3, TRISE($t2)
andi $t3, $t3 0xFFFE # confugirar o pino TRISE0 Como saída, #TRISE0 = 0
sw $t3, TRISE($t2)

while: lw $t4, LATE($t2)
#limpar
or $t4, $t4, $t1
