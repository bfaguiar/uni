# Mapa de registos:
# str: $a0 -> $s0 (argumento é passado em $a0)
# p1: $s1 (registo callee-saved)
# p2: $s2 (registo callee-saved)
# 
	
	.data
	.text
	.globl strrev
	
strrev:	addiu $sp, $sp, -16
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $s2, 12($sp)
	move $s0, $a0
	move $s1, $a0
	move $s2, $a0
	
	lb $t0, 0($s1)
	lb $t1, 0($s2)
	
while1:	beq $t1, '\0', endW1
	addiu $s2, $s2, 1
	lb $t1, 0($s2)
	j while1
	
endW1:	addiu $s2, $s2, -1

while2:	bge $s1, $s2, endW2
	
	move $a0, $s1
	move $a1, $s2
	jal exchange
	
	addiu $s1, $s1, 1
	addiu $s2, $s2, -1
	j while
	
endW2:	move $v0, $s0
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp)
	addu $sp, $sp, 16
	
	jr $ra
	

exchange:
		lw $t1, 0($a0)		#c1
		lw $t2, 0($a1)		#c2
		sb $t1, 0($a1)
		sb $t2, 0($a0)
		jr $ra