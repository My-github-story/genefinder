Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # !pip install biopython
... 
... from Bio.Seq import Seq
... 
... def find_orfs(sequence):
...     orfs = set()
...     seq_len = len(sequence)
... 
...     for strand, seq in [(+1, sequence), (-1, sequence.reverse_complement())]:
...         for frame in range(3):
...             for start in range(frame, seq_len, 3):
...                 if seq[start:start+3] == 'ATG':
...                     for end in range(start + 3, seq_len, 3):
...                         if seq[end:end+3] in ['TAA', 'TAG', 'TGA']:
...                             orf = seq[start:end]
...                             protein = str(orf.translate(to_stop=True))
...                             if len(protein) > 0:
...                                 orfs.add(protein)
...                             break
...     return list(orfs)
... 
... input_string = """
... >>Rosalind_6613
... TTGCGCTCTCTATGTTTTGTGGCGGATCAGTACGGCATTCTCATGACAGTAAACGTTGCA
... AATACGGCTGGAGGACACCCCTGCGAAACCGGCATGGACCACTACGTTCCAAACGTAGTG
... TACAGGACGGAATCTAGCATCCTCACGCGAGAGCCACTTCACTTCTAGCACGTGGAGCGA
... TAGGAGACGCTACCAGGAGTCGGTTGATTTCCACATGTGCAACGTGTTCTATCGCTTATT
... GAAGGTGCGTTGGTGGTAAATTTGCCTCTGAAAGCAGATGGGATACGACACCCGCCTGGG
... CAATTGCTAAAGCATAGTTCGTTAAGATGGGCCATACGTTACAATGCGTGGTTAGTAACT
... AACGCAAGGACCCCACACATGAGAAGGCGCAATACTGTAAAGTAGGCGAATGTATCAGTC
... TCAAGAATAGCTATTCTTGAGACTGATACATGATGACTGGTAACGCACGCAGCCGATGGT
... ATTCCAACTTGCGTTAAGGGCTTGTGTGGATTCAGACCCGATTAAGCTCTCCTTGTATCG
... ATACTCTAGGCTCCTCCATTGACTGTTTTAAAAGCGGACAGGGAAAAAGGTATACGCTAT
... GCTGGGATCATACGGGCACTAGCTACCATGTGTTTGATGTCAGGCACTACGGCTTCATAC
... AGAGTGGAATACCCCCTCTATCTAGAAATGCTATGTTGTCGGACGTTAGCTGCTCTTTAA
... TGTGTAATTTCCTAATGATTAGCATGCAGTAAAGAGACCGTTCTTTGGACGTTGTATAAG
... ACTGAATTCTTACATGTGACGTCAGATGCCTATCTGAGTCCAGTCTATTGACGCTACCCA
... GAGTTCCAACCGGGTAGGAT
... """
... 
... lines = input_string.strip().split('\n')
... sequence = Seq(''.join(lines[1:]))
... 
... proteins = find_orfs(sequence)
... for protein in proteins:
