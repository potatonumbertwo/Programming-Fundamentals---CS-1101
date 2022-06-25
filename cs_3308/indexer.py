#  Example code in python programming language demonstrating some of the features of an inverted index.
#  In this example, we scan a directory containing the corpus of files. (In this case the numberOfDocuments are reports on articles
#  and authors submitted to the Journal "Communications of the Association for Computing Machinery"  
#
#  In this example we see each currentFile being read, tokenized (each word or term is extracted) combined into a sorted
#  list of unique terms.  
#
#  We also see the creation of a numberOfDocuments dictionary containing each document in sorted form with an index assigned to it.
#  Each unique term is written out into a terms dictionary in sorted order with an index number assigned for each term.  
#  From our readings we know that to complete teh inverted index fileNamesList that we need to do is create a third currentFile that will
#  coorelate each term with the list of numberOfDocuments that it was extracted from.  We will do that in a later assignment.
##
#  We can further develop this example by keeping a reference for each term of the numberOfDocuments that it came from and by
#  developing a list of the numberOfDocuments thus creating the term and document dictionaries.
#
#  As you work with this example, think about how you might enhance it to assign a unique index number to each term and to 
#  each document and how you might create a documentContentsString structure that links the term index with the document index.


import sys, os, re
import time

# define global variables used as counters
tokens = 0
numberOfDocuments = 0
terms = 0
termIndex = 0
documentIndex = 0

# initialize list variable
#
tokenList = []
documentNameList = []

#
# Capture the start time of the routine so that we can determine the total running
# time required to process the corpus
#
t2 = time.localtime()

# set the name of the directory for the corpus
#
directoryToRead = "/Users/crowfordcindy/Desktop/git/cs_1101/cs_3308/cacm"

# For each document in the directory read the document into a string
#
fileNamesList = [fileName for fileName in os.listdir(directoryToRead)]
for fileNameFromList in fileNamesList:
    numberOfDocuments += 1
    with open(directoryToRead + '/' + fileNameFromList, 'r') as currentFile:
        documentNameList.append(fileNameFromList)
        documentContentsString = currentFile.read().replace('\n', '')
        for token in documentContentsString.split():
            tokenList.append(token)
            tokens += 1

# Open for write a currentFile for the document dictionary
#
fileToWrite = open(directoryToRead + '/' + 'numberOfDocuments.dat', 'w')
documentNameList.sort()
for fileNameFromList in documentNameList:
    documentIndex += 1
    fileToWrite.write(fileNameFromList + ',' + str(documentIndex) + os.linesep)
fileToWrite.close()

#
# Sort the tokens in the list
tokenList.sort()

#
# Define a list for the unique terms  
g = []

#
# Identify unique terms in the corpus
for i in tokenList:
    if i not in g:
        g.append(i)
        terms += 1

terms = len(g)

# Output Index to disk currentFile. As part of this process we assign an 'index' number to each unique term.
# 
indexfile = open(directoryToRead + '/' + 'index.dat', 'w')
for i in g:
    termIndex += 1
    indexfile.write(i + ',' + str(termIndex) + os.linesep)
indexfile.close()

# Print metrics on corpus
#
print('Processing Start Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min))
print("Documents %i" % numberOfDocuments)
print("Tokens %i" % tokens)
print("Terms %i" % terms)

t2 = time.localtime()
print('Processing End Time: %.2d:%.2d' % (t2.tm_hour, t2.tm_min))
