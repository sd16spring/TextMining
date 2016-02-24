"""
YOUR HEADER COMMENT HERE
Ideas: compare word frequancy, compare tone/positivity, compare word length.


@author: Lauren Pudvan

"""
import string
from pattern.web import *
"""
TheTaleOfPeterRabbitURL = URL('http://www.gutenberg.org/cache/epub/14838/pg14838.txt').download()
TheTaleOfPeterRabbit = plaintext(TheTaleOfPeterRabbitURL)

f_TheTaleOfPeterRabbit = open('TheTaleOfPeterRabbitDownload.txt', 'w')
f_TheTaleOfPeterRabbit.write(TheTaleOfPeterRabbit.encode('UTF-8'))
f_TheTaleOfPeterRabbit.close

TheTaleOfPeterRabbitClean = open('TheTaleOfPeterRabbitDownload.txt', 'r').read()
exclude = set(string.punctuation)
TheTaleOfPeterRabbitClean = ''.join(ch for ch in TheTaleOfPeterRabbitClean if ch not in exclude)
TheTaleOfPeterRabbitClean = TheTaleOfPeterRabbitClean.lower()

FinalTheTaleOfPeterRabbit = open('TheTaleOfPeterRabbitClean.txt', 'w')
FinalTheTaleOfPeterRabbit.write(TheTaleOfPeterRabbitClean)
FinalTheTaleOfPeterRabbit.close
"""
#That was an example of how I got one of the books downloaded.
#Because Gutenberg was down I got the other two by copy and pasting them into a plain text file.


from pattern.en import *
import operator

def word_frequency(book):
    """ This goes through each word of the story and 
    if it does not exist in the dictionary it creates a key of the word and gives it a value of 1.
    If it does exist in the dictionary it increases the value by 1. 
    Then it sorts the dictionary from lovest to highest values (words that occure most are at the end)
    Then it returns the dictionary.
    >>> word_frequency('DocTesting.txt')
    [('a', 1), ('used', 1), ('for', 1), ('This', 1), ('doc', 1), ('is', 1), ('testing', 1)]
    """
    f = open(book,'r')
    wordcount={}
    for word in f.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    f.close();
    sorted_wordcount = sorted(wordcount.items(), key=operator.itemgetter(1))
    return sorted_wordcount

def average_word_length(book):
    """ This will append a list with the length of each word then take the avarage of the list.
    This gives the average word length.
    >>> average_word_length('DocTesting.txt')
    3.4285714285714284
    """
    f = open(book,'r')
    wordLenths = []
    for word in f.read().split():
        length = len(word)
        wordLenths.append(length)
    f.close();
    return sum(wordLenths) / float(len(wordLenths))

def tone(book):
    """ This takes in a string and returns (positive sentiment polarity)
    I do not know how to predict a doctest for this because i do not know the specifics for how to predict the result of sentiment.
    """
    b = open(book,'r')
    b.read()
    sent = sentiment(file)
    b.close()
    return sent[0]


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

print word_frequency('TheVeryHungryCatipillar.txt')
print average_word_length('TheVeryHungryCatipillar.txt')
print tone('TheVeryHungryCatipillar.txt')
print word_frequency('TheGivingTree.txt')
print average_word_length('TheGivingTree.txt')
print tone('TheGivingTree.txt')
print word_frequency('TheTaleOfPeterRabbitClean.txt')
print average_word_length('TheTaleOfPeterRabbitClean.txt')
print tone('TheTaleOfPeterRabbitClean.txt')


