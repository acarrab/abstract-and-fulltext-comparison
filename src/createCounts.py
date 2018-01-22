import sys

if len(sys.argv) < 3:
    sys.exit("Usage: python3 createCounts.py <in_file> <out_file>")


ngramsAndCounts = {}
with open(sys.argv[1]) as fin:
    for document in fin:
        for ngram in document.split()[1:]:
            if not ngram in ngramsAndCounts:
                ngramsAndCounts[ngram] = 1
            else:
                ngramsAndCounts[ngram] += 1


with open(sys.argv[2], 'w') as fout:
    for (ngram, count) in ngramsAndCounts.items():
        fout.write("{} {}\n".format(ngram, count))
