	.data
	.text
	.globl main
main:	ori $t0, $0, 5
	ori $t2, $0, 8
	add $t1, $t0, $t0		# x + x = 2x = ...
	sub $t1, $t1, $t2		# y = 2x + 8
	jr $ra
	