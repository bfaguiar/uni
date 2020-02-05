# Mapa de registos
# ...
# houve_troca: $t4
# i: $t5
# lista: $t6
# lista + i: $t7

	.data
str1:   .asciiz "; "
str2:   .asciiz "\n Conteudo do Array: \n"
lista:  .space 40
        .align 2
        .eqv SIZE, 10
        .eqv TRUE, 1
        .eqv FALSE 0
	.text
	.globl main
	
main:   