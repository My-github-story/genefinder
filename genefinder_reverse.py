#I was assigned to extend the previous tool that identifies open reading frames (ORFs) 
#within a genome sequence stored in a FASTA file. The challenge involved searching for ORFs not 
#only in the original sequence but also in its reverse complement, which meant exploring all six 
#possible reading frames. While I was already familiar with generating reverse complements from an 
#earlier assignment, I needed clarification on how to integrate this into the tool and handle all the 
#frames efficiently. Additionally, I considered using BioPython for certain functionalities and sought guidance on that integration.

import argparse
from Bio import SeqIO
from Bio.Seq import Seq

def find_orfs(sequence):
    orfs = []
    seq_len = len(sequence)
    
    for strand, seq in [(+1, sequence), (-1, sequence.reverse_complement())]:
        for frame in range(3):
            for start in range(frame, seq_len, 3):
                if seq[start:start+3] == 'ATG':
                    for end in range(start + 3, seq_len, 3):
                        if seq[end:end+3] in ['TAA', 'TAG', 'TGA']:
                            orf = seq[start:end+3]
                            orfs.append((start, end+3, strand, orf))
                            break
    return orfs

def main(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        sequence = record.seq
        orfs = find_orfs(sequence)
        
        for start, end, strand, orf in orfs:
            strand_symbol = '+' if strand == 1 else '-'
            print(f">ORF_{start}_{end}_{strand_symbol}")
            print(orf)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find ORFs in a FASTA file")
    parser.add_argument("input_file", help="Input FASTA file")
    args = parser.parse_args()
    
    main(args.input_file)
