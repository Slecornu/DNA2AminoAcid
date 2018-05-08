def main():
    dna = input(">Enter DNA:\n")
    print("\n")
    dna = dna.upper()   #makes sure the dna string is upper case
    if validDNA(dna):    #if dna validation returns true   
        inT = []    #input table
        inT = translate(dna)    #inT contains a list of integers used to
        i = 0
        while i < 3:    #this loop generates the first three frames
            calculate(i, inT, False)    #i is used for the level of indentation, inT array is used to find values in codon table, boolean dictates which side of the bond
            i = i + 1
        print (dna)    #print dna
        bondStr="|----:----"
        bondSize = len(dna) / len(bondStr)        #from here to line 24 calculates the length of the dna bond
        bondRemainder= len(dna) % len(bondStr)
        bond=''
        j = 1
        while j <= bondSize:
            bond += bondStr
            j = j + 1
        n = 0
        while n < bondRemainder:
            bond += bondStr[n]
            n=n+1
        print (bond)  #prints dna bond
        k = 0
        strand = ""
        while k < len(dna):
            strand += (getStrand(dna[k]))
            k = k + 1
        print (strand)    
        m = 0
        while m < 3:
            calculate(m, inT, True)
            m = m + 1
    print("\n")
    main()       
#validDNA checks to see if the dna is valid,
#it returns true if the dna passes validation, otherwise return false and prints the dna errors to the console
def validDNA(dna):
    i = 0
    validDNA = True;#aassuming dna is valid
    if(dna == ""):
        print("DNA string is null, please enter a valid DNA string. \n")
        validDNA = False
    while i < len(dna):   
        if (dna[i] != 'A') and (dna[i] != 'C') and (dna[i] != 'G') and (dna[i] != 'T'):#if not any dna chars
            print ("Invalid DNA, contains " + dna[i] + " at position: " + str(i) + ".")#then print error report
            validDNA = False#dna is not valid 
        i = i + 1
    return validDNA
            
 #translates the dna to a list of integers, the returned list is used to look up values in the 3d codon table     
def translate(dna):
    result = []
    for i in range(len(dna)): # for each char in dna string 
        result.append(getNumber(dna[i]))#translates the char to it's codon table number and appends to result array
    return result #returns an array of numbers

#getNumber returns a number in relation to the value of parameter n
#this number is used to look up values in the 3d codon table array
def getNumber(n):
    if n == 'A':
        return 0
    elif n == 'C':
        return 1
    elif n == 'G':
        return 2
    else:           #must be T
        return 3

#getStrand returns n's dna bond char, to generate the second dna strand
def getStrand(n):
    if n == 'A':
        return 'T'
    elif n == 'C':
        return 'G'
    elif n == 'G':
        return 'C'
    else:           #must be T
        return 'A'

#calculate returns an amino acid string and frame number, in corispondance to the parameters given
def calculate(i, inT, toFlip):
    frameNum = 0    #stores which numer frame is currently being proccessed
    if toFlip:     #if flip is true then the frame number = (3-i)+3 
        frameNum = 6 - i    
    else:           #otherwise the frame number will be 3-i
        frameNum = 3 - i  
    space = 0
    while space < i:    #a loop for printing space charecters to line up the resulting string with the other frames
        print (" ", end="")
        space = space + 1
    result = ""#stores the resulmting frame to be printed
    table = [   #the codon table is stored in a 3d array
            [
                    ["LYS", "ASN","LYS", "ASN"],
                    ["THR", "THR","THR", "THR"],
                    ["ARG", "SER","ARG", "SER"],
                    ["ILE", "ILE","MET", "ILE"]
                ],
                [
                    ["GLN", "HIS","GLN", "HIS"],
                    ["PRO", "PRO","PRO", "PRO"],
                    ["ARG", "ARG","ARG", "ARG"],
                    ["LEU", "LEU","LEU", "LEU"]
                ],
                [
                    ["GLU", "ASP","GLU", "ASP"],
                    ["ALA", "ALA","ALA", "ALA"],
                    ["GLY", "GLY","GLY", "GLY"],
                    ["VAL", "VAL","VAL", "VAL"]
                ],
                [
                    ["***", "TYR","***", "TYR"],
                    ["SER", "SER","SER", "SER"],
                    ["***", "CYS","TRP", "CYS"],
                    ["LEU", "PHE","LEU", "PHE"]
                ]
            ]
    
    while i < (len(inT)-2): #the loop itarates over every 3 charecters in the input table if there are 3 charecters remaning and translates them using the codon table
        a = inT[i]  #stores the 3 charecters
        b = inT[i+1]
        c = inT[i+2]
        if toFlip:
            a = flip(a)
            b = flip(b)
            c = flip(c)
            result = result + table[c][b][a]    #uses the resulting integers as coadinates for the 3d array and appends them to the resulting frame
        else:
            result = result + table[a][b][c]

        i = i + 3
    if len(result) <=0:
        print("empty    F" + str(frameNum)) #prints the resulting frame and frame number
    else:
        print(result + "    F" + str(frameNum)) #prints the resulting frame and frame number

def flip(num):  #he flip function finds the reverse for a charechter in the input table
    if num == 0:
        return 3
    elif num == 1:
        return 2
    elif num == 2:
        return 1
    else:
        return 0

    
if __name__ == '__main__':
    main() 




