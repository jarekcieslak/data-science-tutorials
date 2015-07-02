__author__ = 'jarekcieslak'

from MapReduce import *


mr = MapReduce()


def mapper(record):
    key = record[0]
    value = record[1]
    # print key
    # print value
    t = sorted([key, value])

    mr.emit_intermediate(tuple(t), 1)


def reducer(key, list_of_values):
    # assign tuple to variables
    person, friend = key

    # check if there are duplicates
    if (len(list_of_values) == 1):
        mr.emit((person, friend))
        mr.emit((friend, person))


def main():
    inputfile = open('data/friends.json')
    mr.execute(inputfile, mapper, reducer)


main()