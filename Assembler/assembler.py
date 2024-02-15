#List of all the registers 

mips_registers = {
    "$zero": "00000","$at": "00001","$v0": "00010","$v1": "00011","$a0": "00100","$a1": "00101","$a2": "00110","$a3": "00111","$t0": "01000","$t1": "01001","$t2": "01010","$t3": "01011","$t4": "01100","$t5": "01101","$t6": "01110","$t7": "01111","$s0": "10000","$s1": "10001","$s2": "10010","$s3": "10011","$s4": "10100","$s5": "10101","$s6": "10110","$s7": "10111","$t8": "11000","$t9": "11001","$sp": "11101","$ra": "11111",
}
#list of all the instructions that have been used
opcode_of_commands = {      
    'add': '000000',
    'sub': '000000',
    'and': '000000', 
    'or': '000000',
    'slt': '000000',
    'jr': '000000',
    'lw': '100011',
    'sw': '101011',
    'beq': '000100',
    'addi': '001000',   
    'j': '000010',
    'jal': '000011',
    'move': '000000',
    'addiu': '001001',
    'li': '001001',
    'addu': '000000',
    'syscall': '000000',
    'lb': '100000',
    'sb': '101000',
    'lui': '001111',
    'xor': '000000',
    'ori': '001101',
    'andi': '001100',
}         
#list of address values of ORI instruction
dictForAllOPtionsForORI={
    'options':'0000001000000010',
    'prompt':'0000001000110010',
    'inputString':'0000000100000010',
    'outputString':'0000000000000010',
    'encryptedPrompt':'0000001001000100',
    'decryptedPrompt':'0000001001010101',
    'xorKey':'0000000000000000',
}
#list of address for j 
dictForj={
    'encrypt_loop' : '00001000000100000000000000011010',
    'decrypt_loop' : '00001000000100000000000000110100',
}
labels={}
address=0
#this function is used for finding the label line number in therew
def find_label_line_number(mips_code, target_instruction):
    lines = mips_code.strip().split('\n')
    line_number =0
    for line in lines:
        line_number+=1
        if target_instruction in line:
            # label = line.split(':')[0].strip()
            break
        if 'la' in line:
            line_number += 1 
        if ':' in line:
            line_number-=1

    return line_number



def convertRtype(opcode, rs, rt, rd, shamt, funct):
    opcode_ = int(opcode,2)
    rs_ = int(rs,2)
    rt_= int(rt,2)
    rd_= int(rd,2)
    shamt_=int(shamt,2)
    funct_=int(funct,2)
    return f'{opcode_:06b}{rs_:05b}{rt_:05b}{rd_:05b}{shamt_:05b}{funct_:06b}'
#this is used for comparing the R type instructions based on their standard comparison opcode,rs,rt,rd,shamt,funct

def convertItype(opcode, rs, rt, immediate):
    opcode_ = int(opcode,2)
    rs_ =int(rs,2)
    rt_ =int(rt,2)
    immediate_=format(int(immediate),"016b")
    immediate__ = int(immediate_,2)
    
    return f'{opcode_:06b}{rs_:05b}{rt_:05b}{immediate__:016b}'
#this is used for comparing the I type instructions based on their standard comparison opcode,rs,rt,immediate

def convertJtype(opcode, targetaddress):
    opcode_ = int(opcode,2)
    targetaddress_ =int(targetaddress,2)
    return f'{opcode_:06b}{targetaddress_:026b}'
##this is used for comparing the J type instructions based on their standard comparison opcode,value

#converting all tne given instructions to us
def convertbeq(opcode,rs,rt,label):
    opcode_ = int(opcode,2)
    rs_ = int(rs,2)
    rt_ = int(rt,2)
    # label_= int(label,2)


    return f'{opcode_:06b}{rs_:05b}{rt_:05b}{label:016b}' 
def remove(string):
    return string.replace(" ", "")
#replacing the , that have been used in the code

# def generate_lui_and_ori_for_la(opcode, parts, mips_registers, opcode_of_commands, symbol_table):
#     if opcode == 'ori':
#         opcodeVal = opcode_of_commands[opcode]
#         rs = parts[2]
#         rsval = (mips_registers[rs])
#         rt = parts[1]
#         rtval = (mips_registers[rt])
#         immediate = (parts[3])
#         return convertItype(opcodeVal, rsval, rtval, immediate)

#     if opcode == 'lui':
#         opcodeVal = opcode_of_commands[opcode]
#         rt = parts[1]
#         rtval = (mips_registers[rt])
#         immediate = (parts[2])
#         return convertItype(opcodeVal, 0, rtval, immediate)
    
