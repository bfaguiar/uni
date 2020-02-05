        .equ printStr, 8
        .equ printInt, 6
        .equ printInt10, 7
        .equ readInt10, 5
        .data
str:    .asciiz "\nIntroduza um numero (sinal e modolo): "
base2:  .asciiz "\nvalor lido em base 2: "
base16: .asciiz "\nValor lido em base 16: "
base10u:.asciiz "\nValor lido em base 10 (unsigned): "
base10: .asciiz "\nValor lido em base 10 (signed): "
        .text
        .globl main

main:
while1: la $a0, str
        li $v0, printStr
        syscall

        li $v0, readInt10
        syscall
        move $t2, $v0

        la $a0, base2
        li $v0, printStr
        syscall

        move $a0, $t2
        li $a1, 2
        li $v0, printInt
        syscall

        la $a0, base16
        li $v0, printStr
        syscall

        move $a0, $t2
        li $a1, 16
        li $v0, printInt
        syscall

        la $a0, base10u
        li $v0, printStr
        syscall

        move $a0, $t2
        li $a1, 10
        li $v0, printInt
        syscall

        la $a0, base10
        li $v0, printStr
        syscall

        move $a0, $t2
        li $v0, printInt10
        syscall
        j while1
        jr $ra
