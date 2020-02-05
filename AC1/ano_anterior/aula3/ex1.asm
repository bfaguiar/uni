# Mapa de registos:
#  $t0 – soma
#  $t1 – value
#  $t2 - i

	.data
str1:   .asciiz "Introduza um numero: "
str2:   .asciiz "Valor Ignorado."
str3:   .asciiz "A soma dos positivos e':"

	.eqv, print_String, 4
	.eqv, read_Int, 5
	.eqv, print_Int10,1 
	.eqv, exit_Program, 10
	
	.text
	.globl main
	
main:   li $t0, 0		#soma = 0;
	li $t1, 0		#value = 0;
	li $t2, 0      	        #i = 0;

while:  bge $t2, 5, endw	
	
	la $a0, str1		#print string
	li $v0, print_String	#
	syscall                 #
	
	li $v0, read_Int	#read int
	syscall                 #
	move $t1, $v0           #

if:     blez $t1, else
	add $t0, $t0, $t1
	j endif
	
else: 	la $a0, str2		#print string
	li $v0, print_String	#
	syscall                 #
	
endif:  addi $t2, $t2, 1        #
	j while			#
	
endw:  	la $a0, str3		#print string
	li $v0, print_String	#
	syscall                 #
	
	move $a0, $t0		#print int
	li $v0, print_Int10	#
	syscall                 #
	
	li $v0, exit_Program    # terminar a programa pela syscall. 
	syscall
	
	