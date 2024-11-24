#!/bin/bash

# download 1KFS (Klenow Fragment WT)
mkdir -p data
pdb_fetch 1KFS > data/1KFS_raw.pdb

# split oligo from protein, clean out ions/waters
pdb_selchain -A data/1KFs_raw.pdb | pdb_delhetatm > data/1KFS_wt.pdb
pdb_selchain -B data/1KFs_raw.pdb | pdb_delhetatm > data/oligo.pdb

# create mutant
./mutate_1KFS.py

# generate active-passive files
# THESE STEPS NEED TO BE MANUALLY PASTED INTO chainA.pass AND chainB.pass
haddock3-restraints calc_accessibility --cutoff 0.15 data/1KFS_mt.pdb
haddock3-restraints calc_accessibility --cutoff 0.15 data/oligo.pdb

haddock3-restraints active_passive_to_ambig chainA.pass chainB.pass > ambig_surface.tbl

haddock3 modelrun.cfg
