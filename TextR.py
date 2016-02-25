from pattern.web import *
import pickle

w = Wikipedia()
article = []
title = []
for article_title in w.index():
	temp_article = w.search(article_title)
	article.append(temp_article.string)
	title.append(article_title)
a = open('WikiArticle','w')
pickle.dump(article,a)
a.close()

b = open('Article_title','w')
pickle.dump(title,b)
b.close()

