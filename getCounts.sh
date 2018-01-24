
docCount=1328035
inDir=$1
outDir=$2

runner=getCounts.out

function red() { echo $(tput setaf 1)$@$(tput sgr0); }
function exe() { echo $(tput setaf 1)\$ "$@"$(tput sgr0); $@; }

exe g++ -O3 ./src/getUniqueWordCount.cpp -o $runner
for fileName in $(ls $inDir); do
    red "./$runner $docCount < ${inDir}$fileName > ${outDir}count_$fileName"
    ./$runner $docCount < ${inDir}$fileName > ${outDir}count_$fileName
done
