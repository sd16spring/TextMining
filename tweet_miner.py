from pattern.en import *
from pattern.web import Twitter
import pickle
MY_LICENSE = ('WgRmLC6IAhx27bRIG54ngxaRp', 'ldjhjaWF2G6jtPlg3mudc1IZV0V7PN7YZaSjuDqlw7QpvwF7ra', ('700461301575905284-PMu8wIBN2Qt1dW2T1nrytKjC0GYPgF3', 'OszrgU2gVUyBuNAmQc70CAARcpbqvu26DKwEKE0lAQ1ZG'))

# creates dictionary with weather conditions (ex. #snow) as keys and a list of 1000 tweet strings as the value

dictionary = {}
weather_conditions = ['#snow', '#rain', '#cold', '#storm', "#blizzard", '#sun', '#warm', '#drizzle', '#cloudy']
t = Twitter(license = MY_LICENSE)

for hashtag in weather_conditions:
	dictionary[hashtag] = []
	for tweet in t.search(hashtag, start = None, count = 1000):
		dictionary[hashtag].append(tweet.text)

# pickles the tweet dictionary

f = open('weather2.pickle', 'w')
pickle.dump(dictionary, f)
f.close()