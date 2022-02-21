#!/usr/bin/env bash

set -e

submodules=`find . -maxdepth 1 -not -path '*/\.*' -not -path '.' -type d | xargs`

echo ${submodules}

for DD in ${submodules[@]}; do
    cd ${DD} && \
    git checkout . && \
    brch=`git branch | grep '\*' | cut -d ' ' -f 2`
    if [ ${DD} = "./rust-sgx-sdk" ]; then
        cd ..
        continue
    elif [ ${DD} = "./dumb-all" ]; then
        cd ..
        continue
    fi

    branch="master"
    if [ ${DD} = "./num-bigint-dig-sgx" ]; then
        branch="dig"
        cd ..
        continue
    elif [ ${DD} = "./rust-protobuf-sgx" ]; then
        branch="v2.8"
    elif [ ${DD} = "./mio-sgx" ]; then
        branch="v0.6_sgx_1.1.3"
    elif [ ${DD} = "./deflate-rs-sgx" ]; then
        branch="dev"
    elif [ ${DD} = "./rustls-sgx" ]; then
        branch="mesalock_sgx"
    elif [ ${DD} = "./rusty_leveldb_sgx" ]; then
        branch="sgx"
    elif [ ${DD} = "./wabt-rs-sgx" ]; then
        branch="v0.9-core"
    elif [ ${DD} = "./sct.rs-sgx" ]; then
        branch="mesalock_sgx"
    elif [ ${DD} = "./webpki-sgx" ]; then
        branch="mesalock_sgx"
    elif [ ${DD} = "./webpki-roots-sgx" ]; then
        branch="mesalock_sgx"
    fi
        
    echo ${DD} && git checkout "v1.1.3-backup" || git checkout -b "v1.1.3-backup"
    git push -u origin "v1.1.3-backup" || echo ${DD} backup failed
    #echo ${DD} && git branch -a | grep backup
    cd ..
done
