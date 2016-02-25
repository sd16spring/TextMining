"""
This project takes a formatted Facebook message dump, messages.htm, scrapes it
for the most frequent words in a message thread I specified, and then
returns a word cloud of the most popular words in the thread.
"""
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import string

# read in messages.htm
bs = BeautifulSoup(open('messages.htm'), 'lxml')
# get to the correct thread
def get_msgs(beautifulsoup):
    content = bs.body.contents[1].div.contents[70]
    # get all the messages without any of the metadata
    tagged_msgs = content.contents[2::2]
    # strip p tags
    msgs = [str(m)[3:-4] for m in tagged_msgs]
    # make them into a string
    return " ".join(msgs)

def word_cloud(text):
    """
    This function makes a word_cloud object and 
    """
    wc = WordCloud()
    wc.generate(text)

#assemble a frequency list
words = dict()
for raw in str_msgs.split():
     word = raw.rstrip(string.punctuation).lstrip(string.punctuation).lower()
     words[word] = words.get(word, 0) + 1

output = [(words[word], word) for word in words.keys()]
output.sort(reverse=True)

# print(str(len(output)) + " different fucking words.")
# print("\n".join([str(e) for e in output]))
