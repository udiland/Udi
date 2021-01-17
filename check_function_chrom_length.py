import re

# def create_chromosome_seq_file(file_path):
#     source_file = open(file_path, 'r')
#     content = source_file.read()
#     source_file.close()
#     delimiter_chr = re.compile(">(.*)([^>]+)")
#
#
#     seqs_chromosomes = delimiter_chr.findall(content)
#     dic = {}
#     for i in range(len(seqs_chromosomes)):
#         splitted_chr_seq = re.split("\n|[\s]+", seqs_chromosomes[i][1])
#         sequence = "".join(splitted_chr_seq)
#
#         chromosome = seqs_chromosomes[i][0] # Take the whole fasta header as chromosome name (without '>')
#         dic[chromosome] = len(sequence)
#
#     return dic

# print(create_chromosome_seq_file("sly.con"))

import pickle

with open("sly_genome_dic.p", "rb") as pkl:
    p = pickle.load(pkl)

print(p)

