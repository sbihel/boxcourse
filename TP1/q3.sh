#! /bin/bash

cat ../ind_0.reads.fa | awk "NR==0 || NR%2==0" | awk "{print length($o)}" | sort | uniq -c
