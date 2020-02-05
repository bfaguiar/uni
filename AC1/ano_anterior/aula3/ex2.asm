# Mapa de registos:
     #  $t0 – value
     #  $t1 – bit
     #  $t2 - i

	.data
	
str1:	.asciiz	"Introduza um numero: " 
str2: 	.asciiz ...

	.eqv print_string, 4 
	.eqv read_int, 5 
	.eqv print_char,...
  	
  	.text 
        .globl main
        
main: 	la $a0, str1		#print string
	li $v0, print_string 	#
	syscall			#
	
	li $v0, read_int	#read int 
	syscall			#
	move $t0, $v0		#
	
	li $t2,0		# i = 2
	
while:  bgt $t2, 32, endw

(...)
# print_char('0'); # value = value << 1; # i++;
#}
#
# fim do programa
jfor endfor:
jr $ra