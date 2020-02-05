        .equ READ_CORE_TIMER,  11
        .equ RESET_CORE_TIMER, 12
        .equ PRINT_INT, 6
        .equ BASE_PRINT_INT, 10
        .equ PUT_CHAR, 3
        .equ TIME, 2000000
        .data
        .text
        .globl main

main:   li $t1, 0                    #int counter = 0;
        li $t3, TIME                 # $t3 = 200000
while1: li $v0, READ_CORE_TIMER      #
        syscall                      # readCoreTimer();
        move $t2, $v0                #
        blt $t2, $t3, while1           # while (readCoreTimer() < 200000);                    #
        li $v0, RESET_CORE_TIMER     #
        syscall                      # resetCoreTimer();
        addi $t1, $t1, 1             # Counter++
        move $a0, $t1                #
        li $a1, BASE_PRINT_INT       #
        li $v0, PRINT_INT            # printInt(++counter, 10);
        syscall
        li $a0, ' '
        li $v0, PUT_CHAR
        syscall
        j while1
        jr $ra

        
