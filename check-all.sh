#!/usr/bin/env bash

set -e

submodules=`ls -d */ | xargs`

for DD in ${submodules[@]}; do
    cd ${DD} && \
    echo ${DD} && git fetch && git status | grep "up to date"
    #echo ${DD} && git checkout master
    retval=$?
    if [ $retval -ne 0 ]; then
        echo "Error " ${DD}
    fi
    cd ..
done