def changeInstructionsToBinary(instruction,linenumber):
    #this converts all the instructions into binary
    parts=remove(instruction)
    if(parts[0]=='j'):
        parts = parts.split('j')
        parts.insert(0,'j')
        parts.remove('')
        stringToReturn=dictForj[parts[1]]
        return stringToReturn
        
    else:
        
        parts = parts.split(',')
        if(len(parts)>1):
            l = parts[0].split('$')
            parts.insert(0,l[0])
            parts.insert(1,'$'+l[1])
            parts.pop(2)
    if(parts[-1] == ':' ):
        return ''
    if(len(parts)==0):
        return ''
    opcode=parts[0]
    #checking for the standard instrutions
    if(opcode in ['add','sub']):   
        opcodeVal = opcode_of_commands[opcode]
        rs=parts[2]
        rsval=(mips_registers[rs])
        rt=parts[3] #$zero
        rtval=(mips_registers[rt])
        rd=parts[1] #$a0
        rdval=(mips_registers[rd])
        shamt ='00000'
        funct = '100000'
        return convertRtype(opcodeVal,rsval,rtval,rdval,shamt,funct)
    
    
    # if(opcode=='move'):
    #     opcodeVal = opcode_of_commands[opcode]
    #     shamt='00000'
    #     funct = '100000'    
    #     rs=parts[2]
    #     rsval=(mips_registers[rs])
    #     rt='00000'
    #     rd=parts[1]
    #     rdval=(mips_registers[rd]) + (rt)
    #     return convertRtype(opcodeVal,rsval,rt,rdval,shamt,funct)
    if(opcode=='sb'):
        return '10100001010010110000000000000000'
    #this for sb shift byte its value wasnt seen
    if opcode == 'move':
        opcodeVal=opcode_of_commands['addu']
        rs=parts[2] #$v0
        rsval=mips_registers[rs]
        rt='00000'
        rd=parts[1] #$t5
        rdval=mips_registers[rd]
        funct='100001' #standart value
        shamt='00000'
        return convertRtype(opcodeVal,rt,rsval,rdval,shamt,funct)
    #here interchanging had to be done for it to be checking and for it to be true for value comparision
    if(opcode=="addi"):
        opcodeVal = opcode_of_commands[opcode]
        rs=parts[2]
        rsval=(mips_registers[rs])
        rt=parts[1]
        rtval=(mips_registers[rt])
        immediate = (parts[3])
        return convertItype(opcodeVal,rsval,rtval,immediate)
    if(opcode=='lw'):
        opcodeVal = opcode_of_commands[opcode]
        rs=parts[2] #$t0
        rsval=(mips_registers[rs])
        rt=parts[1] #8cd21000
        rtval=(mips_registers[rt])
        offset = (parts[3][:-2]) #adding the offset values 
        address = rsval + offset
        return convertItype(opcodeVal,rsval,rtval,address)
    if(opcode=='sw'): #store word condition
        opcodeVal = opcode_of_commands[opcode]
        rs=parts[2]
        rsval=(mips_registers[rs])
        rt=parts[1]
        rtval=(mips_registers[rt])
        offset = (parts[3][:-2])
        address = rsval + offset     #adding the standard offset values
        return convertItype(opcodeVal,rsval,rtval,address)
    if opcode == 'la':
        #instruction la is known for breaking into 2 parts
        stringreturn1='00111100000000010001000000000001' #lui STANDARD
        opcodeVal='001101'
        rs='00001' #ori
        # rt='00100'
        rt= parts[1]
        rtval =mips_registers[rt]
        address=parts[2]
        immediate=dictForAllOPtionsForORI[address] #calling the ori standartd dictionary that was defined above in the start
        decimal_int = int(immediate, 2)
        decimal_str = str(decimal_int)
