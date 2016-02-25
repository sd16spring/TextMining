"""
Get a sense of how the sentiment of a comment affects the sentiment of its replies.
A comment forest is imported from the JSON file. The dictionaries haved added keys that reflect their 'sentiment' (calculated by the pattern package). 
The average sentiment of a comment's replies is also calculated and displayed. 

TODO: interesting visualization and furter interpretation of the data. 
"""
import simplejson
from pattern.en import *

def assignSentiment(comment):
	"""
	Take a comment dictionary.
	Add a 'sentiment' key to the dictonary, and compute the comment's sentiment. Then recurse on replies.
	Add a 'avgReplySentiment' key to the dictionary which is the average sentiment in the replies. No replies goves an empty tuple.
	"""
	comment['sentiment'] = sentiment(comment['body']) 					# Get the current comment's sentiment
	comment['avgReplySentiment'] = ()
	if len(comment['replies']):											# If there are replies:
		avgReplySentiment = assignSentiment(comment['replies'][0])		# Initialize the average reply sentiment
		for reply in comment['replies'][1:]:
			avgReplySentiment += assignSentiment(reply)					# Loop through replies to compute the average and implicitely add sentiment to each reply's dictionary

		avgReplySentiment = ( avgReplySentiment[0]/len(comment['replies']), avgReplySentiment[1]/len(comment['replies']) )	# Normalize avgReplySentiment
		comment['avgReplySentiment'] = avgReplySentiment

	return comment['sentiment']

def generateRelationshipList(comment, relationList):
	"""
	Make a list of relationship between sentiments and avgReplySentiment according to this:

	"""
	if comment['avgReplySentiment']:
		relationList.append((comment['sentiment'], comment['avgReplySentiment']))
	else:
		relationList.append((comment['sentiment'], (0,0)))

	for reply in comment['replies']:
		generateRelationshipList(reply, relationList)

def sign(num):
	"""
	Return 1 for a positive number, 0 for 0, -1 for a negative number)
	>>> sign(-1.5)
	-1
	>>> sign(0)
	0
	>>> sign(1.5)
	1
	"""
	if num == 0:
		return 0
	if num > 0:
		return 1
	return -1

# Load Data
input_file = open('redditCommentTrees.json', 'r')
commentForest = simplejson.load(input_file)
input_file.close()

# Generate sentiment and avgReplySentiment (Data ready for process)
for baseComment in commentForest:
	assignSentiment(baseComment)
	#print baseComment['body'][:20], '...' , baseComment['sentiment'], baseComment['avgReplySentiment']

# Analyze relationship between sentiment and avgReplySentiment
#   We consider 3 cases: 
# -  0: one of the sentiments is null
# - -1: change of sign
# -  1: same sign

# Make the list
relationships = []
for baseComment in commentForest:
	generateRelationshipList(baseComment, relationships)

#print relationships[0]

# Perform analysis
results = []
for sent, avgRepSent in relationships:
	#print sent, avgRepSent, sign(sent) * sign(avgRepSent)
	results.append(sign(sent[0]) * sign(avgRepSent[0]))

# print results

hist = {}

for n in results:
	hist[n] = hist.get(n, 0) + 1

for n, f in hist.items():
	print n, f