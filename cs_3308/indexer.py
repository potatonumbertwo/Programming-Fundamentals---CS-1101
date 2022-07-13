import math
import sys, os, re
import time
import datetime
from nltk.stem import PorterStemmer

from pathlib import Path


class Indexer:
    # define global variables used as counters
    numberOfTerms = 0
    numberOfDocuments = 0
    numberOfUniqueTerms = 0
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
    directoryToRead = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308/unit_4/cacm"
    # directoryToRead = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308/unit_4/database"
    directoryToWrite = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308"

    # For each document in the directory read the document into a string

    uniqueTermList = []
    foundStopWords = 0

    termFrequencyDict = {}

    def scan_directroy(self, stop_dict):
        # read file and using porter stemmer to stem the terms
        porterStemmer = PorterStemmer()
        fileNamesList = [fileName for fileName in os.listdir(self.directoryToRead)]
        fileNamesList.sort()
        for fileNameFromList in fileNamesList:
            self.numberOfDocuments += 1
            with open(self.directoryToRead + '/' + fileNameFromList, 'r') as currentFile:
                self.documentNameList.append(fileNameFromList)
                documentContentsString = currentFile.read()
                for token in documentContentsString.split():
                    # Stem the word
                    token = porterStemmer.stem(token)

                    self.tokenList.append(token)
                    self.numberOfTerms += 1
                    if token in stop_dict:
                        self.foundStopWords += 1

    def write_to_file(self):
        # Open for write a currentFile for the document dictionary
        fileToWrite = open(self.directoryToWrite + '/' + 'numberOfDocuments.dat', 'w')
        self.documentNameList.sort()
        for fileNameFromList in self.documentNameList:
            self.documentIndex += 1
            fileToWrite.write(fileNameFromList + ',' + str(self.documentIndex) + os.linesep)
        fileToWrite.close()

    def get_unique_terms(self, stopDict):
        # Sort the numberOfTerms in the list
        self.tokenList.sort()

        # Identify unique numberOfUniqueTerms in the corpus
        for token in self.tokenList:

            tokenNotInTermList = token not in self.uniqueTermList
            tokenNotInStopDict = token not in stopDict
            if tokenNotInTermList and tokenNotInStopDict:
                self.uniqueTermList.append(token)
                self.numberOfUniqueTerms += 1

        terms = len(self.uniqueTermList)

    def write_index_to_disk(self):
        # Output Index to disk currentFile. As part of this process we assign an 'index' number to each unique term.
        indexFile = open(self.directoryToWrite + '/' + 'index.dat', 'w')
        for i in self.uniqueTermList:
            self.termIndex += 1
            indexFile.write(i + ',' + str(self.termIndex) + os.linesep)
        indexFile.close()

    def output_print(self):

        # Print metrics on corpus
        print('Processing Start Time: %.2d:%.2d:%.2d' % (
            self.startTime.tm_hour, self.startTime.tm_min, self.startTime.tm_sec))
        print("The total number of documents processed: %i" % self.numberOfDocuments)
        print("The total number of terms: %i" % self.numberOfTerms)
        print("The total number of unique terms: %i" % self.numberOfUniqueTerms)
        print(
            "Total number of terms found that"
            " matched one of the stop words program’s stop words list: ", self.foundStopWords)

        endTime = time.localtime()
        end = datetime.datetime.now()
        # print('Processing End Time: %.2d:%.2d:%.2d' % (endTime.tm_hour, endTime.tm_min, endTime.tm_sec))
        # print("Total running time: " + str((end - self.start)))
        # print("term frequency", self.termFrequencyDict)
        # print("Inverse Document Frequency: " + str(self.inverse_document_frequency()))
        # print("tf_idf_weighting" + str(self.tf_idf_weighting()))

    def read_stop_dict(self) -> dict:
        # read the stopwords.txt into a dictionary
        stop_dictionary = {}
        with open(Path(__file__).parent / "./unit_4/stopwords.txt") as f:
            for line in f:
                lineWithoutSlashN = line.replace('\n', '')
                stop_dictionary[lineWithoutSlashN] = lineWithoutSlashN
        return stop_dictionary

    def term_frequency(self):
        # term frequency stored in dictionary
        for term in self.tokenList:
            numberOfTimesTermHasBeenSeen = self.termFrequencyDict.get(term)
            if numberOfTimesTermHasBeenSeen is None:
                numberOfTimesTermHasBeenSeen = 1
            else:
                numberOfTimesTermHasBeenSeen += 1
            self.termFrequencyDict[term] = numberOfTimesTermHasBeenSeen

    def inverse_document_frequency(self):
        # calculate the inverse document
        idf = math.log(self.numberOfDocuments / len(self.termFrequencyDict))
        return idf

    # def tf_idf_weighting(self):
    # for i in self.tokenList:
    #     tf_idf = i * self.inverseDocumentFrequency()
    # return tf_idf


indexer = Indexer()
stop_dict = indexer.read_stop_dict()
indexer.scan_directroy(stop_dict)
indexer.write_to_file()
indexer.get_unique_terms(stop_dict)
indexer.write_index_to_disk()
indexer.term_frequency()
indexer.output_print()
