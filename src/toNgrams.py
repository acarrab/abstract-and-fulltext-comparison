#!/usr/bin/python3
from sys import exit, argv

if len(argv) < 3: exit("args: <inputFileName> <outputFileName>")

with open(argv[1]) as fin, open(argv[2], 'w') as fout:
    for document in fin:
        fout.write(" ".join(["_".join(n_gram.split()) for n_gram in document.split(',')[1:]]) + "\n")
