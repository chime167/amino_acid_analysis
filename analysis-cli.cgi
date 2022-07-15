#!/usr/bin/env python3

import re
import pandas as pd
from Bio.SeqUtils.ProtParam import ProteinAnalysis

print("Content-Type: application/json\n\n")
q = input('Enter name of your FASTA file (or absolute path if it is not in this directory: ')
raw_data = []
result = []

# turns query into newline separated list
for line in open(q):
    line = line.rstrip()
    # regex to match FASTA header
    m = re.match('>(\S+)\s+(.+)', line)
    if m:
        dic = {'header': m.group(1), 'sequence': None}
	# resets the seq variable each iteration
        seq = ''
        raw_data.append(dic)
    else:
	# any nonheader line is sequence
        seq += line
        dic['sequence'] = seq

# turns dict values into their own lists
prot_data = [sub['sequence'] for sub in raw_data]
n = [sub['header'] for sub in raw_data]

# employing the biopython module to fetch data about each entry
for seq, id in zip(prot_data, n):
    ambiguous = seq.count('X')
    seq = seq.replace('X', '')
    analyzed_seq = ProteinAnalysis(seq)
    length = len(seq)
    weight = round(analyzed_seq.molecular_weight(), 1)
    pI = round(analyzed_seq.isoelectric_point() ,3)
    counts = analyzed_seq.count_amino_acids()
    hydrophobicity = round(analyzed_seq.gravy(), 3)
    instability = round(analyzed_seq.instability_index(), 2)
    dat = {'ID': id, 'Length': length, 'Weight': weight, 'pI': pI,
           'Hydrophobicity': hydrophobicity, 'Instability_index': instability}

    # appends amino acid count dict to the existing dict
    dat.update(counts)
    result.append(dat)  
    
print(pd.DataFrame(result))
