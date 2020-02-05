# Mapa de registos # num: $t0
# i: $t1
# str: $t2
# str+i: $t3 # str[i]: $t4

	.data
	
	.eqv SIZE, 20
	.eqv read_string, 8
	.eqv print_int10, 1
	
str:    .space SIZE

         .text
         .globl main
         
main:	la $a0, str  			#$a0 = &(array[0]);
	li $a1, SIZE			#a1 = 20
	
	li $v0, read_string 	        #read string
	syscall				# preenche a memoria alocada na string com o que metemos
	
	li $t0, 0                       # $t0 == num 
	li $t1, 0                       # $t1 = i
	
while:  la $t2, str		        # vai buscar a string na memoria
	addu $t3, $t2, $t1		# posicao str{1i}
	lb $t4, ($t3)			# *p = valor
	beq $t4, '\0', endw             #
	
if:     blt $t4, '0', endif
	bgt $t4, '9', endif
	addi $t0, $t0, 1
	
endif:  addi $t1, $t1, 1
        j while

endw:   li  $v0, print_int10           # service 1 is print integer
        move $a0, $t0  # load desired value into argument register $a0, using pseudo-op
        syscall
	
	li $v0, 10
	syscall
	         