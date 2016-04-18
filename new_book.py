import random
import pickle

f = open('dictionary.pickle', 'r')
suffix_dict = pickle.load(f)
punctuation = ['.', ',', '?', '!', ':', ';', '']
order = 2
depth = 10000
prefix = random.choice(suffix_dict.keys())

new_text = prefix.split(' ')
for i in range(depth):
	if prefix not in suffix_dict.keys():
		prefix = random.choice(suffix_dict.keys())
	suffix = random.choice(suffix_dict[prefix])
	new_text.append(suffix)
	prefix = prefix.split(' ')[order-1] + ' ' + suffix

finished_work = []
for i in range(len(new_text)):
	if new_text[i] in punctuation:
		if i ==0 or finished_work[i-1] in punctuation:
			finished_work.append('')
		else:
			finished_work.append(new_text[i])
	elif i == len(new_text)-1:
		finished_work.append(' ' + new_text[i] + '.')
	elif i == 0:
		finished_work.append(new_text[i])
	else:
		finished_work.append(' ' + new_text[i])

new_book = ''.join(finished_work).strip()
book_file = open('new_dickens_book', 'w')
book_file.write(new_book)