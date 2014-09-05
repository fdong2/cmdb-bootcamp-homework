#!/usr/bin/env python
"""
From .fa of clout, finds 100 longest transcripts, open reading frames, and protein sequences
"""

import sys
import pandas as pd

#Functions used
#extracts ORFs
def extract(seq):
   # print "here"
    out = {}
    index = 0
    tr = 0
    for base in seq:
        if seq[index:index+3] in start:
            out[index] = ""
            for codon in thirds(seq[index:]):
                if codon in stop:
                    index += 1
                    break
                for acid, code in aa.iteritems():
                    if codon in code:
                        out[index] += acid
                        tr = 1
                if tr == 0:
                    out[index] += "X"
        index += 1
    return out
    
#iterates by three letters            
def thirds(ext):
    #print "entered"
    three = ""
    for base in ext:
        three += base
        if len(three) == 3:
            yield three
            three = ""
    return

#important variables
start = ["ATG", "TAC"]
stop = ["TAG", "TAA", "TGA", "ATC", "ATT", "ACT"]
aa = {"I": ["ATT", "ATC", "ATA"], "L": ["CTT", "CTC", "CTA", "CTG", "TTA", "TTG"], 
"V":["GTT", "GTC", "GTA", "GTG"], "F": ["TTT", "TTC"], "M":"ATG", "C":["TGT", "TGC"],
"A":["GCT", "GCC", "GCA", "GCG"], "G":["GGT", "GGC", "GGA", "GGG"], "P":['CCT', 'CCC', 
'CCA', 'CCG'], 'T':['ACT','ACC','ACA','ACG'], 'S':['TCT','TCC','TCA','TCG','AGT','AGC'],
'Y':['TAT','TAC'], 'W':'TGG', 'Q':['CAA','CAG'], 'N':['AAT','AAC'], 'H':['CAT','CAC'], 
'E':['GAA','GAG'], 'D':['GAT','GAC'], 'K':['AAA','AAG'], 'R':['CGT','CGC',
'CGA','CGG','AGA','AGG']}

#Exercise 1

#Accept input file and convert to string
file = sys.stdin.read()
lines = file.split("\n") #split string by lines

transcripts = {} #stores reference number and transcript
place = "" #working reference number 

for line in lines:
    if line.startswith( ">" ):
        place = line.split()[0][1:]
        transcripts[place] = ""
    else: 
        transcripts[place] += line
        
#Sorts transcripts and finds 100 longest
lengths = [] #stores transcript 
for ref, seq in transcripts.iteritems():
    lengths.append((ref, len(seq)))
lengths.sort(reverse = True, key = lambda tup: tup[1] )
toplen = lengths[:100] #100 longest transcripts reference numbers
top100 = {}
for ref, long in toplen: # gets 100 longest transcripts
    top100[ref] = transcripts[ref]
    
#Print 100 longest transcripts
top100f = open("top100.fa", "w")
for ref, seq in top100.iteritems():
    top100f.write(">"+ref+"\n")
    s = seq
    while len(s) > 0:
        top100f.write(s[:61] + "\n")
        s = s[61:]
        

#Makes complements of transcripts
conversion = {"A":"T", "T":"A", "G":"C", "C":"G", "N":"N" }
top_c100 = {}
for ref, seq in top100.iteritems():
    top_c100[ref] = ""
    for base in seq:
        top_c100[ref] += base.replace(base, conversion[base])

vertical = ["ref", "protein"]

#Exercise 2
#Find ORFs
transcript_f = [] #reference number, with tuples stating index and amino acid sequence
for ref, seq in top100.iteritems(): 
    #print seq
    x = extract(seq)
    if x != {}:
        transcript_f.append((ref, x))
f = pd.DataFrame(transcript_f, columns = vertical)

transcript_r = []
for ref, seq in top100.iteritems(): 
    x = extract(seq[::-1])
    if x != {}:
        transcript_r.append((ref, x))
r = pd.DataFrame(transcript_r, columns = vertical)

transcript_c_f = [] #complement
for ref, seq in top_c100.iteritems(): 
    x = extract(seq)
    if x != {}:
        transcript_c_f.append((ref, x))
cf = pd.DataFrame(transcript_c_f, columns = vertical)

transcript_c_r = []
for ref, seq in top_c100.iteritems(): 
    x = extract(seq[::-1])
    if x != {}:
        transcript_c_r.append((ref, x))
cr = pd.DataFrame(transcript_c_r, columns = vertical)




print f