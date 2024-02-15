# import random
# import math
# import itertools


print("Enter 1 for Factorial and 2 For Sorting")
a=int(input())


#ENTERING THE CHOICE OF THE USER

mips_registers={"00000": "$zero", "00001": "$at", "00010": "$v0", "00011": "$v1", "00100": "$a0",
"00101": "$a1", "00110": "$a2", "00111": "$a3", "01000": "$t0", "01001": "$t1",
    "01010": "$t2", "01011": "$t3", "01100": "$t4", "01101": "$t5", "01110": "$t6",
    "01111": "$t7", "10000": "$s0", "10001": "$s1", "10010": "$s2", "10011": "$s3",
    "10100": "$s4", "10101": "$s5", "10110": "$s6", "10111": "$s7", "11000": "$t8",
    "11001": "$t9", "11101": "$sp", "11111": "$ra",
}
# print(mips_registers)
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
#list of all the instructions that have been used
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

# I type contains opcodes

Itype={
    0x04:"beq",
    0x23:"lw",
    0x2B:"sw",
    }

# j type contains opcodes

Jtype = {
    0x02:"j",
}

output = open("output_pipeline.txt", "w")


#this contains the instruction memory

instruction_memory= [
0x00000000,
0x20080005,
0x20090001,
0x200A0001,
0x71284802,
0x2108FFFF,
0x150AFFFD,
]
#THIS CONTAINS THE GIVEN INSTRUCTIONS FOR THE SORTING 

instruction_memory_sorting=[
0x00000000,
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
0x10000000,
0x11ccfff9,
0x8d710000,
0x216b0004,
0x8d720000,
0x21ce0001,
0x0232082a,
0x1420fff9,
0xad710000,
0xad72fffc,
0x1000fff6,
0x200c0000,

]

#THE ALLOCATED VALUES FOR THE DATA OF DICTIONARY SORTING 

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


#THESE ARE THE  REGISTERS THAT ARE USED IN THE MIPS REGISTERS

def id_phase(instruction_memory, mips_registers, opcode_of_commands,clk):
    global bin_instruction
    global pc
    global RegWrite
    global MemRead       #DECLARING THEE CONTROL SIGNALS IN THIS CASE 
    #THESE CONTROL SIGNALS WILL BE USED FOR THE ADDITIONAL VALUE AND COMPARISION

    instruction1 = instruction_memory[pc]
    bin_instruction = format(instruction1, "032b")
    
    
    #THIS IS THE ID STAGE WHICH IS USING THW CONSTROL INSTRUCTIONS 
    
    if(bin_instruction[:6]=="000000"):
        RegWrite=1
        MemRead=0
        
        
        
    if(bin_instruction[:6]=="001000"):
        RegWrite=1
        
        
        
    if(bin_instruction[:6]=="000100"):
        RegWrite=0
        MemRead=0
        
        #these are the control signal values
    
    if(bin_instruction[:6]=="000010"):
        RegWrite=0
        
    if(bin_instruction[:6]=="011100"):
        RegWrite=1
    
    if(bin_instruction[:6]=="100011"):
        RegWrite=1



#THEIR CONDITIONS AND THE RESPECTIVE VALUES OF THE PARAMTER'S MUXES

# clk1=0
# global pc1p8
# pc1=0

global clk
clk=0
global pc
pc=0
# xx=open("output.txt","w")
# def if_stage(instruction_memory, clk):
#     print("IF Stage")
#     # print(pc,file=xx)
#     instruction = instruction_memory[pc]
#     instructions_used = format((0x00400000 + (pc * 4)), "08x")
#     # if(instruction == 0x71284802):
#     #     print("Instruction Binary Code: 00000001001010010100000000000000")
#     #     mul_instruction = "00000001001010010100000000000000"
#     # else:
#     print("Instruction address: " + "0x" + instructions_used)
#     print("Instruction Binary Code: " + format(instruction, "032b"))
#     # clk += 1
#     print(f"CLOCK: {clk}")
#     print('-----X-----')




# def id_phase(instruction_memory, mips_registers, opcode_of_commands,clk):
# for i in range(15):
#     d[pc]=i
#     pc+=4
if a==2:
    instruction_memory = instruction_memory_sorting
    
    
def if_stage_instruction(pc):
    # print("IF",pc,d[pc])
    print("IF Stage",file=output)
    # print(pc,file=xx)
    instruction = instruction_memory[pc]
    instructions_used = format((0x00400000 + (pc * 4)), "08x")
    # if(instruction == 0x71284802):
    #     print("Instruction Binary Code: 00000001001010010100000000000000")
    #     mul_instruction = "00000001001010010100000000000000"
    # else:
    print("Instruction address: " + "0x" + instructions_used,file=output)
    print("Instruction Binary Code: " + format(instruction, "032b"),file=output)
    # clk += 1
    print(f"CLOCK: {clk}",file=output)
    #print(clk,file=output)
    print('-----X-----',file=output)

#THIS IS THE COMPARISION IF STAGE INSTRUCTION

