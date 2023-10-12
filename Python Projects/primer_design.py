"""
Question:
Given is a gene sequence. The task is to determine the number of primer sequences possible
from the given gene sequence.
How to find primers?
A primer is a 20 nucleotide long sequence that obeys the following conditions:
1. The GC content of the primer should be 40-60%.
2. The melting temperature should be between 52-56 degrees celcius (Tm = 4(G+C) + 2(A+T))
"""

# This is a function that takes the gene sequence as the input and returns 
# all possible primers satisfying the conditions.
def primer_design(seq = "ATGGCAATCAAGTCATTGGAATCGTTCCTTTTCGAAAGAGGTCTAGTAGG"):
    # First, I will create another list gc_count which will already have
    # a starting element 0.
    gc_count = [0]
    # counter is to keep track of number of 'G' or 'C' bases.
    counter = 0
    # Now, I will iterate through the "seq" received as input. On finding the 
    # 'G' or 'C' bases, counter is incremented and appended to gc_count.
    for i in range(len(seq)):
        if(seq[i] == "G" or seq[i] == "C"):
            counter += 1
        gc_count.append(counter)
    
    # So, essentially, gc_count at an index 'i+1' will have the number of 
    # 'G' or 'C' bases found until the 'i'th position on the seq. 
    
    # So, if I want to find the number of 'G', 'C' bases from 'i' to 'i+20' all I have to
    # do is find the difference between the values at gc_count[i+20+1] and gc_count[i]
    
    nucleotide = 20  #Given to create a 20 nucleotide primer
    valid_primers = []
    for i in range(1, len(gc_count)-(nucleotide-1)):
        gc = gc_count[i+nucleotide-1] - gc_count[i-1]
        # In order to accomplish the given conditions, the only condition that needs
        # to be satisfied is if(gc==8). Logic has been explained after the exit from this method.
        if(gc==8):
            valid_primers.append(seq[i-1:i+nucleotide-1])
    return valid_primers

  # Assuming that the given bounds are all inclusive,
  # The two conditions that need to be satisfied for the primer are:
  # a. The GC content of a primer should be 40-60%.
  #    So, let the 'G', 'C' count in a sequence of 20 bases be x.
  #    The condition says 0.4 <= x/20 <= 0.6. This implies that 8 <= x <= 12
  #    So, this condition says that x can belong in the range [8,12]

  # b. The melting temperature (Tm) should be between 52 to 56 degrees. Tm = 4(G+C)+2(A+T)
  #    So, let the 'G', 'C' count in a sequence of 20 bases be x.
  #    The condition says 52 <= 4(x)+2(20-x) <= 56. This implies that 52 <= 40 + 2x <= 56
  #    This implies that 12 <= 2x <= 16. This is equivalent to saying, 6 <= x <= 8
  #    So, this condition says that x can belong in the range [6,8]

  # Now, what we need is an intersection of the above two ranges.
  # Intersection of [6,8] and [8,12] is [8].
  # Hence the entire condition reduces to checking 'if(gc==8)'.

prime = primer_design()
for i in range(len(prime)):
    print(prime[i])