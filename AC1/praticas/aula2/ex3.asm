	.data
str1:	.asciiz "Uma string qualquer"
str2:	.asciiz "AC1 - P"			#3Uma string qualquer
	.eqv print_string, 4
	.word 0x12345678
	.text
	.globl main
main: 	la $a0,str2
	ori $v0, $0, print_string
	syscall 
	jr $ra