print("Enter 1 for Factorial and 2 For Sorting")
a=int(input())
#TAKING THE CHOICE OF THE INPUT
mips_registers={"00000": "$zero", "00001": "$at", "00010": "$v0", "00011": "$v1", "00100": "$a0",
"00101": "$a1", "00110": "$a2", "00111": "$a3", "01000": "$t0", "01001": "$t1",
    "01010": "$t2", "01011": "$t3", "01100": "$t4", "01101": "$t5", "01110": "$t6",
    "01111": "$t7", "10000": "$s0", "10001": "$s1", "10010": "$s2", "10011": "$s3",
    "10100": "$s4", "10101": "$s5", "10110": "$s6", "10111": "$s7", "11000": "$t8",
    "11001": "$t9", "11101": "$sp", "11111": "$ra",
}
# print(mips_registers)

#LIST OF ALL THE INSTRUCTIONS THAT ARE BEING USED

opcode_of_commands = {      
    'add': '000000',
    'sub': '100010',
    'and': '000000', 
    'or': '000000',
    'slt': '101010',
    'mul' : '011100',
    'jr': '000000',
    'lw': '100011',
    'sw': '101011',
    'beq': '000100',
    'addi': '001000',   
    'j': '000010',
    'bne':'000101',
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
opcode_of_commands = {value: key for key, value in opcode_of_commands.items()}

#LIST OF ADDRESS VALUES FOR THE ORI INSTRUCTION

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

# I type contains opcodes

I_type_instructions={
    0x04:"beq",
    0x23:"lw",
    0x2B:"sw",
    }

# j type contains opcodes

J_type_instructions = {
    0x02:"j",
}

#this contains the instruction memory

instruction_memory= [
0x20080005,
0x20090001,
0x200A0001,
0x71284802,
0x2108FFFF,
0x150AFFFD,
0x20020001,
0x21240000,
]
#these are the hexadecimal values of the factorial .asm when ran in MIPS

instruction_memory_sorting=[
0x3c011001,
0x34290000,
0x23180007,
0x23390000,
0x21ad0000,
0x22b5ffff,
0x11b8000f,
0x030d6022,
0x200e0000,
0x212b0000,
0x21ad0001,
0x0810000c,
0x11ccfff9,
0x8d710000,
0x216b0004,
0x8d720000,
0x21ce0001,
0x0232082a,
0x1420fff9,
0xad710000,
0xad72fffc,
0x0810000c,
0x200c0000,

]
#this is of the sorting when ran in MIPS assembler


instruction_dictionary_sorting={
0x10010000 : 0x00000009,
0x10010004 : 0x0000000f,
0x10010008 : 0x00000006,
0x1001000C : 0x00000005,
0x10010010 : 0x00000004,
0x10010014 : 0x00000003,
0x10010018 : 0x00000002,
0x1001001C : 0x00000001,
}

# mips_registers_values1 = {
#     "$zero": 0,
#     "$at": 0,
#     "$v0": 0,
#     "$v1": 0,
#     "$a0": 0,
#     "$a1": 0,
#     "$a2": 0,
#     "$a3": 0,
#     "$t0": 0,
#     "$t1": 0,
#     "$t2": 0,
#     "$t3": 0,
#     "$t4": 0,
#     "$t5": 0,
#     "$t6": 0,
#     "$t7": 0,
#     "$s0": 0,
#     "$s1": 0,
#     "$s2": 0,
#     "$s3": 0,
#     "$s4": 0,
#     "$s5": 0,
#     "$s6": 0,
#     "$s7": 0,
#     "$t8": 0,
#     "$t9": 0,
#     "$k0": 0,
#     "$k1": 0,
#     "$gp": 0,
#     "$sp": 0,
#     "$fp": 0,
#     "$ra": 0
# }
# global RegWrite 
RegWrite=0
# global MemRead 
MemRead=0
# global MemWrite 
MemWrite=0
# global MemtoReg 
MemtoReg=0
# global ALUSrc 
ALUSrc=0
# global ALUControl
ALUControl=0
# global RegDst 
RegDst=0
# global Branch 
Branch=0
# global Jump  
Jump=0
# global ALUOp 
ALUOp=""
# global PCSrc 
PCSrc=0
#assigning the control signals 
global bin_instruction 
bin_instruction = ""

mips_registers_values = {
    "$zero": 0,
    "$at": 0,
    "$v0": 0,
    "$v1": 0,
    "$a0": 0,
    "$a1": 0,
    "$a2": 0,
    "$a3": 0,
    # "$at": 0,
    "$t0": 0,
    "$t1": 0,
    "$t2": 0,
    "$t3": 0,
    "$t4": 0,
    "$t5": 0,
    "$t6": 0,
    "$t7": 0,
    "$s0": 0,
    "$s1": 0,
    "$s2": 0,
    "$s3": 0,
    "$s4": 0,
    "$s5": 0,
    "$s6": 0,
    "$s7": 0,
    "$t8": 0,
    "$t9": 0,
    "$k0": 0,
    "$k1": 0,
    "$gp": 0,
    "$sp": 0,
    "$fp": 0,
    "$ra": 0
}

# clk1=0
# global pc1
# pc1=0


#THESE ARE THE GIVEN CONTROL SIGNALS FOR THE INSTRUCTIONS


clk=0
global pc
pc=0

answer_file_output = open("output_nonpipeline.txt", "w")

# xx=open("output.txt","w")
def if_stage(instruction_memory, clk):
    print("IF Stage",file=answer_file_output)
    # print(pc,file=xx)
    instruction = instruction_memory[pc]
    inst = format((0x00400000 + (pc * 4)), "08x")
    # if(instruction == 0x71284802):
    #     print("Instruction Binary Code: 00000001001010010100000000000000")
    #     mul_instruction = "00000001001010010100000000000000"
    # else:
    print("Instruction address: " + "0x" + inst,file=answer_file_output)
    print("Instruction Binary Code: " + format(instruction, "032b"),file=answer_file_output)
    # clk += 1
    print(f"CLOCK: {clk}",file=answer_file_output)
    print('-----X-----',file=answer_file_output)
#THIS IS THE INSTRUCTION FETCH STAGE
#IN THIS STAGE WE ARE ONLY FETCCHING THE INSTRUCTION AND PRINTING IT
#HERE WE PRINT THE MEMORY INSTRUCTIONS AND ALL THE OTHER INSTRUCTIONS


#------------------------------------------------------------------------



def id_phase(instruction_memory, mips_registers, opcode_of_commands,clk):
    global bin_instruction
    global pc
    global RegWrite
    global MemRead
    global MemWrite
    global MemtoReg
    global ALUSrc
    global ALUControl
    global RegDst
    global Branch
    global Jump
    global ALUOp
    global PCSrc
    instruction1 = instruction_memory[pc]
    bin_instruction = format(instruction1, "032b")
    
    
    #THIS IS THE ID STAGE WHICH IS USING THW CONSTROL INSTRUCTIONS 
    
    if(bin_instruction[:6]=="000000"):
        RegWrite=1
        MemRead=0
        MemWrite=0
        MemtoReg=0
        ALUSrc=0
        RegDst=1
        Branch=0
        Jump=0
        ALUOp="10"
        PCSrc=0
    if(bin_instruction[:6]=="001000"):
        RegWrite=1
        MemRead=0
        MemWrite=0
        MemtoReg=0
        ALUSrc=1
        RegDst=0
        Branch=0
        Jump=0
        ALUOp="00"
        PCSrc=0
    if(bin_instruction[:6]=="000100"):
        RegWrite=0
        MemRead=0
        MemWrite=0
        MemtoReg=0
        ALUSrc=0
        RegDst=0
        Branch=1
        Jump=0
        ALUOp="01"
        PCSrc=1
    if(bin_instruction[:6]=="000010"):
        RegWrite=0
        MemRead=0
        MemWrite=0
        MemtoReg=0
        ALUSrc=0
        RegDst=0
        Branch=0
        Jump=1
        ALUOp="00"
        PCSrc=1
    if(bin_instruction[:6]=="011100"):
        RegWrite=1
        MemRead=0
        MemWrite=0
        MemtoReg=0
        ALUSrc=0
        RegDst=1
        Branch=0
        Jump=0
        ALUOp="10"
        PCSrc=0
    if(bin_instruction[:6]=="100011"):
        RegWrite=1
        MemRead=1
        MemWrite=0
        MemtoReg=1
        ALUSrc=1
        RegDst=0
        Branch=0
        Jump=0
        ALUOp="00"
        PCSrc=0

    #these are the control signals for the instructions
    
    
    print("ID phase",file=answer_file_output)
    
    
    
    if bin_instruction[:6] == "011100":
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21]
        shamt = int(bin_instruction[21:26], 2)
        funct = bin_instruction[26:32]
        print(f'opcode : {bin_instruction[:6]}',file=answer_file_output)
        print(f"rs = {mips_registers[rs]} rt = {mips_registers[rt]} rd = {mips_registers[rd]} shamt = {shamt} funct = {funct}",file=answer_file_output)
        print(f"Instruction = mul {mips_registers[rd]},{mips_registers[rs]},{mips_registers[rt]}",file=answer_file_output)


