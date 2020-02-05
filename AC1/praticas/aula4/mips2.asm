# Mapa de registos 
# num: $t0
#p: $t1
# *p: $t2


	 .data
	  .eqv SIZE, 20
	  .eqv print_int10, 1
str:	 .space SIZE
	 .eqv read_string, 8
	 .text 
	 .globl main
	 
main:	 li $t0, 0			# int num = 0;
	 li $v0, read_string		# read_string(str, SIZE);
	 la $a0, str			# nao precisamos de retornar o valor porque operamos sobre uma lista, logo nao precisamos de carregar o valor do v0.
	 li $a1, SIZE			#
	 syscall
	 la $t1, str			# p = str;
while:   lb $t2, 0($t1)			# load byte $t1
	 beq $t2, '\0', endwhile	# while(*p!='\0')
if:	 blt $t2, '0', endif		# if( (str[i] >= '0')
	 bgt $t2, '9', endif		# (str[i] <= '9')
	 addi $t0, $t0, 1
endif:   addiu $t1, $t1, 1
	 j while
endwhile: li $v0, print_int10
	 move $a0, $t0
	 syscall
	 jr $ra
	 

	 
