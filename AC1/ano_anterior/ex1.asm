	.data
	.text
        .globl main

main:	ori $v0, $0, 5       # t0 = x
        syscall
      	ori $t2, $0, 8     	 # t2 = 8
      	add $t1, $t0, $t0    	 # y = x + x <=> 2*x
        sub $t1, $t1, $t2        # y = y - 8
        jr $ra
       