######################################
# programming assignment 0100
# Endi Troqe
# 11-19-2024
######################################
import random
import math

#main memory class
class MainMem:


    #initializes the main memory and physical memory
    def __init__(self, frames):
        #Stores the locations of the page frames in the physical memory
        self.mainMem = []
        self.frames = frames
        #The physical memory will store (hits+misses)
        self.physicalMem = [None] * (frames)

    def display(self):
        return "".join(self.mainMem)

class PageTable:

    #Initializes the page table with None in every page
    def __init__(self, pages, mainMem):
        self.pageTable = {page: None for page in range(pages)}
        self.mainMem = mainMem

    #calculates the miss ratio and appends the frames to the main memory
    def display(self, hits, misses):
        missRatio = (misses / (hits+misses)) * 100
        #replaces none for '-'
        frames = [str(value) if value is not None else '-' for value in self.pageTable.values()]

        #replaces the replaced frames with '-'
        for i,x in enumerate(frames):
            y = len(frames)-1
            if x != '-':
                while y > i:
                    if frames[y] == x:
                        frames[i] = '-'
                        break
                    y-=1
        
        self.mainMem.mainMem.append(f"{' '.join(frames)}\n")
        return f"{missRatio:.3f}%"

    #checks to see if physical memory is full
    def full(self):
        return None not in self.mainMem.physicalMem

#cpu class
class CPU:
    
    #initilizes the page table and hits and misses to 0
    def __init__(self, pageTable):
        self.pageTable = pageTable
        self.hits = 0
        self.misses = 0

    #executes a instruction
    def instruction(self, address):
        physicalMem = self.pageTable.mainMem.physicalMem

        #hit if address already in
        if address in physicalMem:
            self.hits += 1
        # if physical mem is full its going to be a miss. Replaces a random frame with new page
        elif self.pageTable.full():
            randValue = random.randint(0, self.pageTable.mainMem.frames - 1)
            if self.pageTable.pageTable[address] == None:
                self.pageTable.pageTable[address] = randValue
            else:

                #if randvalue is already present in dict
                self.pageTable.pageTable[address] = randValue            
            
            physicalMem[randValue] = address
            self.misses += 1

        #if there is room in physical memory finds the empty frame and inserts the page
        else:
            for i, x in enumerate(physicalMem):
                if x is None:
                    physicalMem[i] = address
                    self.pageTable.pageTable[address] = i
                    self.misses += 1
                    break

input_file = "input.txt"
newCommand = None
pageTable = None
mainMem = None


#opens the input file and the output file
with open(input_file, "r+") as r, open("100output.txt", "a") as f:

    #writes NEW at the end of the input file so that the program knows to display whats in the MM
    r.write("NEW")
    for i, x in enumerate(r):
        x = x.strip()

        #gets the offset bits, main mem sie, and vm size based on the line
        if i == 0:
            offBits = math.log(int(x), 2)
        elif i == 1:
            mm_size = int(x)
            mainMem = MainMem(mm_size)
            cpu = CPU(None)  # Initialize CPU once
        elif x == "NEW":
            newCommand = i + 1
            
            #displays what is in the main mem and what is the miss ratio
            if pageTable is not None:
                f.write(f"{pageTable.display(cpu.hits, cpu.misses)} ")
                f.write(f"{mainMem.display()}")
            #if instructions havent started yet write 0%
            else:
                f.write(f" 0.000%")

        # if it is a new command create new page table
        elif i == newCommand:
            vm_size = int(x)
            pageTable = PageTable(vm_size, mainMem)
            cpu.pageTable = pageTable 

            #write the amount of pages in new table
            f.write(f"\t{'- ' * vm_size}\n")

        #if its a instruction send it to CPU class
        else:
            x = x[:-int(offBits)]
            cpu.instruction(int(x, 2))



