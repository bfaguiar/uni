	# Mapa de registos:
	#  $t0 – value
	#  $t1 – bit
	#  $t2 - i

	.data
str1:	.asciiz "Introduza um numero: "
str2:    .asciiz "\nO valor em binário e': "
	.eqv, print_string, 4
	.eqv read_int, 5
	.eqv print_char, 11
	.text
	.globl main
	
main:	li $v0, print_string		# print_string("Introduza um numero: ");
	la $a0, str1			#
	syscall				#
	li $v0, read_int		# 	read_int();
	syscall				#
	move $t0, $v0			#
	li $v0, print_string		# print_string("\nO valor em binário e': ")
	la $a0, str2			#
	syscall				#
	li $t2, 0			#i=0
for:    bge, $t2, 32, endfor		# while( i < 32) {
	rem $t4, $t2, 4			#
if2:	bnez $t4, endf2			#
	li $v0, print_char		#
	li $a0, ' '			#
	syscall				#
endf2:	andi $t1, $t0, 0x80000000	# bit = value & 0x80000000;
if:     beqz $t1, else     		# if(bit != 0)
	li $v0, print_char		# print_char('1');
	li $a0, '1'			#
	syscall				#
	j endif				
else:  li $v0, print_char		# print_char('0');
       li $a0, '0'			#
       syscall				#
endif: sll $t0, $t0, 1      		# // shift left de 1 bit
       addi $t2, $t2, 1			#	i++
       j for				#
endfor: jr $ra				# fim do program, mas nao do total program
        
# fiz ate a alinea d. xomecar a fazer o d.
	
		
	
	