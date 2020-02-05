# Mapa de registos: . 
# p: $t0
# pultimo:$t1
# *p $t2
# soma: $t3

	.data
	.eqv SIZE, 4
	.eqv print_int10, 1
array:	.word 7692, 23, 5, 234
	.text
	.globl main
	
main:	addi $t3, $0, 0		# int soma = 0;
	la $t0, array			# p = array;
	li $t4, SIZE			#
	subu $t4, $t4, 1
	sll $t4, $t4, 2			# SIZE * 4
	addu $t1, $t0, $t4		# 
	
	
while:	bgt $t0, $t1, endwW		# while( p <= pultimo) {
	lw $t2, 0($t0)			#
	add $t3, $t3, $t2		# soma = soma + (*p);
	addiu $t0, $t0, 4		# p++:
	j while				#
endwW:  li $v0, print_int10		# print_int10(soma);
	 move $a0, $t3			#
	 syscall			#
	 jr $ra				#
	
	
	
	