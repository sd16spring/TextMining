from pattern.en import *
import matplotlib.pyplot as plt
import numpy as np
from pattern.web import Twitter

def search_twitter(o):
	""" Given a list of strings to use as search terms, this function 
	searches Twitter and pulls the x most recent tweets related to each
	search term. It finds the polarity of each tweet, averages the
	polarities of the tweets for each search term, and returns the
	average polarity of each string in the list in the form of a list.
	"""
	candidates = []
	tw = Twitter()
	i = None
	l = 0 #the list indice for polarity values list
	for j in o: #runs through each candidate on the list
		sum_of_polarities = (len(o))*[0]
		polarity_average = (len(o))*[0]
		d = [] #create list of tweets so we know the len()of the tweets to divide the sum by
		for tweet in tw.search(j, start = i, count = 42):
			p = tweet.text.encode("utf-8") #assigns tweet as a value to p
			d.append(p) #adds each tweet to a list
			polarity = sentiment(p) #finds polarity and subjectivity of tweet
			sum_of_polarities[l] += polarity[0] #adds polarity to sum of polarities
			i = tweet.id
		polarity_average[l] = sum_of_polarities[l]/(len(d)) #finds average polarity
		candidates.append(polarity_average[l])
		#print j,polarity_average[l]
		#print
		l += 1 #next candidate gets a different list indice
	return candidates

def plot_polarity(o):
	"""This function plots the results of the search_twitter function in
	the form of a bar graph. The x-axis is the list items and the y-axis
	is the polarity of each list item on Twitter.
	"""
	polarity = search_twitter(o) #calls search_twitter function
	objects = o
	y_pos = np.arange(len(objects))
	plt.bar(y_pos,polarity,align = 'center',alpha = .5)
	plt.xticks(y_pos,objects)
	plt.ylabel('Polarity')
	plt.title('Tweet Polarity of Presidential Candidates')
	plt.show()

plot_polarity(['Hillary','Bernie',"O'Malley",'Trump','Cruz','Rubio','Kasich'])
