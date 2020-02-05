        .equ ms, 10000
        .data
        .text
        .globl main
main:   li $a0, ms
        jal delay



delay:  move $t1, $a0
for:    blez $t1, endf
        li $v0, RESET_CORE_TIMER     #
        syscall                      # resetCoreTimer();
        li $t3, TIME                 # $t3 = 200000
while1: li $v0, READ_CORE_TIMER      #
        syscall                      # readCoreTimer();
        move $t2, $v0                #
        blt $t2, $t3, while1         # while (readCoreTimer() < 200000);
        addi $t1, $t1, -1
        j for
endf:   jr $ra
