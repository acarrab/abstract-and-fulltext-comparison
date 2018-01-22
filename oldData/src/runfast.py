#!/usr/bin/env python3
from fileman import files
from subrocess import run, PIPE


for infile, outfile in files:
    run('./fasttext skipgram -input {} -output {}'.format(infile, outfile), stdout=PIPE)
