subsetSize=$1
inDir=$2
outDir=$3

runner=quickSubset.out

function red() { echo $(tput setaf 1)$@$(tput sgr0); }
function exe() { echo $(tput setaf 1)\$ "$@"$(tput sgr0); $@; }

function newCsv() {
    filename=$(basename "$1")
    base=${filename%.*}
    echo ${outDir}$base.csv
}


exe g++ -O3 ./src/quickSubset.cpp -o $runner

for fileName in $(ls $inDir); do
    oldFile=${inDir}$fileName
    newFile=$(newCsv ${outDir}$fileName)
    red "awk -F" " '{print $1}' $oldFile | ./$runner $subsetSize $(wc -l $oldFile) > $newFile"
    awk -F" " '{print $1}' $oldFile | ./$runner $subsetSize $(wc -l $oldFile) > $newFile
    echo
done
