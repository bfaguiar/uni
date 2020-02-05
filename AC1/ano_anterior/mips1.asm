.data
.byte 'c', 'd', 'e'
.word 1
.byte 'c'
.asciiz "ol"
.byte 'c' 'd'
.word 1, 2
.text
.globl main

main:

#li $t2, 7
#li $t3, 6

#rem $t1, $t2, $t3
#li $v0, 1
#move $a0, $t1
#syscall


li $t5, 1

li $v0, 5
syscall
move $a0, $t2

add $t2, $t2, $t5

li $v0, 1
move $a0, $t2

syscall

jr $ra