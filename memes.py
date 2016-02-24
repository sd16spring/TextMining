import sys, random
from pickle import dump, load
ignores = ['http', '#', 'u00', '@', 'u2013', '///']#auto ignore any words including these strings
def markovGen(filename):
	reader = open(filename, 'r')#opens file to read
	markIn = open('markovMeme.txt', 'r')#for importing a previous markov matrix
	mark = load(markIn)
	markIn.close()
	# mark = {}#for starting with a blank markov matrix
	for line in reader:
		if(line != 'p0'):#useless lines ignored
			line = line.replace('.V', '')#other header messages that are uneeded
			line = line.replace('.RT', '')
			if(line[0] == '.'):#some messages start with a .
				line = line[1:]
			words = line.split()#array of individual words
			removes = []#start recording things to remove
			for ig in ignores:
				for word in words:
					if ig in word:
						removes.append(word)
			for stuff in removes:#actually remove objects
				try:
					words.remove(stuff)
				except ValueError:#try/catch in the event that it tries to remove the same object twice
					pass
			for i in range(len(words)):#normalize all words to lowercase
				words[i] = words[i].lower()
			for i in range(len(words) - 1):#add things to markov matrix
				word = words[i]
				if(not(word in mark.keys())):#if the word is not already in the markov, create a new entry for it and the following word
					mark[word] = {words[i+1] : 1}
				else:
					if(words[i+1] in mark[word].keys()):#check to see if the following word is in the dictionary for the current word, increment if it is otherwise create a new entry
						mark[word][words[i+1]] += 1
					else:
						mark[word][words[i+1]] = 1
	fout = open('markovMeme.txt', 'w')#save the markov
	dump(mark, fout)
	fout.close()
	reader.close()
	return mark
def markovMemer(markFile):
	markIn = open(markFile, 'r')
	mark = load(markIn)
	markIn.close()
	k = mark.keys()
	memes = []
	for word in k:
		meme = ''
		curWord = word
		try:
			for x in range(random.randint(5, 12)):
				sortedKeys, sortedFreq = selectionSort(mark[curWord])
				tot = sum(sortedFreq)
				choice = random.randint(1, tot)
				i = 0
				choice -= sortedFreq[0]
				while(choice > 0):
					i += 1
					choice -= sortedFreq[i]
				meme += sortedKeys[i] + ' '
				curWord = sortedKeys[i]
			memes.append(meme)
		except Exception:
			pass
	fout = open('maymays.txt', 'w')
	dump(memes, fout)
	fout.close()
	return memes


def selectionSort(d):
	k = list(d.keys())
	a = [d[q] for q in d]
	for x in range(len(a)-1):
		mintemp = x
		for y in range(x+1, len(a)):
			if a[y] > a[mintemp]:
				mintemp = y
		temp = k[x]
		k[x] = k[mintemp]
		k[mintemp] = temp
		temp = a[x]
		a[x] = a[mintemp]
		a[mintemp] = temp
	return k, a

if __name__ == '__main__':
	#print(markovGen('dankmeme_search2.txt'))
	print(markovMemer('markovMeme.txt'))
