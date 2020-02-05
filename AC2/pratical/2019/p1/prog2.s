         .equ PRINT_STR, 8
         .equ INKEY, 1
         .data
str:     .asciiz "Key Pressed"
         .text
         .globl main
main:
while1:
while2:   li $v0, INKEY
          syscall     #$v0 = c = inkey()
          beq $v0, $0, while2 # while(c==0)
          beq $v0, '\n', endwhile
          la $a0, str
          li $v0, PRINT_STR
          syscall
          j while1
endwhile: li $v0, 0
          jr $ra



#inkey: vai la ver se chegou alguem, se estiver um caracter devolve, se nao estiver lá, devolve zero.

#o getchar é bloqueante, ele fica lá até chegar um char e depois devolve.
