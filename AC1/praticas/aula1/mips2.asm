	.data
	.eqv print_int16, 34
	.eqv print_intu10, 36
	.text
	.globl main
main:	ori $v0, $0, 5  #syscall para read int: 5
	syscall
	move  $t0,$v0
	ori $t2, $0, 8
	add $t1, $t0, $t0		# x + x = 2x = ...
	sub $t1, $t1, $t2		# y = 2x + 8
	li $v0, print_intu10		#16
	add $a0,$0, $t1
	syscall
	jr $ra