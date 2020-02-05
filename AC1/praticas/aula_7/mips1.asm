
	.data
stri:   .asciiz "2016 e 2020 sao anos bissextos"
stri1:  .asciiz "101101"
stri2:  .asciiz "101100"
	.eqv, print_10, 1
	.text
	.globl main

# Mapa de registos # res: $v0
# s: $a0
# *s: $t0 
# digit: $t1

main:		subu $sp, $sp, 4
		sw $ra, 0($sp)
		la $a0, stri1
		jal atoi
		move $t1, $v0
		move $a0, $t1
		li $v0, print_10
		syscall
		lw $ra, 0($sp)
		addiu $sp, $sp, 4
		li $v0, 0
		jr $ra

atoi: 		li $v0, 0 				# res = 0;
while:		lb $t0, 0($a0)				#
		blt $t0, '0', endwhile			#
		bgt $t0, '9', endwhile			# while( (*s >= '0') && (*s <= '9') )
		subu $t1, $t0, '0'
		addiu $a0, $a0, 1
		mul $v0, $v0, 2				# binario para ascii. se for decimal por ascii: substituir o 2 por 10: res = 10 * res + digit;
         						#  ; digit = *s++ - '0'
		add $v0, $v0, $t1
		j while
endwhile:	jr $ra
