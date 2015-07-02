__author__ = 'jarekcieslak'

import io
from MapReduce import *


mr = MapReduce()


def mapper(record):
    seq_id = record[0]
    nucleotide = record[1]
    nucleotide_new = nucleotide[:-10]
    mr.emit_intermediate(nucleotide_new, seq_id)


def reducer(key, list):
    mr.emit(key)

def main():
    inputfile = open('data/dna.json')
    mr.execute(inputfile, mapper, reducer)


main()