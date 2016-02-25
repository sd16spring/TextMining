from pattern.web import *
from pattern.en import *
from math import *

def search(x):
	'''This function allows you to imput a keyword to search for on twitter, and outputs a list of the last ten tweets 
	with that keyword. I have this set at only 10 tweets because Twitter kicks me out if I surpass 600 tweets/hour, and I 
	often run the function a considerable amount of times in one hour.
	'''
	t = Twitter()
	tweets = []
	i = None
	for j in range(2):
	    for tweet in t.search(x, start=i, count=5):
	        # print tweet.text
	        tweets.append(tweet.text.encode("utf-8"))
	        i = tweet.id
	return tweets
# print search('#Scalia')

def measure_sentiment(x):
	''' This function takes the keyword as the input, uses the search function to get the latest tweets with that keyword,
	and returns that average polarity of all of the tweets the search function returned. This function is also programmed to
	ignore any tweets that have a subjectivity grading of greater than 0.5. This is an attempt to filter out tweets that
	are not factual in attempt to make the results of this investigation provide more accurate March Madness predictions.
 	are being used to judge predictions for
	'''
	sum_pol = 0
	tweets = search(x)
	total_tweets = 0
	if len(tweets) == 0:
		return 0
	else:
		for i in tweets:
			polarity = sentiment(i)
			if polarity[1] > .5:
				return 0
			else:
				sum_pol += polarity[0]
				total_tweets += 1
		polarity_average = sum_pol/total_tweets
		return polarity_average

def which_is_bigger(x,y):

	'''This function was used as a part of Tweeter, the website I created with Mary Keenan during WHACK this past weekend, 
	that took two inputs of keywords or hashtags and returned strings that stated which input had a higher polarity
	and by how much. I did not use this function for the March Madness predictions.
	'''

	input1 = measure_sentiment(x)
	input2 = measure_sentiment(y)
	diff = input1 - input2
	if (input1 - input2) < -0.15 or (input1 - input2) < 0.15: 	#or abs(diff) < 0.15:
		return "People are almost equally positive about %s and %s." % (x, y)
	elif input1 > input2:
		if (input1 - input2) <= .3:
			return "People are slightly more positive about %s than %s."  % (x, y)
		elif (input1 - input2) >= .7:
			return "People are significantly more positive about %s than %s."  % (x, y)
		else:
			return "People are more positive about %s than %s."  % (x, y)
	else:
		if (input2 - input1) <= .3:
			return "People are slightly more positive about %s than %s." % (y, x)
		elif (input1 - input2) >= .7:
			return "People are significantly more positive about %s than %s."  % (y, x)
		else:
			return "People are more positive about %s than %s." % (y, x)
# print which_is_bigger("Bernie", "Hillary")


def MMPredictions(x,y,z,a,b,c,d,e,f,g):

	"""
	This function allows user to input teams of interest for the NCAA tournament and returns a horizontal bar chart with the teams listed from most positive
	Twitter activity (top bar) too least positive (bottom bar). This function can be applied to many situations other than March Madness predictions and 
	still provide meaningful results. Examples: Presidential Candidates, NFL Combine Prospects, Oscar Nominations, etc.
	"""
	import matplotlib.pyplot as plt
	plt.rcdefaults()
	import numpy as np
	import matplotlib.pyplot as plt

	input1 = measure_sentiment(x)	
	input2 = measure_sentiment(y)
	input3 = measure_sentiment(z)
	input4 = measure_sentiment(a)
	input5 = measure_sentiment(b)
	input6 = measure_sentiment(c)
	input7 = measure_sentiment(d)
	input8 = measure_sentiment(e)
	input9 = measure_sentiment(f)
	input10 = measure_sentiment(g)
	polarities = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
	arguments = [x,y,z,a,b,c,d,e,f,g]

# zip both lists into one tuple to be sorted

	zipped = zip(polarities, arguments)
	zipped.sort()

	# Example data
	people = [i[1] for i in zipped]
	y_pos = np.arange(10)
	Polarity = [i[0] for i in zipped]
	

	plt.barh(y_pos, Polarity, align='center', alpha=0.4)
	plt.yticks(y_pos, people)
	plt.xlabel('Polarity')
	plt.title('NCAA Bracket Predictions: Who Will Make it to March Madness?')

	plt.show()

MMPredictions('Virginia Cavaliers', 'Purdue Boilermakers','Syracruse Orange', 'Michigan Spartans','Kansas Jayhawks', 'Miami Hurricanes', 'Villanova Wildcats', 'Oklahoma Sooners', 'Xavier Musketeers', 'Oregon Ducks')