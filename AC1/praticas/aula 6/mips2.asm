# Mapa de registos:
# str: $a0 -> $s0 (argumento é passado em $a0)
# p1:  $s1  (registo callee-saved)
# p2:  $s2  (registo callee-saved)
# os ponteiros nao precisam de serem guardados, porque so apontam para a memoria


		.data
ac1: 		.asciiz "ITED - orievA ed edadisrevinU"
		.eqv print_string, 4
		.text
		.globl main
		
main:          	addiu $sp, $sp, -4
		sw $ra, 0($sp)
		la $a0, ac1
		jal strrev
		move $a0, $v0
		li $v0, print_string
		syscall
		 lw $ra, 0($sp)
	  	addiu $sp, $sp, 4
		li $v0, 0
		jr $ra
		

strrev:		addiu $sp, $sp, -16
		sw $ra, 0($sp)
		sw $s0, 4($sp)		#str: $a0
		sw $s1, 8($sp)		#$piq1
		sw $s2, 12($sp)
		move $s0, $a0
		move $s1, $a0
		move $s2, $a0
while:		lb $t2, 0($s2)			# nos guardamos aqui rm t1 porque depois nao vamos utilizar mais o valor do t1
		beq $s2, '\0', endwhile
		addiu $s2, $s2, 1
		j while
endwhile:       subu $s2, $s2, 1
while2:         bge $s1, $s2, endwhile2
		move $a0, $s1
		move $a1, $s2
		jal exchange
		move $s1, $v0
		move $s2, $v1
		addiu $s1, $s1, 1
		addiu $s2, $s2, -1
		j while2
endwhile2:	move $v0, $s0
		lw $ra, 0($sp)
		lw $s0, 4($sp)
		lw $s1, 8($sp)
		lw $s2, 12($sp)
		jr $ra

exchange:
		lw $t1, 0($a0)		#c1
		lw $t2, 0($a1)		#c2
		sb $t1, 0($a1)
		sb $t2, 0($a0)
		jr $ra
		
		