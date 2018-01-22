#!/usr/bin/env python3
from fileman import fstreams

for fin, fout in fstreams():
    ngrams = {}
    for document in fin:
        for ngram in document.split():
            if not ngram in ngrams:
                ngrams[ngram] = 1
            else:
                ngrams[ngram] += 1

    fout.write('\n'.join([
        "{} {}".format(ngram, count)
        for ngram, count in ngrams.items()
    ]))
