inDir=$1
outDir=$2

runner=getCounts.out
cfile="src/getNumberOfCounts.cpp"

function red() { echo $(tput setaf 1)$@$(tput sgr0); }
function exe() { echo $(tput setaf 1)\$ "$@"$(tput sgr0); $@; }

exe g++ -O3 $cfile -o $runner
for fileName in $(ls $inDir); do
    infile=${inDir}$fileName
    outfile=${outDir}count_${fileName%.*}.csv
    red "./$runner $(wc -l $infile) < $infile > $outfile"
    ./$runner $(wc -l $infile) < $infile > $outfile
done
