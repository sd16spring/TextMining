"""
This project takes a formatted Facebook message dump, messages.htm, scrapes it
for the most frequent words in a message thread I specified, and then
returns a word cloud of the most popular words in the thread.

I opted out of unit tests for BeautifulSoup things because the way it does data
types is difficult and confusing.
"""
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import string
import sys


def get_msgs(filename, threadname):
    """
    This function takes a filename object that is the entire message dump
    and returns the block of messages with the thread being searched for
    """
    # read in file
    bs = BeautifulSoup(open(filename), 'lxml')
    # get to the correct thread
    block = bs.body.contents[1].div.contents[70]
    return block

def strip_msgs(msg_block):
    """
    Strips all the messages out of the block of text and removes their p tags
    """
    # get all the messages without any of the metadata
    tagged_msgs = msg_block.contents[2::2]
    # strip p tags
    msgs = [str(m)[3:-4] for m in tagged_msgs]
    # make them into a string
    return " ".join(msgs)

def strip_markov(msg_block):
    """
    Strips all the messages out of the block of text and removes their p tags, but leaves them as a list
    """
    # get all the messages without any of the metadata
    tagged_msgs = msg_block.contents[2::2]
    # strip p tags
    msgs = [str(m)[3:-4] for m in tagged_msgs]
    # add a special designator for End of Message
    return " |\n".join(msgs)

def word_cloud(text):
    """
    This function makes a wordcloud object and attempts to generate a word cloud
    using the collected messages.
    """
    wc = WordCloud()
    wc.generate(text)
    wc.to_file('test.png')

def get_freq(text):
    """
    This function makes a frequency dictionary of all of the words it's given
    """
    words = dict()
    total_words = 0
    for raw in text.split():
        total_words += 1
        word = raw.rstrip(string.punctuation).lstrip(string.punctuation).lower()
        words[word] = words.get(word, 0) + 1
    return words, total_words

def decorate_sort(dictionary):
    """
    This function takes a dictionary and sorts it, returning it as an ordered
    list of tuples of frequency-word pairs
    """
    output = [(dictionary[word], word) for word in dictionary.keys()]
    output.sort(reverse=True)
    return output

if __name__ == '__main__':
    #prompt user for input
    print 'How many words to display: '
    words = int(raw_input())
    print 'What thread to look for: '
    thread = raw_input()

    #Extract message data
    block = get_msgs('messages.htm', thread)
    text = strip_msgs(block)

    strip_markov(block)

    #try to make a word cloud
    try:
        word_cloud(text)
    except ImportError as e:
        print e
        print "Probably a libfreetype error again"

    # Generate sorted frequency list
    freq, total = get_freq(text)
    freq = decorate_sort(freq)

    print 'Of {} total words in the chat,'.format(total)
    print 'the {} most used words in our chat are: '.format(words)
    string_freq = [str(e) for e in freq]
    print "\n".join(string_freq[:words])
