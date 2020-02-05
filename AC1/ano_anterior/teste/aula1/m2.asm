
	.data
str1:	.word 1
str2:   .word 0x12
	.text
	.globl main

main:  
      	la $a0, str1
        li $v0, 1
        syscall
        jr $ra 
        
        
        
	
