from pattern.web import *
from pattern.en import *
from string import *
import pickle
import matplotlib.pyplot as plt

""" when you're downloading the urls
url1 = URL('https://sherlock-holm.es/stories/plain-text/stud.txt')
url2 = URL('https://sherlock-holm.es/stories/plain-text/houn.txt')
url3 = URL('https://sherlock-holm.es/stories/plain-text/sign.txt')
url4 = URL('https://sherlock-holm.es/stories/plain-text/vall.txt')

study_scarlet = plaintext(url1.download())
hound_baskervilles = plaintext(url2.download())
sign_four = plaintext(url3.download())
valley_fear = plaintext(url4.download())



f1 = open('AStudyInScarlet', 'w')
f1.write(study_scarlet.encode("UTF-8"))
f1.close()


f2 = open('TheHoundoftheBaskervilles', 'w')
f2.write(hound_baskervilles.encode("UTF-8"))
f2.close()

f3 = open('TheSignoftheFour', 'w')
f3.write(sign_four.encode("UTF-8"))
f3.close()

f4 = open('TheValleyofFear', 'w')
f4.write(valley_fear.encode("UTF-8"))
f4.close()
"""

f1 = open('AStudyInScarlet', 'r')
f2 = open('TheHoundoftheBaskervilles', 'r')
f3 = open('TheSignoftheFour', 'r')
f4 = open('TheValleyofFear', 'r')
list_books = ['AStudyInScarlet', 'TheHoundoftheBaskervilles', 'TheSignoftheFour', 'TheValleyofFear']
list_files_books = [f1, f2, f3, f4]


def make_book(bookf, title):
	"""This function takes the book file and the book title and breaks the book into chapters, /
	storing each chapter in a list. It then stores these lists in a pickle dump"""
	book = []
	for line in bookf:
		if '----------' in line:
			break
		elif len(line) >= 4:
			book.append(line.strip("\n"))
	real_book = book[30:]
	#print real_book
	chap_begin = 0
	chapter_list = []
	list_line = []
	for i,line in enumerate(real_book):
		if "CHAPTER" in line:
			chapter_list.append(list_line)
			list_line = []
		list_line.append(line)
#		print chapter_list
	pickle.dump( chapter_list, open(str(title) + ".pkl", "wb"))

def sentiment_of(title):
	"""This function takes in the title of the novel and then loads the pickled file that was
	stored in the make_book function. It then runs sentiment analysis on that"""
	sentiment_list = []
	book = pickle.load( open(str(title) + ".pkl", "rb"))
	for chapter in book:
		#for i in range(0, len(chapter), 50):
		feels = sentiment(''.join(chapter)) 
		sentiment_list.append(feels)
	return sentiment_list

#	for elem in chapter_list

def compiler():
	"""This function calls the make_book function and then calls the sentiment_of function for each novel.
	It then stores that sentiment in a list. """
	real_feels = [[],[],[],[]]
	for i,book in enumerate(list_books):
		make_book(list_files_books[i], list_books[i])
		for pair in sentiment_of(list_books[i]):
			real_feels[i].append(pair[0])
	return real_feels

def values():
	"""This function calls the plot_values funtion for each sentiment that the compiler funciton returns """
	sentiment_lists = compiler()
	#for num in sentiment_lists:
	plot_values(sentiment_lists[3])


def plot_values(y):
	"""This function plots a line for each of the novel's sentiment. It also makes it so that each of the
	 lines is spread out over the same range of values"""
	x = []
	for element in range(len(y)):
		x_val = (536 / float(len(y)-1))*element
		x.append(x_val)
	print 
	axes = plt.gca()
	axes.set_xlim([0, 536])
	axes.set_ylim([-0.02, .2])
	plt.plot(x, y)
	plt.ylabel('Sentiment')
	plt.xlabel('Relative Location in Novel')
	plt.show()

if __name__ == '__main__':
	values()