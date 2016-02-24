from pattern.web import *
import pickle


def countMadeUpWordsIn(book, realDict, fakeDict):
	startOfWord = book.index('***\n')+5
	reading = False
	for i in range(startOfWord,len(book)-4):
		if isLetter(book[i]):	# if there is a letter here, keep reading
			reading = True
		elif reading:			# if there is a punctuation but was recently a letter, check to see if you've found a word
			wordCandidate = book[startOfWord:i]
			if not realDict.has_key(wordCandidate):	# if it is not a real word
				fakeDict[wordCandidate] = fakeDict.get(wordCandidate,0)+1	# record it
		elif book[i:i+3] == '***':
			break


title = "insert title here"
book = URL('http://www.gutenberg.org/ebooks/*****').download()
input_file = open('fiction','r')
booksDict = pickle.load(input_file)
input_file.close()

numFic = countMadeUpWordsIn(book)
booksDict[title] = numFic

f = open('fiction','w')
pickle.dumps(booksDict,f)
f.close()