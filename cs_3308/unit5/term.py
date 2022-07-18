"""
This file contains an example search engine that will search the inverted index that we build as part of our assignments in units 3 and 5.
"""
import sys, os, re
import math
import sqlite3
import time

# use simple dictionary data structures in Python to maintain lists with hash keys
docs = {}
resultslist = {}
term = {}

# regular expression or: extract words, extract ID rom path, check or hexa value chars = re.compile(r'\W+')
pattid = re.compile(r'(\d{3})/(\d{3})/(\d{3})')


#
# Docs class: Used to store information about each unit document.
# In this is the Term object which stores each
# unique instance of termid or a docid.
#
class Docs():
    terms = {}

    # def get_unique_terms(self):
    #     # Sort the numberOfTerms in the list
    #     self.tokenList.sort()
    #
    #     # Identify unique numberOfUniqueTerms in the corpus
    #     for token in self.tokenList:
    #
    #         tokenNotInTermList = token not in self.uniqueTermList
    #         tokenNotInStopDict = token not in self.stop_words
    #         if tokenNotInTermList and tokenNotInStopDict:
    #             self.uniqueTermList.append(token)
    #             self.numberOfUniqueTerms += 1
    #
    #     terms = len(self.uniqueTermList)


#
# Term class: used to store information or each unique termid
#
class Term:
    documentFrequency = 0
    termFrequency = 0
    inverseDocumentFrequency = 0.0
    termFrequencyInverseDocumentFrequency = 0.0

    # split on any chars
    def splitchars(line):
        return list(line)

    # this small routine is used to accumulate query inverseDocumentFrequency values
    def ElementQuery(elen, a):
        return (float(math.pow(a.inverseDocumentFrequency, 2)) + float(elen))

    # this small routine is used to accumulate document termFrequencyInverseDocumentFrequency values
    def elenD(elen, a):
        return (float(math.pow(a.termFrequencyInverseDocumentFrequency, 2)) + float(elen))


def main():
    if __name__ == ' __main__ ':
        main()


# Create a sqlite database to hold the inverted index.
# The isolation_level statement turns
# on autocommit which means that changes made in the database are
# committed automatically

connection = sqlite3.connect("indexer_part2.db")
connection.isolation_level = None
cursor = connection.cursor()

#
#
#
line = input('Enter the search terms, each separated by a space: ')

#
# Capture the start time of the search so that we can determine the total running
# time required to process the search
#
startTime = time.localtime()
print('Start Time: %.2d:%.2d:%.2d' % (startTime.tm_hour, startTime.tm_min, startTime.tm_sec))

#
# This routine splits the contents of the line into tokens
tokens = Term.splitchars(line)

#
# Get the total number of documents in the collection
#
query = "select count(*) from documentdictionary"
cursor.execute(query)
row = cursor.fetchone()
documents = row[0]

# Maximum number of search terms that exists in any one document.
maxterms = float(0)

# process the tokens (search terms) entered by the user
for token in tokens:
    # This statement removes the newline character if found
    token = token.replace('\n', '')

    # This statement converts all letters to lower case
    tokenInLowercase = token.lower().strip()

    #
    # Execute query to determine if the term exists in the dictionary
    #
    query = "select count(*) from termdictionary where term = '%s'" % tokenInLowercase
    cursor.execute(query)
    row = cursor.fetchone()

    # If the term exists in the dictionary retrieve all documents for the term and store in a list

    if row[0] > 0:
        query = "select distinct docid, termFrequencyInverseDocumentFrequency," \
                " documentFrequency, termFrequency, " \
                "posting.termid from termdictionary,posting " \
                "where posting.termid = termdictionary.termid " \
                "and term = '%s' order by docid, posting.termid" % tokenInLowercase
        cursor.execute(query)
        for row in cursor:
            i_termid = row[4]
            i_docid = row[0]
            if not (i_docid in docs.keys()):
                docs[i_docid] = Docs()
                docs[i_docid].terms = {}

            if not (i_termid in docs[i_docid].terms.keys()):
                docs[i_docid].terms[i_termid] = Term()
                docs[i_docid].terms[i_termid].documentFrequency = row[2]
                docs[i_docid].terms[i_termid].termFrequency = row[3]
                docs[i_docid].terms[i_termid].inverseDocumentFrequency = 0.0
                docs[i_docid].terms[i_termid].termFrequencyInverseDocumentFrequency = 0.0

#
# Calculate termFrequencyInverseDocumentFrequency values or both the query and each document
# Using the termFrequencyInverseDocumentFrequency (or weight) value, accumulate the vectors and calculate
# the cosine similarity between the query and each document
#

#
# Calculate the denominator which is the euclidean length of the query
# multiplied by the euclidean length of the document
#

#
# This search engine will match on any number of terms and the cosine similarity of a
# document matches on 1 term that appears in a document in the collection tends to score highly
# the float(no_terms/maxtersm) portion of the equation is designed to give a higher weight
# to documents that match on more than 1 term in queries that have multiple terms.
# The remainder of the equation calculates the cosine similarity
#

#
# Sort the results found in order of decreasing cosine similarity. Because we cannot use a float
# value as an index to a list, I multiplied the cosine similarity value by 10,000 and converted
# to an integer. For example i the cosine similarity was calculated to be .98970 multiplying
# it by 10,000 would produce 9897.0 and converting to an integer would result in 9897 which can be
# used as an index that we can then sort in reverse order.   To display the cosine similarity
# correctly in the results list we simply convert it back to a float value and divide by 10,000
#
keylist = resultslist.keys()

# sort in descending order
keylist.sort(reverse=True)
i = 0

# print out the top 20 most relevant documents (or as many as were found)
for key in keylist:
    i += 1
    if i > 20:
        continue
    query = "select DocumentName from documentdictionary where docid = '%d'" % (resultslist[key])
    cursor.execute(query)
    row = cursor.fetchone()
    print("Document: %s Has Relevance o %f" % (row[0], float(key) / 10000))

    connection.close()
#
# Print ending time to show the processing duration of the query.
#
endTime = time.localtime()
print('End Time: %.2d:%.2d:%.2d' % (endTime.tm_hour, endTime.tm_min, endTime.tm_sec))
