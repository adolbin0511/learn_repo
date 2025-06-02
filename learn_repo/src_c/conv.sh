#!/bin/bash
LIST="$(ls *.c)" 
for i in "$LIST"; do
 iconv -f KOI8-R -t UTF-8 < i > i||_koi8
done


