        .equ READ_CORE_TIMER,  11
        .equ RESET_CORE_TIMER, 12
        .equ PRINT_INT, 6
        .equ BASE_PRINT_INT, 10
        .equ PUT_CHAR, 3
        .equ ms, 1000
        .equ TIME, 20000
        .data
        .text
        .globl main

main:   subu $sp, $sp, 8
        sw $ra, 0($sp)
        sw $s0, 4($sp)
        li $s0, 0
while11: li $a0, ms
        jal delay
        addi $s0, $s0, 1             # Counter++
        move $a0, $s0                #
        li $a1, BASE_PRINT_INT       #
        li $v0, PRINT_INT            # printInt(++counter, 10);
        syscall
        li $a0, ' '
        li $v0, PUT_CHAR
        syscall
        j while11
        lw $ra, 0($sp)
        lw $s0, 4($sp)
        addiu $sp, $sp, 8
        jr $ra


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
