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

main:   lui $t1, SFR_BASE_HI        #Mem_addr: 0xBF880000=
        lw  $t2, TRISE($t1)         #READ: Mem_addr: 0xBF880000 + 0x00006110 = 0xBF886110
        andi $t2, $t2, 0xFFFE       #MODIFY porto E0 para meter como saída
        sw  $t2, TRISE($t1)         #WRITE Write TRISE register

        lw $t3, TRISB($t1)
        ori $t3, $t3, 0x0001
        sw $t3, TRISB($t1)

whinf:  lw $t4, PORTB($t1)          # tenho que ler a word do porto b: uma word tem 32 bits
        and $t4, $t4, 0x0001        # pego nos 16 bits menos significativos e vou buscar o ultimo  bit da word

        lw $t5, LATE($t1)           # vou carregar a word do LATE
        andi $t5, $t5, 0xFFFE       # para limpa todos os bit E0 porque se ja tivessemos um um e quisessemos ter um zero, iria ficar 1+0:1
        or $t5, $t5, $t4           # vou carregar o ultimo bit do $t4 no registo $t5

        sw $t5, LATE($t1)

        j whinf

        jr $ra
