	.data
	.text 
	.globl main
	
main:   ori $t0, $0, 0x0F1E
	#ori $t1, $0, 0x000F
	#and $t2, $t0, $t1
	#or $t3, $t0, $t1
	nor $t4, $0, $t0
	#xor $t5, $t1, $t0
	jr $ra
	
	
	
	
	
	
