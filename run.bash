#!/bin/bash
input=$1 

# String_Contain() { case $2 in *$1* ) return 0;; *) return 1;; esac ;}
# String_Contain "/" "${input}";

if [ -d "${input}" ];  then
    for each_file in "${input}"/*
    do
       python3 wav2num.py "${each_file}"
    done
else
    python3 wav2num.py ${input}
fi
