import sys
import os
import json
from collections import OrderedDict


def main():
    ## open the tweetfile
    tweet_file = open(sys.argv[1])
    #tweet_file = open("/Users/micha/Google Drive/WORKSPACE/travaille/side projects/Python/2013_UWash_IntroDataScience/uWash.introDS.hw1/src/output_20.txt")

    ## create dictionary and counter for total tokens

    freqDict = {}
    sumOfTokens = 0.0

    ## process tweet_file, add all words to dictionary and count them

    for line in tweet_file:
        hashtags = json.loads(line).get('entities', "no entities").get('hashtags', "no tags")
        # print hashtags

        for hashtag in hashtags:
            sumOfTokens += 1
            hashText = hashtag.get('text', 'no hashatag text').encode('utf-8')
            if (freqDict.get(hashText) == None):
                freqDict[hashText] = 1
            else:
                freqDict[hashText] += 1



    # print freqDict

    d = sorted(freqDict.items(), key=lambda x: (-x[1], x[0]))

    print d[0:10]


if __name__ == '__main__':
    main()
    
    

    
