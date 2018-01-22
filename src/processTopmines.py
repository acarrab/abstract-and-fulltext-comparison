#!/usr/bin/env python3
from pexpect import run
from sys import exit, argv

if len(argv) < 3: exit("args: <topmine directory> <output directory>")

tdir = '/'.join(argv[1].split('/'))

sourceFile = 'output/outputFiles/corpus.txt'


files = [
    (x[len(tdir)+1:].split('/')[0], x)
    for x in run('bash -c "ls -d {}/*/{}"'.format(tdir, sourceFile)).decode().split()
]

run('mkdir ' + argv[2])

for directory, corpus in files:
    newFile = '/'.join(argv[2].split('/') + [directory.strip('/') + '.data'])
    print('creating: '+newFile)
    with open(corpus) as fin, open(newFile, 'w') as fout:
        for document in fin:
            fout.write(" ".join(["_".join(n_gram.split()) for n_gram in document.split(',')[1:]]) + "\n")
