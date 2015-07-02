__author__ = 'jarekcieslak'

from MapReduce import *


mr = MapReduce()


def mapper(record):
    key = record[0]
    value = record[1]
    # print key
    # print value
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    my_set = set(list_of_values)
    num_friends = len(my_set)
    mr.emit((key, num_friends))


def main():
    inputfile = open('data/friends.json')
    mr.execute(inputfile, mapper, reducer)


main()