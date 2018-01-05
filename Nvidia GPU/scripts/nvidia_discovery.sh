#!/bin/bash

echo "{"
echo '    "data":['
FIRST=1

for line in $(nvidia-smi --list-gpus | awk -F ':' '{gsub("GPU ", "");print $1}')
do
    if [ $FIRST != 0 ]; then
        FIRST=0
    else
        ELEMENT="{ \"{#GPUID}\": $GPU },"
        echo "        $ELEMENT"
    fi
    GPU=$line
done

ELEMENT="{ \"{#GPUID}\": $GPU }"
echo "        $ELEMENT"
echo '    ]'
echo "}"

