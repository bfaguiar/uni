# Mapa de registos:

	  .data
	  .eqv read_string, 8
	  .eqv print_int, 1
str1:     .asciiz "Arquitetura de Computadores I;" 
	  .text
	  .globl main
	
main:     addiu $sp, $sp, -4      # 
          sw $ra, ($sp)           # passa o valor do $ra, 
	  la $a0, str1            # passagem de argumentos
	  jal strlen              # chamada da funcao
	  move $a0, $v0           #
	  li $v0, print_int       #
	  syscall                 #
	  lw $ra, ($sp)           #
	  addiu $sp, $sp, 4       #
	  jr $ra                  #
	
strlen:   li $t1, 0               # len = 0
while:    lb $t0, ($a0)           # guardar o valor do ponteiro ($a0) // // Pointer moves to the next int position (as if it was an array). But returns the old content. 
	  addiu $a0, $a0, 1       # incrementa o ponteiro
	  beq $t0, '\0', endw     # while *s++ != \0
	  addi $t1, $t1, 1        # len = len + 1
	  j while                 # 
endw:     move $v0, $t1           # return len
	  jr $ra                  # funcao terminal, não preciso de guardar o $ra na stack.
	  
