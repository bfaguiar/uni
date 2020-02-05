
	.data
text1:	.asciiz "Escreva aqui um valor: "
	.eqv read_integer, 5
	.eqv print_string, 4
	.eqv print_int, 1
	.text
	.globl main
	
main:  	la $a0, text1
	li $v0, print_string
	syscall 
 	
 	li $v0, read_integer
	syscall
	move $t0, $v0
	
	mul $t1, $t0, 2
	addi $t1, $t1, 8
	
	move $a0, $t1
	li $v0, print_int
	syscall
	
	jr $ra
	
	