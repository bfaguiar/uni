# Mapa de registos:
#  $t0 – soma
#  $t1 – value
#  $t2 - i
 
	.data
str1:   .asciiz "INTRODUZA UM NUMERO: "
str2:   .asciiz "ALOR IGNORADO \n"
str3:   .asciiz "A soma dos positivos e': "
	.eqv print_string, 4
	.eqv, read_int, 5
	.eqv print_int_10, 1
	.text
	.globl main
	
main: 	li $t2, 0		#i=0
	li $t0, 0 		#soma=0
	li $t3, 5		# valor 5
for: 	bge $t2,$t3, endf	#while( i < 5 ) {
	li $v0, print_string	#print_string("Introduza um numero: ");
	la $a0, str1		#
	syscall			#
	li $v0, read_int	#value = read_int();
	syscall			#
	move $t1, $v0		#
	blez $t1, else		# if (value > 0) {
	add $t0, $t0, $t1	# soma = soma + value;
	j endif			#
else:	li $v0, print_string	#else print_string("Valor ignorado\n");
	la $a0, str2		#
	syscall			#
endif: 	addi $t2, $t2, 1	# i++
	j for
endf:	li $v0, print_string	#print_string("A soma dos positivos e': ");
	la $a0, str3		#
	syscall			#
	li $v0, print_int_10	#  print_int10(soma);
	move $a0, $t0		#
	syscall			#
	jr $ra			#
	
	

	