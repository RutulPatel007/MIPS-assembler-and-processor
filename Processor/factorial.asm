.text
main:
    addi $t0,$zero 9
    addi $t1,$zero 1
    addi $t2,$zero 1
    factorial_loop:
        mul $t1, $t1, $t0
        addi $t0, $t0, -1
        bne $t0, $t2, factorial_loop
	    addi $v0,$zero 1       # Load the service code 1 for printing an integer
    	addi $a0,$t1, 0        # Load the integer value you want to print into $a0
    	#syscall 