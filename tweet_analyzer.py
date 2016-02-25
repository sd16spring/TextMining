"""Determines the sentiment of tweets for given weather conditions and plots them on a scatter plot"""
import pickle
from pattern.en import *
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

f = open('weather2.pickle', 'r')
dictionary = pickle.load(f)
print dictionary.keys()

# removes hashtag from text of tweet as not to impact sentiment analysis

tweet_dictionary = {}
for hashtag in dictionary.keys():
	tweet_dictionary[hashtag] = []

	for tweet in dictionary[hashtag]:
		tweet.replace(hashtag, '')
		tweet_dictionary[hashtag].append(tweet)

# determines positivity and subjectivity of tweets

tone_dictionary = {}
print "tweet dictionary keys:", tweet_dictionary.keys()
for hashtag in tweet_dictionary.keys():

	positivity_list = []
	subjectivity_list = []
	sentiment_tuple = (positivity_list, subjectivity_list)
	print "sentiment tuple:", sentiment_tuple

	for tweet in tweet_dictionary[hashtag]:
		positivity_list.append(sentiment(tweet)[0])
		subjectivity_list.append(sentiment(tweet)[1])

	tone_dictionary[hashtag] = sentiment_tuple

# creates scatter plot displaying positivity and subjectivity of tweets for given weather conditions as well as the average

fig, axes = plt.subplots(nrows = 1, ncols = 6, figsize = (15,5), sharey = 'row')

# for debugging purposes... Am I actually getting all of the tweets?
print "tone dictionary:", tone_dictionary
print "tone dictionary length:", len(tone_dictionary["#rain"][0])

# calculates average positivity and subjectivity
snow_avg_pos = sum(tone_dictionary["#snow"][0])/len(tone_dictionary["#snow"][0])
snow_avg_sub = sum(tone_dictionary["#snow"][1])/len(tone_dictionary["#snow"][1])

# plots data on subplot of the figure
axes[0].scatter(snow_avg_sub, snow_avg_pos, c='k')
axes[0].scatter(tone_dictionary["#snow"][1], tone_dictionary["#snow"][0], c = '#cab5d8')
axes[0].set_title('#snow')

rain_avg_pos = sum(tone_dictionary["#rain"][0])/len(tone_dictionary["#rain"][0])
rain_avg_sub = sum(tone_dictionary["#rain"][1])/len(tone_dictionary["#rain"][1])

axes[1].scatter(rain_avg_sub, rain_avg_pos, c='k')
axes[1].scatter(tone_dictionary["#rain"][1], tone_dictionary["#rain"][0], c = '#b0e0e6')
axes[1].set_title('#rain')

sun_avg_pos = sum(tone_dictionary["#sun"][0])/len(tone_dictionary["#sun"][0])
sun_avg_sub = sum(tone_dictionary["#sun"][1])/len(tone_dictionary["#sun"][1])

axes[2].scatter(sun_avg_sub, sun_avg_pos, c='k')
axes[2].scatter(tone_dictionary["#sun"][1], tone_dictionary["#sun"][0], c = '#ffec99')
axes[2].set_title('#sun')

blizzard_avg_pos = sum(tone_dictionary["#blizzard"][0])/len(tone_dictionary["#blizzard"][0])
blizzard_avg_sub = sum(tone_dictionary["#blizzard"][1])/len(tone_dictionary["#blizzard"][1])

axes[4].scatter(blizzard_avg_sub, blizzard_avg_pos, c='k')
axes[4].scatter(tone_dictionary["#blizzard"][1], tone_dictionary["#blizzard"][0], c = '#4c4c70')
axes[4].set_title('#blizzard')

cloudy_avg_pos = sum(tone_dictionary["#cloudy"][0])/len(tone_dictionary["#cloudy"][0])
cloudy_avg_sub = sum(tone_dictionary["#cloudy"][1])/len(tone_dictionary["#cloudy"][1])

axes[3].scatter(cloudy_avg_sub, cloudy_avg_pos, c='k')
axes[3].scatter(tone_dictionary["#cloudy"][1], tone_dictionary["#cloudy"][0], c = '#95aeab')
axes[3].set_title('#cloudy')

# plots averages on final subplot
axes[5].scatter(snow_avg_sub, snow_avg_pos, s=80, c='#cab5d8')
axes[5].scatter(rain_avg_sub, rain_avg_pos, s=80, c='#b0e0e6')
axes[5].scatter(sun_avg_sub, sun_avg_pos, s=80, c='#ffec99')
axes[5].scatter(cloudy_avg_sub, cloudy_avg_pos, s=80, c='#95aeab')
axes[5].scatter(blizzard_avg_sub, blizzard_avg_pos, s=80, c='#4c4c70')
axes[5].set_title('Average')
	
# creates gird and exis labels
for ax in axes:
	ax.yaxis.grid(True)
	ax.set_xlabel('Subjectivity')
	ax.set_ylabel('Positivity')

plt.show()