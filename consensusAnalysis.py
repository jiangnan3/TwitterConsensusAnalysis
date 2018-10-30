import nltk
from nltk.classify import *
from nltk.corpus import stopwords
import nltk.classify.util
import csv
import re

stopwords = open('StopWords.txt')
stopwords = stopwords.read().split('\n')
traindataset = "traindataset.csv"
testdataset = "test.csv"

def repetition(word):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", word)

def FeatureList(tweet):
    words = tweet.split()
    featurelist = []
    for word in words:
        word = repetition(word).strip('\'"?,.')
        flag = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", word)
        if (word in stopwords or flag is None):
            continue
        else:
            featurelist.append(word.lower())
    return featurelist

def featuresummary(filename):
    tweetdata = csv.reader(open(filename, 'rb'))
    tweetandsentiment = []
    for line in tweetdata:
        sentiment = line[1]
        tweet = line[3]
        featurelist = FeatureList(tweet)
        tweetandsentiment.append((featurelist, sentiment))
    return tweetandsentiment

tweetandsentiment = featuresummary(traindataset)
testdatainput = featuresummary(testdataset)

def wordfeatures(tweetsentiment):
    allwordlist = []
    for item in tweetsentiment:
        allwordlist.extend(item[0])
    wordlist = nltk.FreqDist(allwordlist)
    word_features = wordlist.keys()
    return word_features

word_features = wordfeatures(tweetandsentiment) 

def extract_features(tweet):
    tweetset = set(tweet)
    features = {}
    for word in word_features:
        if (word in tweetset):
            numlogic = 1
        else:
            numlogic = 0
        features['%s' % word] = numlogic
    return features

trainingset = nltk.classify.apply_features(extract_features, traindataset)
testset = nltk.classify.apply_features(extract_features, testdataset)

classifier = nltk.NaiveBayesClassifier.train(trainingset)
accuracy = nltk.classify.accuracy(classifier, testset)

print accuracy

# Analysis of Moonlight
Moonlight = open("/BestPicture/Moonlight")
Moonlight = Moonlight.read().split('\n')

score = 0

for tweet in Moonlight:
    input = tweet.lower().split()
    score = score + classifier.classify(extract_features(input))

print score
