# Mapa de registos:

	  .data
	  .eqv read_string, 8
	  .eqv print_int, 1
str1:     .asciiz "2016 e 2020 sao anos bissextos" 
	  .text
	  .globl main
	 
main:     addiu $sp, $sp, -4      # 
          sw $ra, ($sp) 
	  la $a0, str1            # passagem de argumentos
	  jal atoi
	  move $a0, $v0           #
	  li $v0, print_int       #
	  syscall                 #
	  lw $ra, ($sp)           #
	  addiu $sp, $sp, 4       #
	  jr $ra


# Mapa de registos # res: $v0
# s: $a0
# *s: $t0
# digit: $t1# Mapa de registos # res: $v0
 #Sub-rotina terminal: não devem ser usados registos $sx
# s: $a0
# *s: $t0
# digit: $t1
# Sub-rotina terminal: não devem ser usados registos $sx
 
atoi:  lui $v0, 0    # res   = 0;
while: lb $t0, ($a0) # *s carregar o valor do s.
       blt $t0, '0', endw
       bgt $t0, '9', endw
       sub $t1, $t0, '0'
       addi $t0, $t0, 1
       mulu $v0, $v0, 10 
       add $v0, $v0, $t1
endw:  jr $ra 
