__author__ = 'jarekcieslak'

import sys
from MapReduce import *



# Part 1
mr = MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)
      # mr.emit_intermediate(w, 1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    mr.emit((key, list_of_values))



def main():

    inputdata = open('data/books.json')
    mr.execute(inputdata, mapper, reducer)


main()