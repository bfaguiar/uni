        # i == $t0
        # lista == $t1
        # lista + i == $t2

	.data
	.eqv SIZE, 5
str1:   .asciiz  "\n Introduza um numero: "
	.align 2
lista:  .space 20
	.eqv read_kint, 5
	.eqv print_string, 4
	.eqv exit, 10
	.text
	.globl main

main:   li  $t0, 0

while:	bge $t0, SIZE, endw
	la  $a0, str1
	li  $v0, print_string
	syscall
	
	li $v0, read_kint
	syscall
	
	la $t1, lista           # carrega a lista &lista(0)
	
	sll $t2, $t0, 2		# lista i
	addu $t2, $t2, $t1	# carrega para o elemento i
	
	sw $v0, 0($t2)		# store word para o t2.
	
	addi $t0, $t0, 1        # incrementa 1
	
	j while		        # salta para o while
	
endw:   li $v0, exit
              syscall
	
	
	
	
	