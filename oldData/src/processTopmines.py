#!/usr/bin/env python3
from fileman import fstreams

for fin, fout in fstreams():
    for document in fin:
        fout.write(" ".join(["_".join(n_gram.split()) for n_gram in document.split(',')[1:]]) + "\n")
