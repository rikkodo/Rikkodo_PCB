#!/bin/bash

for i in $(seq 11 44)
do
    j=$(($i-5))
    # echo $i $j
    gsed -e 's/"SW'$i'"/"SW'$j'"/g' -e 's/"D'$i'"/"D'$j'"/g' -i $1
done
