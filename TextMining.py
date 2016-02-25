"""
A collection of functions that download and perform sentiment analysis on
Jane Austen's Pride and Prejudice

author: Coleman Ellis
"""

import sys
import string
import matplotlib.pyplot as plt
from pickle import dump, load
from pattern.web import *
from pattern.en import *
from nltk import tokenize

def get_book(filename,url):
    """
    Downloads the webpage from url and writes it to filename.

    I'm using it to get books from Gutenberg, hence get_book, but I
    suppose it could download any webpage.

    >>> get_book('a.txt','http://www.gutenberg.lib.md.us/1/3/4/1342/1342.txt')
    >>> f = open('a.txt','r')
    >>> text = f.readline()
    >>> f.close()
    >>> print text[:3]
    The
    """
    text = URL(url).download()

    f = open(filename,'w')
    f.write(text)
    f.close()

def pickle_book(filename):
    """
    Stores the given text file in a pickle file with the same name as the original file
    Except with the pickle extension

    I realize this is a pretty inefficient use of pickling, but it helped me figure
    out how pickle works.

    >>> pickle_book('a.txt')
    >>> f = open('a.pickle')
    >>> text = load(f)
    >>> f.close()
    >>> print text[:3]
    The
    """
    f = open(filename,'r')
    text = f.read()
    f.close()

    #remove the .txt extension and replace with .pickle
    pickle_filename = filename[:-4] + '.pickle'
    f = open(pickle_filename,'w')
    dump(text,f)
    f.close()

def clean_pride_and_prejudice_sentences(filename = 'pride_and_prejudice_full_text.pickle'):
    """
    Given I have the copy of Pride and Prejudice available from Project Gutenberg
    (http://www.gutenberg.org/cache/epub/1342/pg1342.txt)
    downloaded and pickled, this function does the following:
    -Splits the book into a list of chapters
    -Removes beginning and end boilerplate text
    -Removes chapter numbers from beginning of chapters
    -Splits each chapter into a list of sentences

    There's a mirror available at http://www.gutenberg.lib.md.us/1/3/4/1342/1342.txt

    >>> clean_pride_and_prejudice_sentences('a.pickle')
    >>> f = open('a_clean_sentences.pickle')
    >>> text = load(f)
    >>> f.close()
    >>> print text[0][0].strip()[:5]
    It is
    """
    f = open(filename,'r')
    text = load(f)
    f.close()

    #"Chapter " only occurs at the beginning of chapters, so this is fine
    chapter_list = text.split('Chapter ')

    #Removes everything before the first real chapter
    chapter_list.pop(0)

    #Remove the ending Project Gutenberg text
    ending_index = chapter_list[-1].index('End of the Project')
    chapter_list[-1] = chapter_list[-1][:ending_index]

    #remove the chapter number from the beginning of each chapter
    chapter_list = [chapter.strip('0123456789') for chapter in chapter_list]

    #split into sentences
    chapter_list_sentences = [tokenize.sent_tokenize(chapter) for chapter in chapter_list]

    f = open(filename[:-7] + '_clean_sentences' + filename[-7:],'w')
    dump(chapter_list_sentences,f)
    f.close()

def keyword_sentiment_list(keyword = 'Mr. Darcy',filename = 'pride_and_prejudice_full_text_clean_sentences.pickle'):
    """
    Takes in a pickle filename which, when loaded, yeilds a list of lists
    where each item of the outer list is a chapter of a book and each in the
    inner list is a sentence

    Returns the average sentiment for each sentence containing a given keyword for
    each chapter in the book

    Defaults to 'Mr. Darcy' because I'm analyzing sentiment towards him

    No doctests here, this is what I'm trying to actually analyze
    """

    f = open(filename,'r')
    chapter_list_sentences = load(f)
    f.close()

    chapter_sentiments = []

    for chapter in chapter_list_sentences:
        sentences = []
        for sentence in chapter:
            #Catch both Mr. Darcy and Mr. Darcy over a linebreak
            if keyword in sentence or keyword.replace(' ','\r\n') in sentence:
                sentences.append(sentence)

                #Debugging
                # if sentiment(sentence)[0] > 0.5 or sentiment(sentence)[0] < -0.5:
                #     print sentence, str(sentiment(sentence)[0]) + "\n\n\n"

        # print len(sentences)
        if len(sentences) > 0:
            sentence_sentiments = [sentiment(sentence)[0] for sentence in sentences]
            average_sentiment   = float(sum(sentence_sentiments))/len(sentences)
        else:
            average_sentiment = 0
        chapter_sentiments.append(average_sentiment)

    return chapter_sentiments

def average_sentiment_list(filename = 'pride_and_prejudice_full_text_clean_sentences.pickle'):
    """
    Takes in a pickle filename which, when loaded, yields a list of lists
    where each item of the outer list is a chapter of a book and each in the
    inner list is a sentence

    Returns the average sentiment for each sentence for each chapter of the book as a list

    No doctests here, this is what I'm trying to actually analyze
    """

    f = open(filename, 'r')
    chapter_list_sentences = load(f)
    f.close()

    chapter_sentiments = []

    for chapter in chapter_list_sentences:
        sentiments = [sentiment(sentence)[0] for sentence in chapter]
        average_sentiment = sum(sentiments)/len(chapter_list_sentences)
        chapter_sentiments.append(average_sentiment)

    return chapter_sentiments

def sentiment_difference_plot():
    """
    Plots the difference between the average sentiment over the course of
    Pride and Prejudice and the sentiment toward Mr. Darcy

    No doctests (what could I even test here?), this is the generation
    of my results.
    """
    darcy_sentiment = keyword_sentiment_list()
    average_sentiment = average_sentiment_list()

    sentiment_difference = [darcy_sentiment[i] - average_sentiment[i] for i in range(len(darcy_sentiment))]

    plt.plot(darcy_sentiment,'r*')
    plt.xlabel("Chapters")
    plt.ylabel("Average Sentiment of Sentences containing 'Mr. Darcy'")
    plt.show()

    plt.plot(sentiment_difference,'g*')
    plt.xlabel("Chapters")
    plt.ylabel("Corrected Darcy Sentiment")
    plt.show()

if __name__ == '__main__':
    """
    Only run these as needed!
    doctests and get_book require a connection to the internet
    (and can lock you out of gutenberg if you do them too much)
    """

    # import doctest
    # doctest.testmod()
    
    #get_book('pride_and_prejudice_full_text.txt','http://www.gutenberg.org/cache/epub/1342/pg1342.txt')
    #pickle_book('pride_and_prejudice_full_text.txt')
    #clean_pride_and_prejudice_sentences()
    sentiment_difference_plot()