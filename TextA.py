from pattern.en import *
import pickle
Wiki = open('WikiArticle','r')
titles = open('Article_title','r')
article = pickle.load(Wiki)
title = pickle.load(titles)
s = 0
count = 0
subjective = []
subjectiveArticles = []
for string in article:
	t = sentiment(string)
	s += t[1]
	if t[1]>0.5:
		subjectiveArticles.append(article[count])
		print title[count]
		print t[1]
	count += 1
Wiki_subjectivity = s/len(article)
print Wiki_subjectivity




