import sys, os, re
import time
import datetime

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# define global variables used as counters
# tokens = 0
# numberOfDocuments = 0
terms = 0
termIndex = 0
documentIndex = 0

# initialize list variable
tokenList = []
documentNameList = []

# Capture the start time of the routine so that we can determine the total running
# time required to process the corpus
startTime = time.localtime()
start = datetime.datetime.now()

# set the name of the directory for the corpus
# directoryToRead = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308/cacm"
directoryToRead = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308/corpus"
directoryToWrite = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308"


# For each document in the directory read the document into a string


def scan_directroy():
    tokens = 0
    numberOfDocuments = 0
    fileNamesList = [fileName for fileName in os.listdir(directoryToRead)]
    for fileNameFromList in fileNamesList:
        numberOfDocuments += 1
    with open(directoryToRead + '/' + fileNameFromList, 'r') as currentFile:
        documentNameList.append(fileNameFromList)
        documentContentsString = currentFile.read().replace('\n', '')
        for token in documentContentsString.split():
            tokenList.append(token)
            tokens += 1


def remove_spot_words():
    for i in range(1):
        # this will convert
        # the word into tokens
        text_tokens = word_tokenize(tokens)

    tokens_without_stop_words = [
        word for word in text_tokens if not word in stopwords.words()]
    # print(tokens_without_stop_words)


# Open for write a currentFile for the document dictionary
fileToWrite = open(directoryToWrite + '/' + 'numberOfDocuments.dat', 'w')
documentNameList.sort()
for fileNameFromList in documentNameList:
    documentIndex += 1
    fileToWrite.write(fileNameFromList + ',' + str(documentIndex) + os.linesep)
fileToWrite.close()

# Sort the tokens in the list
tokenList.sort()

# Define a list for the unique terms
uniqueTermList = []

# Identify unique terms in the corpus
for i in tokenList:
    if i not in uniqueTermList:
        uniqueTermList.append(i)
        terms += 1

terms = len(uniqueTermList)

# Output Index to disk currentFile. As part of this process we assign an 'index' number to each unique term.
indexFile = open(directoryToWrite + '/' + 'index.dat', 'w')
for i in uniqueTermList:
    termIndex += 1
    indexFile.write(i + ',' + str(termIndex) + os.linesep)
indexFile.close()

# Print metrics on corpus
print('Processing Start Time: %.2d:%.2d:%.2d' % (startTime.tm_hour, startTime.tm_min, startTime.tm_sec))
print("The total number of documents processed: %i" % numberOfDocuments)
print("The total number of terms: %i" % tokens)
print("The total number of unique terms: %i" % terms)
print("Total number of terms found that matched one of the stop words program’s stop words list: ")

endTime = time.localtime()
end = datetime.datetime.now()
print('Processing End Time: %.2d:%.2d:%.2d' % (endTime.tm_hour, endTime.tm_min, endTime.tm_sec))
print("Total running time: " + str((end - start)))