#PPRINTING THE DIFFERENT TYPES OF INSTRUCTIONS BASED ON THIER GIVEN OPCODE 

    elif bin_instruction[:6] == "000000":
        print("R type instruction",file=answer_file_output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21]
        shamt = int(bin_instruction[21:26], 2)
        funct = bin_instruction[26:32]
        print(f'opcode : {bin_instruction[:6]}',file=answer_file_output)
        print(f"rs = {mips_registers[rs]} rt = {mips_registers[rt]} rd = {mips_registers[rd]} shamt = {shamt} funct = {funct}",file=answer_file_output)
        print(f"Instruction = {opcode_of_commands[funct]} {mips_registers[rd]},{mips_registers[rs]},{mips_registers[rt]}",file=answer_file_output)
    
    elif bin_instruction[:6] == "000010":
        print("J type instruction",file=answer_file_output)
        print(f'opcode : {bin_instruction[:6]}',file=answer_file_output)
        address = int(bin_instruction[6:32], 2)
        print(f"address = {address}",file=answer_file_output)
        # int initial = 0x40000000
        print(f"Instruction = {address}",file=answer_file_output)
    
    else:
        print("I type instruction",file=answer_file_output)
        opcode = bin_instruction[:6]
        print(f'opcode : {bin_instruction[:6]}',file=answer_file_output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        #print(rs,rt,end=" ")
        immediate = int(bin_instruction[16:32],2)
        print(f"rs = {rs} rt = {rt} immediate = {immediate}",file=answer_file_output)
        print(f"Instruction = {opcode_of_commands[opcode]} {mips_registers[rt]},{mips_registers[rs]},{immediate}",file=answer_file_output)
    # clk+=1
    print(f"CLOCK : {clk}",file=answer_file_output)
    print('-----X-----',file=answer_file_output)
    
    
  #--------------------------------------------------------------
  
    
def exe_stage(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk):
    print('EXE Stage',file=answer_file_output)
    result = 0
    answer = 0
    global pc
    stringtocheck = format(int(bin_instruction,2),"08x")

#HERE WE ARE STORING THE ANSWERS AND UPDATING THE GIVEN RESULTS
#APART FROM THAT HERE WE ARE ALSO DOING THE NECESSARY VALUE UPDATAL OF THE GIVEN REGISTERS THAT WE HAD DEFINED IN THE GIVEN ABOVE DICTIONARY 

    # if(stringtocheck=="0x3c011001"):
    #     pc+=2
    #     rs = format(int(bin_instruction[6:11], 2), "05b")
    #     rt = format(int(bin_instruction[11:16], 2), "05b")
    #     immediate = int(bin_instruction[16:32], 2)
    #     mips_registers_values[mips_registers[rt]] = mips_registers_values[mips_registers[rs]] + immediate

        
    if (bin_instruction[:6] == "011100" and RegWrite==1 and RegDst==1):
        print("mul",file=answer_file_output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21]
        shamt = bin_instruction[21:26]
        funct = bin_instruction[26:32]
        # print(funct)
        mips_registers_values[mips_registers[rd]] = mips_registers_values[mips_registers[rt]] * mips_registers_values[mips_registers[rs]]
        # answer = mips_registers_values[mips_registers[rs]]
        # print(mips_registers_values[mips_registers[rs]])
        # print(mips_registers_values[mips_registers[rt]])
        # print(mips_registers_values[mips_registers[rd]])
        # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rs]]}")
    elif (bin_instruction[:6] == "000000" and RegWrite==1 and RegDst==1):
        print("R type instruction",file=answer_file_output)
        #COMPARING THE CONTROL SIGNALS VALUES 
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21]
        #print(rs,rt,rd,end=" ")
        #print(rs,rt,rd,end=" ")
        shamt = bin_instruction[21:26]
        funct = bin_instruction[26:32]
        # print(funct)
        # rd = mips_registers[rd]
        if funct ==  "101010":
            if mips_registers_values[mips_registers[rs]] < mips_registers_values[mips_registers[rt]]:
                # print(rd)
                # print(mips_registers[rd])
                # print(mips_registers_values[mips_registers[rd]])
                mips_registers_values[mips_registers[rd]] = 1
            else:
                mips_registers_values[mips_registers[rd]] = 0
        # print(f"Instruction = {funct} ${rd},${mips_registers[rs]},${mips_registers[rt]}")
        if funct == "100010":
            mips_registers_values[mips_registers[rd]] = mips_registers_values[mips_registers[rs]] - mips_registers_values[mips_registers[rt]]
    elif bin_instruction[:6] == "000010" and MemRead==0 and RegWrite==0 and Jump==1:
        print("J type instruction",file=answer_file_output)
        # print(f'opcode : {bin_instruction[:6]}')
        print(bin_instruction[6:32],file=answer_file_output)
        
        address = int("0000"+bin_instruction[6:32]+"00", 2)
        print(address,file=answer_file_output)
      
        # print(f"address = {address}")
        # print(f"Instruction = {address}")s
        # inst = format((0x40000000 + (pc * 4)), "08x")
        anwer=(pc*4)+4194304-address
        anwer//=4
        print(anwer,file=answer_file_output)
        pc = pc-anwer-1
        
        
        
        
        

       
        
        # print(address)
        # pc=pc-int(str(abs((inst-address))),16)/4
        
        opcode = bin_instruction[:6]

        nameOfOpcode = opcode_of_commands[opcode]
        # funct = format(funct,"02x")
        # print(funct)
        # print(f'opcode : {bin_instruction[:6]}')
        # print(f"rs = {rs} rt = {rt} rd = {rd} shamt = {shamt} funct = {funct}")
        # print(f"Instruction = {funct} ${rd},${rs},${rt}")
        # if(funct == "100000"):
        #     result = mips_registers[rs] + mips_registers[rt]
        # elif(funct == "100010"):
        #     result = mips_registers[rs] - mips_registers[rt]
        # elif(funct == "100100"):
        #     result = mips_registers[rs] & mips_registers[rt]
        # elif(funct == "100101"):
        #     result = mips_registers[rs] | mips_registers[rt]
        # #xor
        # elif(funct == "100110"):
        #     result = mips_registers[rs] ^ mips_registers[rt]
            
        # print(f"result = {result}")  
        # print(rd,type(rd))
    else:
        print("I type instruction",file=answer_file_output)
        # print(bin_instruction[:6])
        opcode = format(int(bin_instruction[:6], 2), "06b")
        # print(f'opcode : {bin_instruction[:6]}')
        rs = format(int(bin_instruction[6:11], 2), "05b")
        rt = format(int(bin_instruction[11:16], 2), "05b")
        immediate = int(bin_instruction[16:32], 2)
        
        if immediate == 65535:
            immediate = -1
        if immediate == 65533:
            immediate = -3
        if immediate == 65532:
            immediate = -4
        # print(f"rs = {mips_registers[rs]} rt = {mips_registers[rt]} immediate = {immediate}")
        nameOfOpcode = opcode_of_commands[opcode]
        print(nameOfOpcode,file=answer_file_output)
        if nameOfOpcode == 'lw':
            mips_registers_values[mips_registers[rt]] = instruction_dictionary_sorting[mips_registers_values[mips_registers[rs]]] + immediate
            # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rt]]}")
        if nameOfOpcode == 'lui':
            mips_registers_values[mips_registers[rt]] = immediate << 16
            # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rt]]}")
        if nameOfOpcode == 'ori':
            mips_registers_values[mips_registers[rt]] = mips_registers_values[mips_registers[rs]] | immediate
            # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rt]]}")
        if nameOfOpcode == 'bne':
            if mips_registers_values[mips_registers[rs]] != mips_registers_values[mips_registers[rt]]:
                string_immediate = bin_instruction[16:32]
                inverted_string = ''.join(['1' if bit == '0' else '0' for bit in string_immediate])
                #WE REVERSED THE DICTIONARY OVER HERE 
                
                pc = pc - int(inverted_string, 2) - 1
                # print(inverted_string)
        if nameOfOpcode == "beq":
            if mips_registers_values[mips_registers[rs]] == mips_registers_values[mips_registers[rt]]:
                string_immediate = bin_instruction[16:32]
                inverted_string = ''.join(['1' if bit == '0' else '0' for bit in string_immediate])
                if int(string_immediate,2)>100:
                    pc = pc-int(inverted_string,2)-1
                else:
                    pc = pc+int(string_immediate,2)
                # print(inverted_string)
                # pc = pc - int(inverted_string, 2) - 1
        if nameOfOpcode == "sw":
            address = mips_registers_values[mips_registers[rs]] + immediate
            print(address,file=answer_file_output)
            instruction_dictionary_sorting[address] = mips_registers_values[mips_registers[rt]]
            print(instruction_dictionary_sorting[address],file=answer_file_output)

