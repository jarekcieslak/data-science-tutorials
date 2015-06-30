import sys
import os
import json


def createSentimentDict(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # return dictionary    
    return scores


def main():
    ## open the 2 files that are added via the arguments
    #sent_file = open(sys.argv[1])
    sent_file = open("products/afinn-11.txt")
    #tweet_file = open(sys.argv[2])
    tweet_file = open("products/problem_1_submission.txt")

    ## create dictionary

    # Slownik w ktorym mamy przypusane wartosci do kluczowych slow z pliku.
    # nacechowanie pozytywne negatywne slow
    sentiDict = createSentimentDict(sent_file)

    # slownik w ktorym beda wszystkie nowe zwroty i ich wartosci nacechowania.
    newDict = {}


    #???
    sentiTweetList = [] #adds the sentiment of each tweet to list (e.g., first element, first tweet, etc
    #tweetNum = 0

    for line in tweet_file:
        # tweet = json.loads(line)
        # print tweet
        # print tweet['text'].encode('utf-8').split()
        tweet = json.loads(line).get('text', 'EMPTY').encode('utf-8').split()   #.keys() #[u"text"]
        sentCount = 0

        for word in tweet:
            wordSentiment = sentiDict.get(word, 0)
            sentCount += wordSentiment


            # if word not in sentiDict check if it's on new Dict
            if int(wordSentiment) == 0:

            # if word is not on newDict: add it and add sentiment score to list
                if newDict.get(word) == None:
                    newDict[word] = []

        # assign total tweet sentiment to list
        sentiTweetList.append(sentCount)



    # go through all tweets again from the beginning
    tweet_file.seek(0)
    tweetCounter = 0

    for line in tweet_file:

        tweet = json.loads(line).get('text', "EMPTY").split()   #.keys() #[u"text"]

        # if word is newDict, add sentiment of tweet from sentiTweetList        
        for word in tweet:

            if newDict.get(word) != None:
                word = word.encode('utf-8')
                newDict[word].append(sentiTweetList[tweetCounter])
        tweetCounter += 1

    #
    # print '\n\n stary dict \n'
    # print sentiDict
    # print '\n\n nowy dict\n'
    #
    # for key in newDict.keys():
    #     print '%s - %s' % (key, str(newDict[key]))






    # go through all keys in dict and calculate the average of all values

    d = dict(newDict)
    for key in d:
        # print key
        # print newDict[key]
        # print '\n'
        if d[key] == []:
            d[key] = 0.0
            # continue
        else:
            d[key] = sum(d[key]) / float(len(d[key]))

    # newDict = d


    # print results key-value pairs
    #
    for key in d:
        # if d[key]>0:
        print key, d[key]


if __name__ == '__main__':
    main()
    
    

    
