#!/usr/bin/env python3

from webbrowser import get
import jinja2
import mysql.connector

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('database.html')
print("Content-Type: text/html\n\n")


pw = open('pw.txt').read()
password = pw.rstrip()

conn = mysql.connector.connect(user='mjone286', password=password, host='localhost', database='mjone286')
curs = conn.cursor()
qry = "SELECT * from Prot"
curs.execute(qry)
result = list()
for EntryID,Seq_ID,Length,Weight,pI,Hydrophobicity,Instability_index,A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y in curs:
    result.append({'EntryID':EntryID,'Seq_ID':Seq_ID,'Length':Length,'Weight':Weight,
                   'pI':pI,'Hydrophobicity':Hydrophobicity,'Instability_index':Instability_index,'A':A,
                   'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'K':K,'L':L,'M':M,'N':N,'P':P,
                   'Q':Q,'R':R,'S':S,'T':T,'V':V,'W':W,'Y':Y})
conn.commit()
curs.close()
conn.close()

print("Content-Type: text/html\n\n")
print(template.render(result=result))
