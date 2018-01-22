#!/usr/bin/env python3
from fileman import fstreams


for fin, fout in fstreams():
    data = {}
    for pair in fin:
        ngram, count = pair.split()
        count = int(count)
        size = len(ngram.strip('_').split('_'))

        if size in data:
            data[size] += count
        else:
            data[size] = count

    for size, count in data.items():
        fout.write("{} {}\n".format(size, count))
