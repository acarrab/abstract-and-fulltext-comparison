import random
from sys import argv, exit

if len(argv) < 2: exit("<subset size in thousands>")

# number of lines in the file
n = 1328035
# selection size
k = int(argv[1]) * 1000
rest = k


oldFile = 'pmids.data'
newFile = oldFile.split('.')
newFile[0] += '_' + argv[1]
newFile = ".".join(newFile)


with open(oldFile, "r") as fin, open(newFile, "w") as fout:
    for line in fin:
        if 0 == random.randrange(0, int(float(n) / k)) or n == k:
            fout.write(line)
            k -= 1
            if k % 10000 == 0: print("written: " + str(rest - k))
            if k == 0: break
        n -= 1
