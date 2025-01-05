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

cp "$1" "$1.bak"

# for i in $(seq 44 -1 11)
for i in $(seq 11 44)
do
    j=$(($i-5))
    # echo $i $j
    gsed -e 's/"SW'$i'"/"SW'$j'"/g' -e 's/"D'$i'"/"D'$j'"/g' -i $1
done
