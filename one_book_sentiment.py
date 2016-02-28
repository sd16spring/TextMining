from pattern.en import *
from os.path import exists
import pickle
import plotly.plotly as plot
import plotly.graph_objs as maketrace
import pandas

def plot_storyline(book_file_name, plot_name='test-plot'):
	''' Plots sentiment (-1 to 1) of book text using rolling window of 5 (default) sentences.
		Input: book_file_name, ie 'Clotelle.txt'
		Commented output: a sentiment plot over the length of the book.
		Modified output: x (0 to 1000) and y (sentiment scores)'''

	listAndCoeff= sliding_window_sentiment(book_file_name) #implied windowsize of 6, which then gets scaled based on size of book
	sentiment_list = listAndCoeff[0]
	scaling_coeff = listAndCoeff[1] #Used in sliding_window_sentiment for window size; now used for rolling mean calc
	
	sentiment_series = pandas.Series(sentiment_list)

	roll_mean_sentiment = pandas.rolling_mean(sentiment_series,80*scaling_coeff) #Smoothes out sentiment data

	x = scale_xrange(range(len(roll_mean_sentiment))) #scales the length of roll_mean_sentiment to a standard (1001)
	y = roll_mean_sentiment
	return [x,y]

	##TO PLOT JUST ONE BOOK COMMENT OUT 'return' LINE AND UNCOMMENT BELOW:
	# trace = maketrace.Scatter( x = range(len(roll_mean_sentiment)), y = roll_mean_sentiment)
	# data = [trace]
	# plot.iplot(data, filename = plot_name)
	## it works!!!

def scale_xrange(xrange):
	''' Returns a range of same number of points that spans from 0 to 1000 regardless of input values
		Input: xrange, ie [0,1,2]
		Output: scaled xrange, ie [0,500,1000]'''
	new_range = []
	for index in xrange:
		new_range.append((1000.0/xrange[-1]) * index)
	return new_range


def sliding_window_sentiment(book_file_name, windowSize = 8):
	''' This does a couple things.
		It gets the list of sentences in the book by calling list_of_all_sentences.
		It calculates a 'scaling coefficient' that makes the window size bigger for a particularly long book.
		Then it looks at sentences in the window, calculates sentiment and puts it in sentiment_list,
		then jumps forward one sentence and looks at the new window.

		Inputs: book file name so it can call the list of all sentences function, and the default windowsize.
		Outputs: a list of the sentiment score for every window and the scaling coefficient.'''

	sentenceList = list_of_all_sentences(book_file_name)
	scaling_coeff = len(sentenceList)//900 #Based on Our Nig, shortest book
	windowSize = scaling_coeff * windowSize

	sentiment_list = []

	for i in range(len(sentenceList) - (windowSize-1)):
		mySentences = sentenceList[i : i+windowSize]
		mySentences = '. '.join(mySentences)
		sentiment_list.append(measure_sentiment(mySentences))

	return [sentiment_list, scaling_coeff]


def list_of_all_sentences(book_file_name):
	''' Pass in the name of the book file (ie 'Clotelle.txt')
		Returns: sequential list of every sentence in the book
		If it's already pickled that list, this function just unpickles it and passes it out
		If it hasn't pickled it yet, it stores a pickled version of the list for the future
		but still passes out the unpickled one.
	>>> list_of_all_sentences('example.txt')
	['Hello', 'It's me', 'I was wondering if after all these years you'd like to meet', 'Hello', 'How aaare you.\n']
	'''

	book_name = book_file_name[:-4] #take off .txt
	pickled_book_name = ('%s' + '_pickled_sentence_list.txt') %(book_name)
	if exists(pickled_book_name):
		f = open(pickled_book_name,'r')
		pickled_sentence_list = f.read()
		f.close()
		sentence_list = pickle.loads(pickled_sentence_list)
		return sentence_list
	else:
		#First, make a sequential list of every sentence in the book
		f = open(book_file_name, 'r')
		book_text = f.read()
		f.close()
		sentence_list = book_text.split('. ') #This is what we will return, but first should pickle it for future use
		f2 = open(pickled_book_name,'w')
		pickled_sentence_list = pickle.dumps(sentence_list)
		f2.write(pickled_sentence_list)
		f2.close()
		return sentence_list


def measure_sentiment(sentences):
	''' Returns the sentiment, from -1 (very negative) to 1 (positive), of a string
		The string should be one sentence from the story.'''
	(sentim, subjectivity) = sentiment(sentences)
	return sentim
