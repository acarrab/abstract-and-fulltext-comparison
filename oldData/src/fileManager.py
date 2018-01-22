#!usr/bin/env python3
from sys import argv, exit
from pexpect import run
from re import sub

if len(argv) < 3: exit('<in: ../topmines/{*/output}/corpus.txt> <out: directoryOut/{}>')



# adds / to end
def dstrip(directory): return sub(r'^/+', '/',sub(r'/*$', '/', directory))
# does not add /
def strip(fileName): return sub(r'^/+', '/',sub(r'/+$', '/', fileName))

def ls(path): return run('bash -c "ls {}"'.format(strip(path))).decode().split()
# lists full path
def listPaths(directory): return ls('-d '+dstrip(directory))
# lists only filename
def listNames(directory): return ls(dstrip(directory))
# lists path relatively
def listRelNames(baseDir, rel): return ls('{}*/{}'.format(dstrip(baseDir), strip(rel)))






dirIn = dstrip(argv[1])
dirOut = dstrip(argv[2])


if len(argv) > 3:
    files = dict([(n, (dirIn+n, dirOut+n)) for n in listNames(dirIn)])
else:
    files = dict([(n, (dirIn+n, dirOut+n)) for n in listNames(dirIn)])

run('mkdir '+dirOut)
for outfile in listNames(dirOut):
    if outfile in files:
        del files[outfile]


def fstreams():
    for (inPath, outPath) in files.values():
        print('\n'.join([inPath, 'to', outPath, '~'*60]))
        with open(inPath) as fin, open(outPath, 'w')  as fout:
            yield (fin, fout)
