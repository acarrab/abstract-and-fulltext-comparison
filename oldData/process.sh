#!/bin/bash

function exe() { echo \$ $@; echo; $@; }
echo "setting up"
exe "python3 ./src/processTopmines.py ../topmines/{*}/output/outputFiles/corpus.txt ./ngramDocs/{}.data"
exe "python3 ./src/countNgrams.py ./ngramDocs/{*} ./ngramCounts/{}"


# analyze just the ngrams (separate from the number of instances of ngrams in the document)
exe "python3 ./src/uniqueNgramSizes.py ./ngramCounts/{*} ./uniqueSizes/{}"

# count ngrams size occurances in corpus
exe "python3 ./src/countNgrams.py ./ngramCounts/{*} ./sizeDistribution/{}"

echo "this can cause grief"
exe "python3 ./src/addpmids.py ./ngramDocs/{abstract_500*} ./documents/{} ./subset_pmids.data"
exe "python3 ./src/addpmids.py ./ngramDocs/{fulltext_500*} ./documents/{} ./subset_pmids.data"

exe "python3 ./src/addpmids.py ./ngramDocs/{*} ./documents/{} ./pmids.data"
