# seq_fetch_not_in_list

Author: Murat Buyukyoruk

        seq_fetch_not_in_list help:

This script is developed to fetch sequences from multifasta file that are not provided in the list file that contains accession numbers. 

SeqIO package from Bio is required to fetch sequences. Additionally, tqdm is required to provide a progress bar since some multifasta files can contain long and many sequences.

Syntax:

        python seq_fetch_not_in_list.py -i demo.fasta -l demo_sub_list.txt -o demo_sub_list.fasta

seq_fetch_not_in_list dependencies:

Bio module and SeqIO available in this package      refer to https://biopython.org/wiki/Download

tqdm                                                refer to https://pypi.org/project/tqdm/

Input Paramaters (REQUIRED):
----------------------------
	-i/--input		FASTA			Specify a fasta file. FASTA file requires headers starting with accession number. (i.e. >NZ_CP006019 [fullname])

	-l/--list		List			Specify a list of accession (Accession only). Each accession should be included in a new line (i.e. generated with Excel spreadsheet). Script works with or without '>' symbol before the accession.

	-o/--output		output file		Specify a output file name that should contain fetched sequences.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

