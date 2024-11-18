#!/bin/bash

# download PDB 1KFS (Klenow Fragment WT)
mkdir -p data
curl -O "https://www.rcsb.org/fasta/entry/1KFS"
mv 1KFs data/1KFs_raw.fasta
