#!/usr/bin/env python3
from fileManager import fstreams

for fin, fout in fstreams():
    sizeAndCount = {}
    for line in fin:
        ngram, count = line.split()
        size = len(ngram.strip('_').split('_'))
        if not size in sizeAndCount:
            sizeAndCount[size] = 1
        else:
            sizeAndCount[size] += 1

    fout.write('\n'.join([
        "{} {}".format(key, val)
        for key, val in sizeAndCount.items()
    ]))
