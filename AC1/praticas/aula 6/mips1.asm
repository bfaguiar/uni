
	.data
ac1:	.asciiz "Arquitectura de computadores I"
	.eqv PRINT_INT10, 1
	.text
	.globl main
	
main:	  subu $sp, $sp, 4
	  sw $ra, 0($sp)
	  la $a0, ac1
	  jal strlen
	  move $t0, $v0
	  li $v0, PRINT_INT10
	  move $a0, $t0
	  syscall
	  lw $ra, 0($sp)
	  addiu $sp, $sp, 4
	  li $v0, 0
	  jr $ra
strlen:   li $t1, 0		# int len = 0;
while:	  lb $t2, 0($a0)
	  addiu $a0, $a0, 1
	  beq $t2, '\0', endwhile
	  addi $t1, $t1, 1
	  j while
endwhile: move $v0, $t1
	  jr $ra
	  