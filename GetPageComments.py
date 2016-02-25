"""
Parse comments in: 3xad6j
and store them in a file
""" 
import praw

r = praw.Reddit('Comment Scraper 1.0 by u/TheMattgican') # initialize PRAW

submissions = r.get_submission(submission_id='3zad6j')  # get submissions


# Get Flat Comments in a File
flat_comments = praw.helpers.flatten_tree(submissions.comments)	# Get all comments as an unordered list

file = open('redditComments.txt', 'w')

for comment in flat_comments:
	if type(comment) != praw.objects.MoreComments:
		file.write(comment.body + 'DELIM\n')

file.close()



import json

def makeCommentObject(comment):

	someReplies = filter(lambda reply: type(reply) != praw.objects.MoreComments, comment.replies)
	commentDict = {
	'body':			comment.body,
	'replies': 		[ makeCommentObject(reply) for reply in someReplies ]
	}
	return commentDict

commentTrees = submissions.comments
baseComments = []

for baseComment in commentTrees:
	if type(baseComment) != praw.objects.MoreComments:
		baseComments.append(makeCommentObject(baseComment))

file = open('redditCommentTrees.json', 'w')
file.write(json.dumps(baseComments))
file.close()