#CONSIDERING DIFFERENT CASES 
#HERE THE OPERATIONS PERFORMED WILL BE DIFFERENT BASED ON THE ALU/EXE STAGE 
#WHAT EVER MAY BE THE TYPE OF INSTRUCTION WE ARE PERFORMING THE OPERATIONS BASED ON THE GIVEN TYPE OF THE GIVEN INSTRUCTION'S TYPE


        if nameOfOpcode == "addi":
            mips_registers_values[mips_registers[rt]] = mips_registers_values[mips_registers[rs]] + immediate
            # return mips_registers_values[mips_registers[rs]] + immediate

            # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rt]]}")

    # clk += 1
    print(f"CLOCK : {clk}",file=answer_file_output)
    print('-----X-----',file=answer_file_output)



#-----------------------------------------------------------------------

def mem_stage_instruction(instructions_used):
    # print("MEM",instructions_used)
    global clk
    clk+=1
    # value = exe_stage(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
    # global pc
    # opcode = format(int(bin_instruction[:6], 2), "06b")
    # nameOfOpcode = opcode_of_commands[opcode]
    # if nameOfOpcode == 'bne':
    #     string_immediate = bin_instruction[16:32]
    #     inverted_string = ''.join(['1' if bit == '0' else '0' for bit in string_immediate])
    #     pc = pc + int(inverted_string, 2) + 1
    rs = format(int(bin_instruction[6:11], 2), "05b")
    rt = format(int(bin_instruction[11:16], 2), "05b")
    immediate = int(bin_instruction[16:32], 2)
    rd = bin_instruction[16:21]
    shamt = int(bin_instruction[21:26], 2)
    funct = bin_instruction[26:32]
    print("MEM Stage",file=answer_file_output)
    print(mips_registers[rs],file=answer_file_output)
    print(f'CLOCK : {clk}',file=answer_file_output)
    print('-----X-----',file=answer_file_output)





