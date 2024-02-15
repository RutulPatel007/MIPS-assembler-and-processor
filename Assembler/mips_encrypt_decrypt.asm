.data
xorKey:.byte '\n'
option:.space 1
outputString:.space 256
inputString: .space 256
options: .asciiz "Type 0 to encrpt string or 1 to decrypt string "
prompt:.asciiz "Enter your data: "
encryptedPrompt: .asciiz "Encrypted data: "
decryptedPrompt:  .asciiz "Decrypted data: "
.text
.globl main
main:
  addi $v0,$zero, 4
  la $a0, options # Printing options prompt to ask user what he/she need to do
  syscall
  addi $v0,$zero, 5 # Taking input from user 
  syscall
  move $t5,$v0 
  addi $v0,$zero, 4 # Printing prompt
  la $a0, prompt
  syscall
  addi $v0,$zero, 8 # Taking data input from user in variable inputString
  la $a0, inputString
  addi $a1,$zero, 256
  syscall
  beq $t5, $zero, encrypt # encrypting data when user chooses 0 as option
  addi $t6,$t6,1
  beq $t5, $t6, decrypt # decrypting data when user chooses 1 as option
  addi $v0,$zero, 10
  syscall
encrypt: 
  addi $t0,$zero, 0 
  la $t1, inputString # Load address of inputString  
  la $t2, outputString # Load address of outputString
encrypt_loop: # encrypting data 
  lb $t3, 0($t1) # loading each byte from inputString
  beq $t3,$zero, encrypt_done
  la $t4,xorKey # load address of xorKey
  lb $t4, 0($t4)# Load byte of xorLey
  xor $t3, $t3, $t4  # each byte of data is xor with xorKey
  sb $t3, 0($t2) # storing that bite in outputString
  addi $t0, $t0, 1  
  addi $t1, $t1, 1 
  addi $t2, $t2, 1 
  j encrypt_loop
encrypt_done:
  addi $v0,$zero, 4 #Prining prompt saying Encrypted data 
  la $a0, encryptedPrompt
  syscall
  addi $v0,$zero, 4 # Printing encrypted data 
  la $a0, outputString
  syscall
  addi $v0,$zero, 10 #To exit the program
  syscall
decrypt:
  addi $t0,$zero,0       
  la $t1, inputString #Load address of inputString
  la $t2, outputString#load address fo outputString
decrypt_loop:
  lb $t3, 0($t1) # decrypting data 
  beq $t3,$zero, decrypt_done
  la $t4,xorKey # Load address of xorKey
  lb $t4, 0($t4)
  xor $t3, $t3, $t4  # each byte of data is xor with xorKey
  sb $t3, 0($t2) # storing that bite in outputString
  addi $t0, $t0, 1
  addi $t1, $t1, 1
  addi $t2, $t2, 1
  j decrypt_loop
decrypt_done:
  addi $v0,$zero, 4 # Printing prompt saying Decrypted data
  la $a0, decryptedPrompt
  syscall
  addi $v0,$zero, 4 # Printing decrypted data
  la $a0, outputString
  syscall
  addi $v0,$zero, 10 # Exit the program
  syscall
