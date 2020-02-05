	.data
	.text
	.globl main
main:   li $t2, 0x12345678
	srl $t1, $t2, 1 	# bin >> 1
	sra $t0, $t2, $t1	# bin ^ (bin >> 1)
	jr $ra
	