def write_back(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk):
    # value = exe_stage(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
    # global pc
    # opcode = format(int(bin_instruction[:6], 2), "06b")
    # nameOfOpcode = opcode_of_commands[opcode]
    # if nameOfOpcode == 'bne':
    #     string_immediate = bin_instruction[16:32]
    #     inverted_string = ''.join(['1' if bit == '0' else '0' for bit in string_immediate])
    #     pc = pc + int(inverted_string, 2) + 1
    rs = format(int(bin_instruction[6:11], 2), "05b")
    rt = format(int(bin_instruction[11:16], 2), "05b")
    immediate = int(bin_instruction[16:32], 2)
    
    #print(immediate)
    rd = bin_instruction[16:21]
    shamt = int(bin_instruction[21:26], 2)
    funct = bin_instruction[26:32]
    # if(value is not None):
    #     mips_registers_values[mips_registers[rs]] = value
    print(mips_registers[rs],":",mips_registers_values[mips_registers[rs]],file=answer_file_output)
    # clk+=1
    print(f"CLOCK : {clk}",file=answer_file_output)
    print('-----X-----',file=answer_file_output)
    
#-------------------------------------------------------------------------




    
    #CONSIDERING THE CASE OF THE FACTORIAL 
    
while (pc < len(instruction_memory) and a==1):
    
    #IF phase 
    if(a==1):
        clk+=1
        if_stage(instruction_memory,clk)
   
    # print("IF Stage")
    # instruction = instruction_memory[pc]
    # inst = format((0x40000000+(pc*4)),"08x")
    # print("Instruction address: "+"0x"+inst)
    
    # print("Instruction Binary Code: "+format(instruction,"032b")) 
    # clk+=1
    
    # print(f"CLOCK : {clk}")   
    # print(pc) 
        clk+=1
        id_phase(instruction_memory, mips_registers, opcode_of_commands,clk)
    # print(pc)
        clk+=1
        exe_stage(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
        if(a==1):
            clk+=1
            print("MEM Stage",file=answer_file_output)
            print("Nothing is being stored",file=answer_file_output)
            print(bin_instruction,file=answer_file_output)
            # clk += 1
            print(f"CLOCK : {clk}",file=answer_file_output)
            print('-----X-----',file=answer_file_output)
    # print(pc)
        print("Write Back Stage",file=answer_file_output)
        clk+=1
        write_back(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
    # print(pc)
        pc+=1
        print(f"\n",file=answer_file_output)
        print("-----------------------------------------------------------------",file=answer_file_output)
        print("\n",file=answer_file_output)
        print("\n",file=answer_file_output)
        print(mips_registers_values['$t1'],file=answer_file_output)


if(a==1):
    print("\n",file=answer_file_output)
    print("\n",file=answer_file_output)
    print(mips_registers_values,file=answer_file_output)



#CONSIDERING THE CASE OF THE SORTING WHEN SORTING IS GIVEN TO US AS INPUT


while(pc<len(instruction_memory_sorting) and a==2): 
    # if_stage(instruction_memory_sorting,clk1)
    if(a==2):
        clk+=1
        if_stage(instruction_memory_sorting,clk)
   
    # print("IF Stage")
    # instruction = instruction_memory[pc]
    # inst = format((0x40000000+(pc*4)),"08x")
    # print("Instruction address: "+"0x"+inst)
    
    # print("Instruction Binary Code: "+format(instruction,"032b")) 
    # clk+=1
    
    # print(f"CLOCK : {clk}")   
    # print(pc) 
        clk+=1
        id_phase(instruction_memory_sorting, mips_registers, opcode_of_commands,clk)
    # print(pc)
        clk+=1
        exe_stage(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
        if(a==1):
            clk+=1
            print("MEM Stage",file=answer_file_output)
            print("Nothing is being stored",file=answer_file_output)
            print(bin_instruction,file=answer_file_output)
            # clk += 1
            print(f"CLOCK : {clk}",file=answer_file_output)
            print('-----X-----',file=answer_file_output)
        mem_stage_instruction(instruction_memory_sorting)
    # print(pc)
        print("Write Back Stage",file=answer_file_output)
        clk+=1
        write_back(bin_instruction, mips_registers, mips_registers_values, opcode_of_commands, clk)
    # print(pc)
        pc+=1
        print(f"\n",file=answer_file_output)
        print("-----------------------------------------------------------------",file=answer_file_output)
        print(mips_registers_values['$t1'],file=answer_file_output)
        print(instruction_dictionary_sorting,file=answer_file_output)
        print("\n",file=answer_file_output)
        print("\n",file=answer_file_output)
    


#HEMANG SETH IMT2022098
#RUTUL PATEL IMT2022021
