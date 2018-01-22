#!/bin/bash
if [[ $# < 4 ]]; then
    echo "expected <document files> <temp label> <number of threads> <isFirstRun (0 or 1)>"
    exit -1
fi

function green() { echo $(tput setaf 2)$@$(tput sgr0); }
function yellow() { echo $(tput setaf 3)$@$(tput sgr0); }
function red() { echo $(tput setaf 1)$@$(tput sgr0); }

function exe() { echo $(yellow \$) $(red $1) ${@:2}; $@; }

datafile=$(readlink -f $1)
tmp=$(readlink -f ./tmp/$2)
exe mkdir $tmp

base_autophrase=$(readlink -f "./src/AutoPhrase")
cp src/my_auto_phrase.sh src/my_phrasal_segmentation.sh $base_autophrase

exe cp -r $base_autophrase/* $tmp

exe pushd $tmp

exe ./my_auto_phrase.sh $datafile $4 $3

exe popd
