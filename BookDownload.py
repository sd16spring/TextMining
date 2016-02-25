""" This script downloads all of the books I'm going to be looking at for
    this mini project
    The books, beginning in year 1900 and going by 3 years, are as follows:
    0. To have and Hold
    1. The Call of the Wild
    2. The jungle
    3. The Promise of American Life
    4. The just and the unjust
    5. The turmoil
    6. The Major
    7. Main Street
    8. Plastic Age

    @author: Jonathan Jacobs

"""

import pickle
from pattern.web import *


# dictionary of books and their url on gutenburg.org

books = {'toHaveAndHold': 'http://www.gutenberg.org/ebooks/2807.txt.utf-8',
         'theCallOfTheWild': 'http://www.gutenberg.org/ebooks/215.txt.utf-8',
         'theJungle': 'http://www.gutenberg.org/ebooks/140.txt.utf-8',
         'thePromiseOfAmericanLife': 'http://www.gutenberg.org/ebooks/14422.txt.utf-8',
         'theJustandtheUnjust': 'http://www.gutenberg.org/ebooks/14581.txt.utf-8',
         'theTurmoil': 'http://www.gutenberg.org/ebooks/1098.txt.utf-8',
         'theMajor': 'http://www.gutenberg.org/ebooks/3249.txt.utf-8',
         'MainStreet': 'http://www.gutenberg.org/ebooks/543.txt.utf-8',
         'PlasticAge': 'http://www.gutenberg.org/ebooks/16532.txt.utf-8'}

# downloading all of the books from gutenburg

downloadedBooks = {}


def bookDownload(bookList):
    for book in bookList:
        downloadedBooks[book] = download(bookList[book])

    saveBooks(downloadedBooks)


# saves all of the books on the hard dive


def saveBooks(texts):
        f = open('gutenburgTexts', 'w')
        pickle.dump(texts, f)
        f.close()


if __name__ == '__main__':
    bookDownload(books)
