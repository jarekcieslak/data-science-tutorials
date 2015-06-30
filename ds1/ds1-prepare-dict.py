__author__ = 'jarekcieslak'

import io

inputFile = open('afinn-11.txt')
scores = {}

for line in inputFile:
    term, score = line.split('\t')
    scores[term] = int(score)

print scores.items()

