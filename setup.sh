#!/bin/bash

# download PDB 1KFS (Klenow Fragment WT)
mkdir -p data
curl -O "https://files.rcsb.org/view/1KFS.pdb"
mv 1KFS.pdb data/1KFS_raw.pdb

# split oligo from protein, clean out ions/waters
pdb_selchain -A data/1KFs_raw.pdb | pdb_delhetatm > data/1KFS_wt.pdb
pdb_selchain -B data/1KFs_raw.pdb | pdb_delhetatm > data/oligo.pdb
