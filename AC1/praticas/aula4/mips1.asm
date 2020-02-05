# Mapa de registos # num: $t0
# i: $t1
# str: $t2
# str+i: $t3 
# str[i]: $t4

	 .data
	  .eqv SIZE, 20
	  .eqv print_int10, 1
str:	 .space SIZE
	 .eqv read_string, 8
	 .text 
	 .globl main

main: 	 li $v0, read_string		# read_string(str, SIZE);
	 la $a0, str			# nao precisamos de retornar o valor porque operamos sobre uma lista, logo nao precisamos de carregar o valor do v0.
	 li $a1, SIZE			#
	 syscall			#
	 #move $t2, $v0			# $t2 == str[0]
	 li $t0, 0			# $t0 == num == 0
	 li $t1, 0			# $t1 == i   == 0
while:   la $t2, str
	 addu $t3, $t2, $t1          	# $t3 == str + 1
	 lb $t4, 0($t3)			# $t4 == load byte do $t3
	 beq $t4, '\0', endwhile		# while( str[i] != '\0' )
if:	 blt $t4, '0', endif		# if( (str[i] >= '0')
	 bgt $t4, '9', endif		# (str[i] <= '9')
	 addi $t0, $t0, 1		# num++

endif:   addiu $t1, $t1, 1
	 j while
endwhile:li $v0, print_int10
	 move $a0, $t0
	 syscall
	 jr $ra
	 
	 