

.equ SFR_BASE_HI, 0xBF88

.equ TRISE,       0x6100
.equ PORTE,       0x6110
.equ LATE,        0x6120

.equ TRISB,       0x6040
.equ PORTB,       0x6050
.equ LATEB,       0x6060


.data
.text
.globl            main


main:             lui  $t1, SFR_BASE_HI

                  lw   $t2, TRISE($t1)
                  andi $t2, $t2, 0xFFFE
                  sw   $t3, TRISE($t1) #E0 é OUT

                  lw   $t2, TRISB($t1)
                  ori  $t2, $t2, 0x01
                  sw   $t2, TRISB($t1) #E1 é IN

                  #RE0 = RBO => LATE0 = PORTB0
while:            lw    $t2,PORTB($t1) #$t2 = PORTB
                  andi  $t2,$t2,0x01   #t2 = PORB0 (o bit 0)

                  lw    $t3,LATE($t1) #$t3 = LATE
                  andi  $t3,$t3,0xFFFE #$t3 = LATE0 (metemos o E0 a 0 para depois copiar o B0 para lá )

                  #copiar o B0 para o E0
                  or    $t3,$t3,$t2
                  sw    $t3,LATE($t1)
                j     while





# B0 : ultimo (primeiro do in) bit do registo.
#
#           ----------------
#PORT B     |             B0|  IN  // isolar o bit B0 porque queremos copiá-lo para a saída.
#           ----------------
#
#				    B0
#           -----------
#LATE  $t3  |???? ????|    lw $t3, LATE
#           -----------
#
#$t3 AND 1111 1110 = ???? ???0 (fica no $t3)
#$t3 OR  ???? 000B0
