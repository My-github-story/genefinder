#For this problem, I was tasked with processing a genome sequence stored in a FASTA file. 
#Specifically, I needed to write a tool that could identify gene-like regions 
#by searching for open reading frames (ORFs), marked by the 'ATG' 
#start codon and stop codons ('TAA', 'TAG', 'TGA'). The tool had to consider three reading frames, 
#excluding reverse complements. I sought help in clarifying the approach to reading the FASTA file, 
#identifying the regions between the start and stop codons, and efficiently handling command-line inputs. 
#The guidance I received greatly helped me structure my solution.

import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_orfs(sequence):
    orfs = []
    seq_len = len(sequence)
    
    for frame in range(3):
        for start in range(frame, seq_len, 3):
            codon = sequence[start:start+3]
            if codon == 'ATG':
                for end in range(start + 3, seq_len, 3):
                    stop_codon = sequence[end:end+3]
                    if stop_codon in ['TAA', 'TAG', 'TGA']:
                        orf = sequence[start:end+3]
                        orfs.append((start, end+3, orf))
                        break
    return orfs

def main(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = str(record.seq)
        orfs = find_orfs(sequence)
        
        for start, end, orf in orfs:
            print(f">ORF_{start}_{end}")
            print(orf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file")
    parser.add_argument("input_file", help="Input FASTA file")
    args = parser.parse_args()
    
    main(args.input_file)
