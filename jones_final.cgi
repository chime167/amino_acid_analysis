#!/usr/bin/env python3

import re
import cgi
import jinja2
import mysql.connector
import json
from Bio.SeqUtils.ProtParam import ProteinAnalysis

#templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
#env = jinja2.Environment(loader=templateLoader)
#template = env.get_template('temp2.html')
#print("Content-Type: text/html\n\n")
print("Content-Type: application/json\n\n")


pw = open('pw.txt').read()
password = pw.rstrip()
form = cgi.FieldStorage()
q = form.getvalue('query')
raw_data = list()
result = list()

#turns query into newline separated list
for line in q.splitlines():
    line = line.rstrip()
    #regex to match FASTA header
    m = re.match('>(\S+)\s+(.+)', line)
    if m:
        dic = {'header': m.group(1), 'sequence': None}
	#resets the seq variable each iteration
        seq = ''
        raw_data.append(dic)
    else:
	#any nonheader line is sequence
        seq += line
        dic['sequence'] = seq

#turns dict values into their own lists
prot_data = [sub['sequence'] for sub in raw_data]
n = [sub['header'] for sub in raw_data]

#employing the biopython module to fetch data about each entry
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

    #appends amino acid count dict to the existing dict
    dat.update(counts)
    result.append(dat)
    conn = mysql.connector.connect(user='mjone286', password=password, host='localhost', database='mjone286')
    curs = conn.cursor()
    
    #query to enter all data into database
    qry = """INSERT INTO Prot (Seq_ID, Length, Weight, pI, 
        Hydrophobicity, Instability_index, A, C, D, E, F, G, H, I, K, L, M, N,
        P, Q, R, S, T, V, W, Y) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    curs.execute(qry, (id, length, weight, pI, hydrophobicity, instability, counts['A'],
                       counts['C'], counts['D'], counts['E'], counts['F'], counts['G'], counts['H'],
                       counts['I'], counts['K'], counts['L'], counts['M'], counts['N'], counts['P'],
                       counts['Q'], counts['R'], counts['S'], counts['T'], counts['V'], counts['W'],
                       counts['Y']))
    conn.commit()
    curs.close()
    conn.close()    
    

#print(template.render(result=result))
print(json.dumps(result))