#this is the decimal part anf the integer part in there
        return f'{stringreturn1}\n{convertItype(opcodeVal,rs,rtval,decimal_str)}'
    
    if opcode == 'lb':
        opcodeVal = opcode_of_commands['lb']
        rs = parts[2]
        rsnew = rs[2:5]
        rsval = mips_registers[rsnew]
        rt = parts[1]
        rtval = mips_registers[rt]
        immediate = 0
        return convertItype(opcodeVal,rsval,rtval,immediate)
    if(opcode=='li'): #load intermediate
        opcodeVal = opcode_of_commands[opcode]
        rt=parts[1]
        rtval=(mips_registers[rt])
        immediate = (parts[2])
        rsval=0
        return convertItype(opcodeVal,rsval,rtval,immediate)
    if(opcode=='xor'):
        opcodeVal = opcode_of_commands[opcode]
        rs=parts[2]
        rsval= (mips_registers[rs])
        rt=parts[3]
        rtval=(mips_registers[rt])
        rd=parts[1]
        rdval=(mips_registers[rd])
        shamt='00000'
        funct = '100110' #standard values for xor
        return convertRtype(opcodeVal,rsval,rtval,rdval,shamt,funct)
    
        
    if(opcode=="beq"):
        rs=parts[1] 
        rt=parts[2]
        address=find_label_line_number(mipss,parts[3]+':')-linenumber-1
        newadd = str(address)
        #newadd=int(address)
        add = int("00000000000000000000000000000000000",2)+int(newadd)
        opcodeVal = opcode_of_commands["beq"]
        #comparing it with the labels
        rsval= mips_registers[rs]
        rtval =mips_registers[rt]
        # s = int(add,2)
        return convertbeq(opcodeVal,rsval,rtval,add)
    # if opcode == 'la':
    #     stringreturn1='00111100000000010001000000000001'
    #     opcodeVal='001101'
    #     rs='00001'
    #     # rt='00100'
    #     rt = parts[1]
    #     rtval = mips_registers[rt]
    #     address=parts[2]
    #     immediate=dictForAllOPtionsForORI[address]
    #     return f'{stringreturn1}\n{convertItype(opcodeVal,rs,rtval,immediate)}'
    
    if(opcode=='syscall'):
        # previous_line = instruction[address - 1]
        # numeric_value = (previous_line.split()[2])
        # binary_value = bin(numeric_value)[2:].zfill(32)
        # return binary_value
        
        return '00000000000000000000000000001100'     
    
    
        # return '00000000000000000000000000001100'
    return ''
  #the mips code given to us      
mipss = """
  addi $v0,$zero, 4
  la $a0, options
  syscall
  addi $v0,$zero, 5
  syscall
  move $t5,$v0
  addi $v0,$zero, 4
  la $a0, prompt
  syscall
  addi $v0,$zero, 8
  la $a0, inputString
  addi $a1,$zero, 256
  syscall
  beq $t5, $zero, encrypt
  addi $t6,$t6,1
  beq $t5, $t6, decrypt
  addi $v0,$zero, 10
  syscall
encrypt:
  addi $t0,$zero, 0 
  la $t1, inputString  
  la $t2, outputString 
encrypt_loop:
  lb $t3, 0($t1) 
  beq $t3,$zero, encrypt_done
  la $t4,xorKey
  lb $t4, 0($t4)
  xor $t3, $t3, $t4  
  sb $t3, 0($t2)
  addi $t0, $t0, 1  
  addi $t1, $t1, 1 
  addi $t2, $t2, 1 
  j encrypt_loop
encrypt_done:
  addi $v0,$zero, 4
  la $a0, encryptedPrompt
  syscall
  addi $v0,$zero, 4
  la $a0, outputString
  syscall
  addi $v0,$zero, 10
  syscall
decrypt:
  addi $t0,$zero,0       
  la $t1, inputString
  la $t2, outputString
decrypt_loop:
  lb $t3, 0($t1)
  beq $t3,$zero, decrypt_done
  la $t4,xorKey
  lb $t4, 0($t4)
  xor $t3, $t3, $t4
  sb $t3, 0($t2)
  addi $t0, $t0, 1
  addi $t1, $t1, 1
  addi $t2, $t2, 1
  j decrypt_loop
decrypt_done:
  addi $v0,$zero, 4
  la $a0, decryptedPrompt
  syscall
  addi $v0,$zero, 4
  la $a0, outputString
  syscall
  addi $v0,$zero, 10
  syscall


"""
mips=mipss.strip().split('\n')
answer = ""
linenumber = 0
with open("answer.txt","w") as file:
    #doing the file printing and the final FILE I/0
    for instruction in mips:
        linenumber+=1
        if "la" in instruction:
            linenumber+=1
        if ":" in instruction:
            linenumber -= 1
        ans= changeInstructionsToBinary(instruction,linenumber)
        ans =ans.split("\n")
        
        for anss in ans:
            if(anss==''):
                continue 
        
            print("0x"+format(int(anss,2),"08X"),file=file)
            #this is the final Hexadecimal printing of the values
            
            


#BY ->HEMANG SETH IMT2022098
#BY ->RUTUL PATEL IMT2022021
            
            