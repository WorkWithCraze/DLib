# Generate Random RNA Strand


#given n, this function genrates the random DNA strand of length n


# import random library
import random
  
# function to generate dna strands
def generate_random_dna_strand(n):
    
    # list l created and in that stored all the types of nucleotides present in DNA
    # 'A' -> Adenine
    # 'C' -> Cytosine
    # 'G' -> Guanine
    # 'U' -> Uracil
    l = ['C', 'A', 'G', 'U']
    
    # string res created to store the random strand created
    res = ""
    for i in range(0, n):
        # creating the DNA strand by appending random characters from the list
        res = res + random.choice(l)
    return res


# Testing
# assuming n
n = 50

# calling the generate_random_dna_strand(n), to print the random strand
generate_random_dna_strand(n)

# Code contributed by, Abhishek Sharma,2021 @abhisheks008 #LGMSOC21
