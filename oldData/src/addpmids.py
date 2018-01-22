#!/usr/bin/env python3
from fileman import fstreams, argv


for fin, fout in fstreams():
    with open(argv[3]) as pmids:
        for pmid, document in zip(pmids, fin):
            fout.write(" ".join([pmid, document]))
