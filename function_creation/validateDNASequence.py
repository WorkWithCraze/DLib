
typesOfNucleotides =["A","C","G","T"]

def validateDNASequence(DNASequence):
      '''
            This function verifies whether the passed in sequence 
            is an DNA sequence or not . Returns False if not ,
            otherwise returns the original sequence .
      '''
      sequence=DNASequence.upper()
      for nuc in sequence:
            if nuc not in typesOfNucleotides:
                  return False
      return DNASequence
