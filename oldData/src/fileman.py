#!usr/bin/env python3
from sys import argv, exit
from subprocess import check_output
from re import compile, sub
from os.path import abspath, isfile

if len(argv) < 3: exit('<in: ../topmines/{*/output}/corpus.txt> <out: directoryOut/{}>')


def strip(directory): return sub(r'/+', '/', directory)
def run(s): return check_output(s, shell=True).decode()
def ls(pathRegex): return [abspath(f) for f in run('find {} -type f '.format(pathRegex)).split()]


path = sub(r'[}{]', '', argv[1])
base = abspath(argv[1].split('{')[0]) + '/'
rest = argv[1].split('}')[1]

def getName(f): return sub(r'^{}'.format(base),'', sub(r'{}$'.format(rest), '', f))


# (infile, outfile)
files = [ (f, argv[2].format(getName(f))) for f in ls(path) ]

def fstreams():
    for infile, outfile in files:
        run('mkdir -p {}'.format(sub('[^/]*$', '', outfile)))
        if not isfile(outfile):
            print('processing:\n\t{}\n\t{}'.format(infile, outfile))
            with open(infile) as fin, open(outfile, 'w') as fout:
                yield (fin, fout)
