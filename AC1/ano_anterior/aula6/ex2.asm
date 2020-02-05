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
	  jal strrev              # chamada da funcao
	  move $a0, $v0           #
	  li $v0, print_int       #
	  syscall                 #
	  lw $ra, ($sp)           #
	  addiu $sp, $sp, 4       #
	  jr $ra                  #
	  
strrev:   addiu $sp, $sp, -16
	  sw    $ra, 0($sp)
	  sw    $s0, 4($sp)
	  sw    $s1, 8($sp)
	  sw    $s2, 12($sp)
	  move  $s0, $a0           # para depois retornar o valor do início do string.
	  move  $s2, $a0           # guardar os valores na stack para a próxima sub-rotinia não alterar os valores
	  move  $s1, $a0           # 
while1:   beq ($s2), '\0' , endw1  #
          addiu $s2, $s2, 4        #
          j while1
endw1:    subiu $s2, $s2, 4
while2:   bge $s1, $s2, endw2
          move $a0, $s1
          move $a1, $s2
	  
	  
	  
