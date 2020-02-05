	.data
	.text
	.globl main
main:	ori $t0, $0, 0x1234
	ori $t1, $0, 0x000F
	and $t2, $t1, $t0
	or $t3, $t1, $t0
	nor $t4, $t1, $t0
	xor $t5, $t1, $t0
not:	nor $t6, $t1, $0
	jr $ra
