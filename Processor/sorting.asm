.data
ar:.word 9 15 6 5 4 3 2 1
.text
	
	li $t1,0x10010000
	addi $t8 $t8,7
	addi $t9,$t9, 0
	addi $t5,$t5,0#i
	addi $s5,$s5,-1
for:	
	beq $t5,$t8,done
	sub $t4,$t8,$t5#n-i-1
	addi $t6,$zero,0 #j
	addi $t3,$t1,0  #&(ar[i])
	addi $t5,$t5,1  #i++
	j for2
					
for2:
	beq $t6,$t4,for
	lw $s1,0($t3)
	addi $t3, $t3,4
	lw $s2, 0($t3)
	addi $t6,$t6,1
	
	blt $s1, $s2, for2
	sw $s1,0($t3)
	sw $s2,-4($t3)
	j for2
	
done:
	addi $t4,$zero,0
