#!/usr/bin/env python

import Bio
import Bio.Blast
import Bio.Blast.Applications
from Bio.Blast.Applications import NcbiblastpCommandline
from io import StringIO
from Bio.Blast import NCBIXML
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Create two sequence files

x1 = input("What is the first sequence? ")
x2 = input("What is the second sequence? ")
x3 = input("What is the third sequence? ")
x4 = input("What is the fourth sequence? ")
x5 = input("What is the fifth sequence? ")

sequences = [x1, x2, x3, x4, x5]

#seq1 = SeqRecord(Seq("FQTWEEFSRAAEKLYLADPMKVRVVLKYRHVDGNLCIKVTDDLVCLVYRTDQAQDVKKIEKF"),
#                   id="seq1")
#seq2 = SeqRecord(Seq("FQTWEEFSRAEKLYLADPMKVRVVLRYRHVDGNLCIKVTDDLICLVYRTDQAQDVKKIEKF"),
#                   id="seq2")
#SeqIO.write(seq1, "seq1.fasta", "fasta")
#SeqIO.write(seq2, "seq2.fasta", "fasta")

# Run BLAST and parse the output as XML
output = NcbiblastpCommandline(query="seq1.fasta", subject="seq2.fasta", outfmt=5)()[0]
blast_result_record = NCBIXML.read(StringIO(output))

# Print some information on the result

def find_match(a, b):

    # Record sequences and add them to a fasta file

    seq1 = SeqRecord(Seq(a), id = seq1)
    seq2 = SeqRecord(Seq(b), id = seq2)

    SeqIO.write(seq1, "seq1.fasta", "fasta")
    SeqIO.write(seq2, "seq2.fasta", "fasta")    

    # Run BLAST and create it as an XML

    output = NcbiblastpCommandline(query="seq1.fasta", subject="seq2.fasta", outfmt=5)()[0]
    blast_result_record = NCBIXML.read(StringIO(output))


    # Print out important things from this 

#    for alignment in blast_result_record.alignments:
#        for hsp in alignment.hsps:
#            print('****Alignment****')
#            print('sequence:', alignment.title)
#            print('length:', alignment.length)
#            print('e value:', hsp.expect)
#            print(hsp.query)
#            print(hsp.match)
#            print(hsp.sbjct)

# Create 2 lists to collect data

evals = []
names = []

# Create for loop

for i in range(5):
    for j in range(5):
        if(i != j & i > j):
            find_match(sequences(i-1),sequences(j-1))
            for alignment in blast_result_record.alignments:
                for hsp in alignment.hsps:
                    evals.extend(hsp.expect)
                    
                    s = "x" + i-1 + " and x" + j-1
                    names.extend(s)

# Check for the lowest e value comparison and rank

s1 = evals.sort()
print("The sorted e val list is ")
print(s1)

Z = [x for _, x in sorted(zip(evals, names))]
print("The corresponding names are ")
print(Z)
