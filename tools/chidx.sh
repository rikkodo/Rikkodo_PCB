#!/bin/bash

USAGE="""Usage $0 filename
<filename>で指定したファイルの数字を調整する。
SWの番号がズレる時などに使用する。

番号は使用時に調整する。
"""

if [ $# -ne 1 ]; then
    echo "$USAGE" 1>&2
    exit 1
fi

# for i in $(seq 12 -1 9)
for i in $(seq 12 20)
do
    j=$(($i-2))
    # echo $i $j
    # gsed -e 's/"LED'$i'"/"LED'$j'"/g' -e 's/"D'$i'"/"D'$j'"/g' -i $1
    gsed -e 's/"LED'$i'"/"LED'$j'"/g' -i.bak $1
done
