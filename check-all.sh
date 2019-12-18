#!/usr/bin/env bash

set -e

submodules=`find . -maxdepth 1 -not -path '*/\.*' -not -path '.' -type d | xargs`

for DD in ${submodules[@]}; do
    cd ${DD} && \
    brch=`git branch | grep '\*' | cut -d ' ' -f 2`
    #if [ $brch = "master" ]; then
        echo ${DD} && git fetch && git status | grep "up to date"
        #echo ${DD} && git checkout master
        retval=$?
        if [ $retval -ne 0 ]; then
            echo "Error " ${DD}
        fi
    #else
    #    echo working on ${DD} and brch=$brch skipping...
    #fi
    cd ..
done
