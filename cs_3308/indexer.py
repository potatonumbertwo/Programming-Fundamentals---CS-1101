import sys, os, re
import time
import datetime

from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords


class Indexer:
    nltk.download('stopwords')

    # define global variables used as counters
    tokens = 0
    numberOfDocuments = 0
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

    uniqueTermList = []

    def scan_directroy(self):
        fileNamesList = [fileName for fileName in os.listdir(self.directoryToRead)]
        for fileNameFromList in fileNamesList:
            self.numberOfDocuments += 1
        with open(self.directoryToRead + '/' + fileNameFromList, 'r') as currentFile:
            self.documentNameList.append(fileNameFromList)
            documentContentsString = currentFile.read().replace('\n', '')
            for token in documentContentsString.split():
                self.tokenList.append(token)
                self.tokens += 1

    def remove_spot_words(self):
        for i in range(1):
            # this will convert
            # the word into tokens
            text_tokens = word_tokenize(self.tokens)

        tokens_without_stop_words = [
            word for word in text_tokens if not word in stopwords.words()]
        # print(tokens_without_stop_words)

    def writeToFile(self):
        # Open for write a currentFile for the document dictionary
        fileToWrite = open(self.directoryToWrite + '/' + 'numberOfDocuments.dat', 'w')
        self.documentNameList.sort()
        for fileNameFromList in self.documentNameList:
            self.documentIndex += 1
            fileToWrite.write(fileNameFromList + ',' + str(self.documentIndex) + os.linesep)
        fileToWrite.close()

    def getUniqueTerms(self):
        # Sort the tokens in the list
        self.tokenList.sort()

        # Identify unique terms in the corpus
        for i in self.tokenList:
            if i not in self.uniqueTermList:
                self.uniqueTermList.append(i)
                self.terms += 1

        terms = len(self.uniqueTermList)

    def writeIndexToDisk(self):
        # Output Index to disk currentFile. As part of this process we assign an 'index' number to each unique term.
        indexFile = open(self.directoryToWrite + '/' + 'index.dat', 'w')
        for i in self.uniqueTermList:
            self.termIndex += 1
            indexFile.write(i + ',' + str(self.termIndex) + os.linesep)
        indexFile.close()

    def outputPrint(self):

        # Print metrics on corpus
        print('Processing Start Time: %.2d:%.2d:%.2d' % (
            self.startTime.tm_hour, self.startTime.tm_min, self.startTime.tm_sec))
        print("The total number of documents processed: %i" % self.numberOfDocuments)
        print("The total number of terms: %i" % self.tokens)
        print("The total number of unique terms: %i" % self.terms)
        print("Total number of terms found that matched one of the stop words program’s stop words list: ")

        endTime = time.localtime()
        end = datetime.datetime.now()
        print('Processing End Time: %.2d:%.2d:%.2d' % (endTime.tm_hour, endTime.tm_min, endTime.tm_sec))
        print("Total running time: " + str((end - self.start)))


indexer = Indexer()

indexer.scan_directroy()
indexer.writeToFile()
indexer.getUniqueTerms()
indexer.writeIndexToDisk()
indexer.outputPrint()
