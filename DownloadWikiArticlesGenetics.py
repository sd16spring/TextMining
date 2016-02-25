import pickle 

from pattern.web import *
w = Wikipedia()


search_terms = ['cloning', 'genetic engineering', 'gene therapy', 'CRISPR', 'genetically modified organisms', 'genetics', 'conservation genetics']

for element in search_terms: 
	article = w.search(element)
	print article.sections

	with open(element +'.txt', 'w') as f:
		f.write(article.plaintext().encode('UTF-8'))