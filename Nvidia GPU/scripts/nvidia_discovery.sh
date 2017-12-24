#!/bin/bash

echo "{"
echo '    "data":['
FIRST=1
 
while read line; do
    if [ $FIRST != 0 ]; then
        FIRST=0
    else
        ELEMENT="{ \"{#GPUID}\": $GPU },"
        echo "        $ELEMENT"
    fi
    GPU=$line
done <<< $(nvidia-smi --list-gpus | awk -F ':' '{gsub("GPU ", "");print $1}')
ELEMENT="{ \"{#GPUID}\": $GPU }"
echo "        $ELEMENT"
echo '    ]'
echo "}"
