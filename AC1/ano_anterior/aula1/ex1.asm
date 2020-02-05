	.data
	
ola:	.space 20
	.text
        .globl main

main:	li $t3, 12
	la $t2, ola
	addu $t3, $t3, $t2
	li $v0, 10
	syscall
     
      
      
       
