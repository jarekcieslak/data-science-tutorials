__author__ = 'jarekcieslak'

import sys
from MapReduce import *


mr = MapReduce()
_debug = False

def mapper(record):
    id = record[1]
    mr.emit_intermediate(id, record)



def reducer(key, list_of_values):
    orders = []
    line_items = []
    for item in list_of_values:
        if item[0] == "order":
            orders.append(item)

        elif (item[0] == "line_item"):
            line_items.append(item)

    if _debug:
        print key
        print orders
        print line_items
        print '\n\n\n'

    for order in orders:
        for item in line_items:
            mixed_item = order + item
            mr.emit(mixed_item)


def main():
    inputdata = open("data/records.json")
    mr.execute(inputdata, mapper, reducer)




main()