def id_stage_instruction(inst1):
    global bin_instruction
    global pc
    #global clk
    print("ID phase",file=output)
    instruction1 = instruction_memory[pc]
    bin_instruction = format(instruction1, "032b")
    
    if bin_instruction[:6] == "011100" and RegWrite==1:
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21]
        #print(rs,rd)
        shamt = int(bin_instruction[21:26], 2)
        funct = bin_instruction[26:32]
        print(f'opcode : {bin_instruction[:6]}',file=output)
        print(f"rs = {mips_registers[rs]} rt = {mips_registers[rt]} rd = {mips_registers[rd]} shamt = {shamt} funct = {funct}",file=output)
        print(f"Instruction = mul {mips_registers[rd]},{mips_registers[rs]},{mips_registers[rt]}",file=output)
    
    elif bin_instruction[:6] == "000000" and RegWrite==1:
        print("R type instruction",file=output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        #print(rs)
        rd = bin_instruction[16:21]
        shamt = int(bin_instruction[21:26], 2)
        funct = bin_instruction[26:32]
        print(f'opcode : {bin_instruction[:6]}',file=output)
        print(f"rs = {mips_registers[rs]} rt = {mips_registers[rt]} rd = {mips_registers[rd]} shamt = {shamt} funct = {funct}",file=output)
        print(f"Instruction = {opcode_of_commands[funct]} {mips_registers[rd]},{mips_registers[rs]},{mips_registers[rt]}",file=output)
    
    elif bin_instruction[:6] == "000010" and RegWrite==0:
        print("J type instruction",file=output)
        #print(opcode_of_commands[bin_instruction[:6]])
        print(f'opcode : {bin_instruction[:6]}',file=output)
        address = int(bin_instruction[6:32], 2)
        print(f"address = {address}",file=output)
        # int initial = 0x40000000
        print(f"Instruction = {address}",file=output)
    
    else:
        print("I type instruction",file=output)
        opcode = bin_instruction[:6]
        print(f'opcode : {bin_instruction[:6]}',file=output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        #print(rt)
        immediate = int(bin_instruction[16:32],2)
        print(f"rs = {rs} rt = {rt} immediate = {immediate}",file=output)
        print(f"Instruction = {opcode_of_commands[opcode]} {mips_registers[rt]},{mips_registers[rs]},{immediate}",file=output)
        #print(instruction)
    # clk+=1
    print(f"CLOCK : {clk}",file=output)
    print('-----X-----',file=output)
    #print(pc)
    
#THIS IS THE ID STAGE INSTRUCTION     

def ex_stage_instruction(instructions_used):
    print("EX",instructions_used,file=output)

    print('EXE Stage',file=output)
    result = 0
    answer = 0
    global pc
    #THIS IS THE EXE STAGE INSTRUCTION
    stringtocheck = format(int(bin_instruction,2),"08x")

    # if(stringtocheck=="0x3c011001"):
    #     pc+=2
    #     rs = format(int(bin_instruction[6:11], 2), "05b")
    #     rt = format(int(bin_instruction[11:16], 2), "05b")
    #     immediate = int(bin_instruction[16:32], 2)
    #     mips_registers_values[mips_registers[rt]] = mips_registers_values[mips_registers[rs]] + immediate

        
    if bin_instruction[:6] == "011100":
        print("mul",file=output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        #print(rs)
        rd = bin_instruction[16:21]
        shamt = bin_instruction[21:26]
        funct = bin_instruction[26:32]
        # print(funct)
        mips_registers_values[mips_registers[rs]] = mips_registers_values[mips_registers[rt]] * mips_registers_values[mips_registers[rd]]
        # answer = mips_registers_values[mips_registers[rs]]
        # print(mips_registers_values[mips_registers[rs]])
        # print(mips_registers_values[mips_registers[rt]])
        # print(mips_registers_values[mips_registers[rd]])
        # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rs]]}")
    elif bin_instruction[:6] == "000000":
        print("R type instruction",file=output)
        rs = bin_instruction[6:11]
        rt = bin_instruction[11:16]
        rd = bin_instruction[16:21] #THIS IS THE DIFFERENT TYPEES OF INSTRUCTIONS THAT ARE USED 
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
    elif bin_instruction[:6] == "000010":
        print("J type instruction",file=output)
        # print(f'opcode : {bin_instruction[:6]}')
        print(bin_instruction[6:32],file=output)
        
        address = int("0000"+bin_instruction[6:32]+"00", 2)
        print(address,file=output)
      
        # print(f"address = {address}")
        # print(f"Instruction = {address}")s
        # instructions_used = format((0x40000000 + (pc * 4)), "08x")
        anwer=(pc*4)+4194304-address
        anwer//=4
        print(anwer,file=output)
        pc = pc-anwer-1
        
        
        
        
        

       
        
        # print(address)
        # pc=pc-int(str(abs((instructions_used-address))),16)/4
        
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
        print("I type instruction",file=output)
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
        print(nameOfOpcode,file=output)
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
                pc = pc - int(inverted_string, 2) - 1-1
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
            print(address,file=output)
            instruction_dictionary_sorting[address] = mips_registers_values[mips_registers[rt]]
            print(instruction_dictionary_sorting[address],file=output)

        if nameOfOpcode == "addi":
            mips_registers_values[mips_registers[rt]] = mips_registers_values[mips_registers[rs]] + immediate
            # return mips_registers_values[mips_registers[rs]] + immediate

            # print(f"{mips_registers[rt]}: {mips_registers_values[mips_registers[rt]]}")

    # clk += 1
    print(f"CLOCK : {clk}",file=output)
    print('-----X-----',file=output)
    
def mem_stage_instruction(instructions_used):
    # print("MEM",instructions_used)
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
    # if(value is not None):
    #     mips_registers_values[mips_registers[rs]] = value
    if(a==2):
        print(mips_registers[rs],":",mips_registers_values[mips_registers[rs]],file=output)
        print(instruction_dictionary_sorting,file=output)
    # clk+=1
    print(f"CLOCK : {clk}",file=output)
    print('-----X-----',file=output)

def wb_stage_instruction(instructions_used):
    # print("WB",instructions_used)
#THIS IS THE WRITE BACK INSTRUCTION


    print('MEM Stage',file=output)
    print('-----X-----',file=output)
    print(f"CLOCK : {clk}",file=output)
    # print(instruction_dictionary_sorting)



#HERE WE HAVE USED THE PIPELINE INSTRUCTIONS USED
#HERE WE HAVE USED THE CONCEPT OF OOPS to determine the instructioons used in the pipeline to help us use in the pipelinee 

class Pipeline_instructions_used:
    def __init__(self) -> None:
        self.list=[if_stage_instruction,id_stage_instruction,ex_stage_instruction,mem_stage_instruction,wb_stage_instruction]
        self.values_initialsed=[False, False, False, False, False]
        self.instructionsGet=None
        self.i=0
        #commparing the given values of list 
        
        #print(self.list)
        #for i in range(len(list)):
            #print(list[i])
        
        self.clock=clk
        self.pc=pc
        #print(self.pc)
        
        
        
        
    def run(self,pc=None):
        if self.i==0:
            self.instructionsGet=self.list[self.i](pc)
            #this is how we used the run instructionds
            
        else:
            self.list[self.i](self.instructionsGet)
            
            
        self.values_initialsed[self.i]=True
        self.i+=1
        
    def resetSelf(self):
        #this RESETS the given values of the pipeline and then sets it by the initialiased values
        self.values_initialsed = [False, False, False, False, False]
        # self.instructionsGet = None
        # self.i = 0
        self.clock = clk
        self.pc = pc

    def flush_pipeline(pipeline):
        for steps in pipelineprocessor:
            steps.resetSelf()
            #for flushing 
            #print(pipeline[i].values_initialsed)
        
class pipelineprocessor:
    # pc=0x400000
    # global pc
    
    def __init__(self):
        self.pipelineprocessor=[]
    
    def refresh(self):
        if self.pipelineprocessor and self.pipelineprocessor[-1].values_initialsed[-1]:
            self.pipelineprocessor.pop()
            #this is used for refreshing the PipeLine
            #print(self.pipelineprocessor)
            
            
    def append(self,instructions_used:Pipeline_instructions_used):
        self.refresh()
        #for appending the given Instructions
        if len(self.pipelineprocessor)<5:
            self.pipelineprocessor=[instructions_used]+self.pipelineprocessor
            

    def run(self):
        global clk
        #This will run and then check for the clock
        
        
        global pc
        while pc<len(instruction_memory)-1 or self.pipelineprocessor:
            self.refresh()
            instructionsGet=Pipeline_instructions_used()    
            print(f"The value of pc is {pc}",file=output)
            for i in self.pipelineprocessor[::-1]:
                i.run(pc)
            if pc<len(instruction_memory)-1:
                #FINAL RUN FUNCTIONN
                self.append(instructionsGet)
                self.pipelineprocessor[0].run(pc)
                # if pc < len(instruction_memory) - 1:
                # self.append(instructionsGet)
                # self.pipelineprocessor[0].run(pc)
            pc+=1
            clk+=1
            if(a==2): #considering the differnet cases....
                # print(mips_registers_values,file=output)
                print('--------------------------------------------------------------',file=output)
            elif(a==1):
                print("\n",file=output)
                print("\n",file=output)
                print(mips_registers_values['$t1'],file=output)
                print('--------------------------------------------------------------',file=output)

p=pipelineprocessor()
p.run()

if(a==1):
    print("\n",file=output)
    print(mips_registers_values,file=output)

#PRINTING THE FINAL OUTPUT BASED ON THE GIVEN CASE.....

if(a==2):
    print("\n",file=output)
    print(mips_registers_values,file=output)

#print(p.flush_pipeline())



# if(a==1):
#     print("\n",file=output)
#     print("\n",file=output)
#     print(mips_registers_values['$t1'],file=output)



#HEMANG SETH IMT2022098
#RUTUL PATEL IMT2022021