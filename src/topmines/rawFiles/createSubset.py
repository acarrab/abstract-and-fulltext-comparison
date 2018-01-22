from sys import argv, exit
from os.path import isfile
from subprocess import check_output
def run(c): return check_output(c, shell=True).decode()
def countLines(fileName): return int(run('wc -l '+fileName).split()[0])

if len(argv) < 3: exit('<pmids in thousands> <file to subset>')

fullPmidFile = 'pmids.data'

def subsetName(oldFile):
    newFile = oldFile.split('.')
    newFile[0] += '_' + argv[1]
    newFile = ".".join(newFile)
    return newFile

subsetPmids = subsetName(fullPmidFile)

def createSubset(size):
    print('creating subset called: ' + subsetPmids)
    n = countLines(fullPmidFile)
    k = size
    with open(fullPmidFile) as fin, open(subsetPmids, 'w') as fout:
        for line in fin:
            if 0 == random.randrange(0, int(float(n) / k)) or n == k:
                fout.write(line)
                k -= 1
                if k % 10000 == 0: print("written: " + str(rest - k))
                if k == 0: break
            # fi
            n -= 1

subsetSize = 1000 * int(argv[1])
if not isfile(subsetPmids) or countLines(subsetPmids) != subsetSize:
    createSubset(subsetSize)
else:
    print('subset file already exists')


inFile = argv[2]
outFile = subsetName(argv[2])
print('creating '+outFile)

with open(subsetPmids) as pmids, open(inFile) as fin, open(outFile, 'w') as fout:
    i = 0
    for pmid in pmids:
        pmid = pmid.strip()
        for document in fin:
            if pmid in document:
                i += 1
                if (i % 10000 == 0): print (i)
                fout.write(document)
                break
