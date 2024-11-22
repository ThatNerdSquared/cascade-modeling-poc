from pymol import cmd

# load the raw PDB
cmd.load("data/1KFS_wt.pdb")

# activate pymol wizard
cmd.wizard("mutagenesis")
pdb = cmd.get_names()[0]
cmd.get_wizard().set_mode("ALA")
cmd.get_wizard().do_select("chain A and residue 355")
cmd.get_wizard().apply()
cmd.get_wizard().do_select("chain A and residue 357")
cmd.get_wizard().apply()
cmd.set_wizard("done")
cmd.save("data/1KFS_mt.pdb", pdb)
