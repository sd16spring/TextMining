"""
Straightup sentiment analysis on the comments as a whole
"""
from pattern.en import *
import string

file = open('redditComments.txt', 'r')

bigString = file.read()

file.close()

commentList = bigString.split('DELIM\n')

love, certainty = sentiment(commentList[0])
comCount = 1.0

for i in range(len(commentList[1:])):
	a,b = sentiment(commentList[1])
	love += a
	certainty += b
	comCount += 1

love = love/comCount
certainty = certainty/comCount

print "Sentiment analysis"
print(love, certainty)

# And now for some word frequency analysis.

hist = {}
numWords = 0.0

for comment in commentList:    											# Look at every comment
	for word in comment.split():										# Every word in that comment
		word = word.strip(string.punctuation + string.whitespace)		# Strip punctuation and whitespace
		word = word.lower()												# Make lowercase

		hist[word] = hist.get(word,0) + 1

		numWords += 1

sortedHist = []
for word, freq in hist.items():													# Generate a list of (frequency, word) tuples
	sortedHist.append( (freq, word) )

sortedHist.sort(reverse = True)

print "Top 20 most frequent"
for freq, word in sortedHist[:20]:
	print word, freq