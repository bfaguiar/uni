           .equ getChar, 2
           .equ putChar, 3
           .data
           .text
           .globl main

main:
while1:    li $v0, getChar              #
           syscall                      # c = getChar()
if:        beq $v0, '\n', exitwhile     # if (c == '\n')
           move $a0, $v0                # else
           #li $a0, 'c' # para provar que os caracteres vêm do programa e não sobre o facto de eu estar a escrever na bash
           li $v0, putChar              # putChar()
           syscall                       #
           j while1                      #
exitwhile: li $v0, 1                    # return 1
           jr $ra                       #
