#!/usr/bin/env python3
from fileman import fstreams

for fin, fout in fstreams():
    fout.write(fin.read())
