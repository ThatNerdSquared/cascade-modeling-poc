from Bio import SeqIO, Seq, SeqRecord

OPTIMIZER_AA_SEQ = Seq.Seq("MGSSHHHHHHSSGLVPRGSHMASMTGGQQMGRGSEFV")

# read in raw data
records = list(SeqIO.parse("data/1KFs.fasta", "fasta"))
raw_oligo_seq = records[0].seq
raw_wt_seq = records[1].seq

# add optimizer sequence
wt_seq = OPTIMIZER_AA_SEQ + raw_wt_seq[1:]

# mutate WT sequence to match Klenow Exo– (MT)
# at position 68: D->A
# at position 70: E->A
mt_seq = Seq.MutableSeq(wt_seq)
assert(mt_seq[67] == "D")
assert(mt_seq[69] == "E")
mt_seq[67] = "A"
mt_seq[69] = "A"
mt_seq = Seq.Seq(mt_seq)

# write back out to FASTA files
wt_seq_record = SeqRecord.SeqRecord(wt_seq, id="Klenow Fragment (WT)")
mt_seq_record = SeqRecord.SeqRecord(mt_seq, id="Klenow Exo- (MT)")

SeqIO.write(wt_seq_record, "data/1KFs_wt.fasta", "fasta")
SeqIO.write(mt_seq_record, "data/1KFs_mt.fasta", "fasta")
