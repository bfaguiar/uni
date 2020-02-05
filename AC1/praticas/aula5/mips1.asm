# i: $t0
# lista:  $t1
# lista + i:  $t2

	.data
	.eqv SIZE, 5
str1:  	.asciiz "\n Introduza um numero "
	.align 2
lista:	.space 20
	.eqv read_int, 5
	.eqv print_string, 4
	.text 
	.globl main
	
main:   li $t0, 0
for:    bge $t0, SIZE, endfor
	li $v0, print_string
	la $a0, str1
	syscall
	li $v0, read_int
	syscall
	la $t1, lista
	sll $t2, $t0, 2
	addu $t2, $t2, $t1
	sw $v0, 0($t2)
	addi $t0, $t0, 1
	j for
endfor: jr $ra
 
	 