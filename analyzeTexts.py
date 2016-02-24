
""" Analyses the texts downloaded from project gutenburg

    @author: Jonathan Jacobs
"""


import pickle
import string
import re
from pattern.en import *

# load the pickled files and test to see if they work

input_file = open('gutenburgTexts', 'r')
gutenTexts = pickle.load(input_file)


wordFreq = {}
sentimentOfBooks = {}


# runs the two things I want to see about the books
def analysis(books):
    for text in books:
        # sentimentOfBooks[text] = analyzeSentiment(books[text])
        wordFreq[text] = findWordFrequency(books[text])

    wordList = []
    temp = []
    # keeps track of the order of the titles in the sorted list
    order = []

    # puts wordFreq into a sorted list
    i = 0
    for name in wordFreq:
        order.append(name)
        temp = wordFreq[name].items()

        # reverses the key, value tuple thing
        for j in range(len(temp)):
            anotherTemp = temp[j][1], temp[j][0]
            temp[j] = anotherTemp

        # reverse sorts the list and adds it to the sorted list
        temp.sort(reverse=True)
        wordList.append(temp)
        i += 1

    # writes all of the word frequency lists with appropriate titles
    for k in range(len(order)):
        newFile = open(order[k] + '--Word_Frequency.txt', 'w')
        newFile.write(str(wordList[k]))
        newFile.close()

    # savedFile = open('results.txt', 'w')
    # savedFile.write(str(sentimentOfBooks))
    # savedFile.close()


# uses pattern to analyze the sentiments of the texts
def analyzeSentiment(book):
    num = 0.0
    polarity = 0.0
    subjectivity = 0.0
    textToAnalyze = re.split('[?!.]', book)
    temporaryVar = ()
    for line in textToAnalyze:
        if line != '':
            num += 1
            temporaryVar = sentiment(line)
            polarity += float(temporaryVar[0])
            subjectivity += float(temporaryVar[1])
    return (polarity/num, subjectivity/num)


# finds the frequency of words throught the entire book
def findWordFrequency(book):
    wordHolder = ''
    temp = {}
    text_file = open('temporay.txt', 'w')
    text_file.write(book)
    text_file.close()
    f = open('temporay.txt', 'r')

    for line in f:
        for word in line.split():
            wordHolder = word
            wordHolder = wordHolder.strip(string.punctuation)
            wordHolder = wordHolder.strip(string.whitespace)
            wordHolder = wordHolder.lower()
            temp[wordHolder] = temp.get(wordHolder, 0) + 1
    f.close()
    return temp


if __name__ == '__main__':
    analysis(gutenTexts)
