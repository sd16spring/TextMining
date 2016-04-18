from pattern.web import *
import pickle
f = open('dickens_texts.pickle','r')
books = pickle.load(f)
f.close()

# URL('http://www.gutenberg.org/ebooks/1400.txt.utf-8').download(), URL('http://www.gutenberg.org/ebooks/1289.txt.utf-8').download(), URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download(), 	URL('http://www.gutenberg.org/ebooks/786.txt.utf-8').download()

books.extend([URL('http://www.gutenberg.org/ebooks/786.txt.utf-8').download()])
f = open('dickens_texts.pickle','w')
pickle.dump(books, f)
f.close()

