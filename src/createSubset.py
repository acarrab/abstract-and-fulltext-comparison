#!/usr/bin/env python3
import sys
if len(sys.argv) < 4:
    sys.exit("Correct usage: python3 ./createSubset.py <pmcids_subset> <in_file> <out_file>")

pmids = set()

with open(sys.argv[1]) as pmidFile:
    for pmid in pmidFile:
        pmids.add(pmid.split()[0])

print (len(pmids))

with open(sys.argv[2]) as fin:
    with open(sys.argv[3], 'w') as fout:
        for document in fin:
            if document.split()[0] in pmids:
                fout.write(document)
