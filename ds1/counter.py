__author__ = 'jarekcieslak'
'''
program builds dictionary of items and scores
'''


import sys

afinnfile = open(sys.argv[0])
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer.

print scores.items() # Print every (term, score) pair in the dictionary
