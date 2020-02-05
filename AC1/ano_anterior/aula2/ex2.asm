	.data
 	.text
 	.globl main


gray = bin ^ (bin >> 1); 




main:   li $t0, 0x12345678 # instrução virtual (decomposta           # em duas instruções nativas)
        srl $t3,$t0, 1 #
        sra $t4,$t0, 1 #
        jr $ra # fim do programa
        
        
    
