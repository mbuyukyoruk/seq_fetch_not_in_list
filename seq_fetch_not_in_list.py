import argparse
import sys
import os
import subprocess
import textwrap

try:
    from Bio import SeqIO
except:
    print("SeqIO module is not installed! Please install SeqIO and try again.")
    sys.exit()

try:
    import tqdm
except:
    print("tqdm module is not installed! Please install tqdm and try again.")
    sys.exit()

parser = argparse.ArgumentParser(prog='python seq_fetch_not_in_list.py',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=textwrap.dedent('''\

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

	-o/--output		output file	    Specify a output file name that should contain fetched sequences.

Basic Options:
--------------
	-h/--help		HELP			Shows this help text and exits the run.

      	'''))
parser.add_argument('-i', '--input', required=True, type=str, dest='filename',
                    help='Specify a original fasta file.\n')
parser.add_argument('-l', '--list', required=True, type=str, dest='list',
                    help='Specify a list of accession numbers NOT to fetch.\n')
parser.add_argument('-o', '--output', required=True, dest='out',
                    help='Specify a output fasta file name.\n')

results = parser.parse_args()
filename = results.filename
list = results.list
out = results.out

acc_list = []

os.system('> ' + out)

proc = subprocess.Popen("wc -l < " + list, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length + 1)) as pbar:
    pbar.set_description('Reading list ...')
    with open(list, "r") as file:
        for line in file:
            pbar.update()
            acc = line.split("\n")[0]
            acc_list.append(acc)

proc = subprocess.Popen("grep -c '>' " + filename, shell=True, stdout=subprocess.PIPE, text=True)
length = int(proc.communicate()[0].split('\n')[0])

with tqdm.tqdm(range(length)) as pbar:
    pbar.set_description('Writing...')
    for record in SeqIO.parse(filename, "fasta"):
        pbar.update()
        if record.id.split("_PAZ")[0] not in acc_list:
            f = open(out, 'a')
            sys.stdout = f
            print(record.format("fasta"))

