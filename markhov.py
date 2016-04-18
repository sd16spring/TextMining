"""Ignore quotation marks
"""
import random
import pickle
input_file = open('dickens_texts.pickle','r')
books = pickle.load(input_file)
punctuation = ['.', ',', '?', '!', ':', ';', '']
order = 2
suffix_dict = {}
for book in books:
	text = book.strip()
	words = text.split(' ')												#divide it by spaces

	for k in range(len(words)):
		words[k] = words[k].replace('"', '')
		words[k] = words[k].replace("'", "")

	i = 0																
	while i < len(words):												#separate out the punctuation
		if len(words[i])>0:
			last = words[i][len(words[i])-1]
			if last in punctuation:
				words[i] = words[i][:len(words[i])-1]
				words.insert(i+1, last)
				i+=1
		i+=1

	for i in range(order):												#iterate through the different starting positions, create a dictionary of prefixs and the suffixes
		for k in range(i, len(words)-order, order):						#go through each set of order words starting at i
			prefix = ' '.join(words[k:k+order])
			suffix = words[k+order]
			if prefix not in suffix_dict:
				suffix_dict[prefix] = [suffix]
			else:
				suffix_dict[prefix].append(suffix)

f = open('dictionary.pickle', 'w')
pickle.dump(suffix_dict, f)
f.close()