import sys

if len(sys.argv) < 6:
    sys.exit("args: <topPhrases.txt 1> <topPhrases.txt 2> <inFirst.out> <inSecond.out> <inBoth.out>")

inclusions = {}

def getNgram(ngramAndCount):
    return " ".join(ngramAndCount.split()[:-1])

with open(sys.argv[1]) as file1:
    for document in file1:
        for ngram in document.split():
            inclusions[ngram] = 1

with open(sys.argv[2]) as file2:
    for document in file2:
        for ngram in document.split():
            if not ngram in inclusions:
                inclusions[ngram] = 2
            elif inclusions[ngram] == 1:
                inclusions[ngram] = 3


with open(sys.argv[3], 'w') as inFirst, open(sys.argv[4], 'w') as inSecond, open(sys.argv[5], 'w') as inBoth:
    for (ngram, val) in inclusions.items():
        if val == 1: inFirst.write(ngram + '\n')
        if val == 2: inSecond.write(ngram + '\n')
        if val == 3: inBoth.write(ngram + '\n')
