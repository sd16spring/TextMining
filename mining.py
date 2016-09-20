from os.path import exists
import sys
from pickle import dump, load
import string
import csv

def loadFile(fileName):
	""" 
		Takes raw data from project Gutenberg and cuts out the introduction and bottom part
		It also tranfers the entire text to lowercase and removes punctuation

		Returns a String

	>>> s = 'A***H   ***1234@&().ABCabc***'
	>>> f = open('text.txt', 'w')
	>>> dump(s, f)
	>>> f.close()
	>>> loadFile('text.txt')
	'abcabc'
	"""
	inputFile = open(fileName, 'r')
	text = load(inputFile)

	l = text.split('***') #marker for stop and end of text in gutenberg
	try: #returns none in case there is something strange with the project gutenberg text
		mainText = l[2] #main text is the third block of text 
	except:
		return None
	mainText = mainText.lower() #changes everything to lowercase
	mainText = mainText.replace("\r\n", "")
	mainText = mainText.translate(string.maketrans("",""), string.punctuation) #removes punctuation
	mainText = mainText.translate(string.maketrans("",""), string.digits) #removes numbers
	return mainText

def histogram(fileName):
	"""
		Input is a textFile
		Creates a word count
		Returns a dictionary

	>>> s = 'A***B***hello hello hello'
	>>> f = open('text.txt', 'w')
	>>> dump(s, f)
	>>> f.close()
	>>> histogram('text.txt')
	{'hello': 3}
	"""
	mainText = loadFile(fileName)
	d = dict()
	l = mainText.split(" ")
	for word in l:
		if word != "": #gets rid of all of the empty strings in the list of words
			d[word] = d.get(word, 0)
			d[word] += 1
	return d 

def mostFrequent(fileName):
	"""
		Takes a file name
		Returns a list with words sorted by frequency (high to low)
	>>> s = 'A***B***hello hello hello 12 bye bye small'
	>>> f = open('text.txt', 'w')
	>>> dump(s, f)
	>>> f.close()
	>>> mostFrequent('text.txt')
	[(3, 'hello'), (2, 'bye'), (1, 'small')]
	"""
	d = histogram(fileName)

	l = []
	for i in d:
		l.append((d[i], i))
	l.sort(reverse = True)
	return l

if __name__ == '__main__':
	# import doctest
	# doctest.testmod()
	l1 = mostFrequent('odyssey.txt')
	l2 = mostFrequent('peter_pan.txt')
	l3 = mostFrequent('wizard_of_oz.txt')
	l4 = mostFrequent('frankenstein_text.txt')

	num1 = []
	num2 = []
	num3 = []
	num4 = []
	for i in range(len(l1)):
		num1.append(l1[i][0])
	for i in range(len(l2)):
		num2.append(l2[i][0])
	for i in range(len(l3)):
		num3.append(l3[i][0])
	for i in range(len(l4)):
		num4.append(l4[i][0])


	myfile1 = open('odyssey_data.csv', 'wb')
	wr1 = csv.writer(myfile1)
	wr1.writerow(num1)
	myfile2 = open('peter_pan_data.csv', 'wb')
	wr2 = csv.writer(myfile2)
	wr2.writerow(num2)
	myfile3 = open('wizard_of_oz_data.csv', 'wb')
	wr3 = csv.writer(myfile3)
	wr3.writerow(num3)
	myfile4 = open('frankenstein_data.csv', 'wb')
	wr4 = csv.writer(myfile4)
	wr4.writerow(num4)
