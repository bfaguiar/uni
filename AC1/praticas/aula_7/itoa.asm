# registos que precisamos de guardar: s, b e in

	.data
	.text
	.globl strrev, strcpy

itoa:	addiu $sp, $sp, -16
	sw $ra, 0($sp)		
	sw $s0, 4($sp)		# n
	sw $s1, 8($sp)		# b
	sw $s2, 12($sp)		# s
	sw $s3, 16($sp)		# p
	move $s0, $a0
	move $s1, $a1
	move $s2, $a2
	move $s3, $s2		#  char *p = s; 
do:	divu $s0, $s1		#  n = n / b; 
	mflo $s0		# 	; 
	mfhi $s1		#  #  digit = n % b
	move $a0, $t1
	jal toascii
	sb $v0, 0($s3)
	addiu $s3, $s3, 1
	bgtz $s0, do
	sb, '\0', 0($s3)
	move $a0, $s2
	jal strrev
	move $v0, $s2
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp)
	lw $s3, 16($sp)
	jr $ra

toascii: addiu $a0, $a0, '0'
	 ble $a0, '9', endif
	 addiu $a0, $a0, 7
endif:   move $v0, $a0
	 jr $ra




	