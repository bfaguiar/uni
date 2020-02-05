# Mapa de registos 
# p: $t0 
# *p: $t1 
# lista+Size: $t2

	.data
	.eqv SIZE, 10
	.eqv print_int10, 1
	.eqv print_string, 4
str1:   .asciiz "\nConteudo do array:\n"
str2:   .asciiz "; "
	.align 2
lista:  .word, 8, -4, 3, 5, 124, -15, 87, 9, 27, 15 
	.text
	.globl main
	
main: 	li $v0, print_string
	la $a0, str1
	syscall
	la $t0, lista 
	li $t2, SIZE
	sll $t2, $t2, 2
	addu $t2, $t2, $t0
for:	bge $t0, $t2, endfor
	lw $t1, 0($t0)
	li $v0, print_int10
	move $a0, $t1
	syscall
	li $v0, print_string
	la $a0,str2
	syscall
	addiu $t0, $t0, 4
	j for
endfor: jr $ra

