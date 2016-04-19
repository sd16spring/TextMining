from pattern.web import *
import os
import pickle
import anydbm

# w = Wikipedia()
# for article_title in w.index():
# 	try:
# 		print article_title
# 	except UnicodeEncodeError:
# 		pass
# w = Wikipedia()
# olin_article = w.search('Olin College')
# print olin_article.s
import praw
r = praw.Reddit(user_agent='my_cool_application')
submissions = r.get_subreddit('opensource').get_hot(limit=5)
print[ str(x) for x in submissions]
