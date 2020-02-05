      .equ printStr, 8
      .equ printInt, 6
      .equ printInt10, 7
      .equ readStr, 9
      .equ STR_MAX_SIZE, 20
      .data
str1: .space STR_MAX_SIZE + 1
str2: .space STR_MAX_SIZE + 1
str3: .space 2*STR_MAX_SIZE + 1
      .space
      .text
      .globl main

main: jr $ra
