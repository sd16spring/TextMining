import sys, random
from pickle import dump, load
ignores = ['http', '#', 'u00', '@', 'u2013', '///']#auto ignore any words including these strings
def markovGen(filename, markFile, existing = True):#creates file with markov dictionary
	reader = open(filename, 'r')#opens file to read
	if(existing):
		markIn = open(markFile, 'r')#for importing a previous markov dictionary
		mark = load(markIn)
		markIn.close()
	else:
		mark = {}#for starting with a blank markov dictionary
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
			for i in range(len(words) - 1):#add things to markov dictionary
				wordy = words[i]
				if(not(wordy in mark.keys())):#if the word is not already in the markov, create a new entry for it and the following word
					mark[wordy] = {words[i+1] : 1}
				else:
					if(words[i+1] in mark[wordy].keys()):#check to see if the following word is in the dictionary for the current word, increment if it is otherwise create a new entry
						mark[wordy][words[i+1]] += 1
					else:
						mark[wordy][words[i+1]] = 1
			if('.end!' in mark[wordy].keys()):#create an entry to indicate the end of a tweet
				mark[wordy]['.end!'] += 1
			else:
				mark[wordy]['.end!'] = 1
	fout = open(markFile, 'w')#save the markov
	dump(mark, fout)
	fout.close()
	reader.close()
	return mark
def markovMemer(markFile, output, existing = True):#generates strings of words based on markov dictionary
	markIn = open(markFile, 'r')#reads in markov file
	mark = load(markIn)
	markIn.close()
	k = mark.keys()
	memes = []
	for word in k:#iterates over each word in the keys of the markov
		meme = ''
		curWord = word
		try:#try/catch, some keys wouldn't link to anything
			for x in range(random.randint(10, 30)):
				sortedKeys, sortedFreq = selectionSort(mark[curWord])#sorts by keys by frequency
				choice = random.randint(1, sum(sortedFreq))#chooses a random integer within the range of the sum of all frequencies
				i = 0
				choice -= sortedFreq[0]
				while(choice > 0):#iterates down by each frequency in the list of frequencies, reaching 0 indicates the word that is chosen
					i += 1
					choice -= sortedFreq[i]
				if(sortedKeys[i] == '.end!'):#if an indicator of end of a tweet is reached, it ends the creation of current string
					break
				meme += sortedKeys[i] + ' '#adds a word to the string
				curWord = sortedKeys[i]#sets the next word to operate on
			if(meme != ''):
				memes.append(meme[:len(meme)-1])#adds the string to a list as long as it isn't empty
		except Exception:#in the event that an error is raised due to a string not mapping to anything, gives up on the current string generation
			pass
	if(existing):#previous collection of strings are added to the current one if they exist
		fin = open(output, 'r')
		memes = load(fin) + memes
		fin.close()
	fout = open(output, 'w')#save the list of strings
	dump(memes, fout)
	fout.close()
	return memes


def selectionSort(d):#modified selection sort to operate on dictionary keys and mapped values to sort by maps
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

def readMemes(filename):#for reading the pickled files
	fin = open(filename, 'r')
	memes = load(fin)
	fin.close()
	return memes

def purelyDankMemes():#creates list of strings based purely on tweets that included the phrase 'dankmeme'
	markovGen('dankmeme_search.txt', 'puremarkov.txt', False)
	markovGen('dankmeme_search1.txt', 'puremarkov.txt')
	markovGen('dankmeme_search2.txt', 'puremarkov.txt')
	return(markovMemer('puremarkov.txt', 'puredankmemes.txt', False))

def wateredDownMemes():#to gain a better understanding of syntax, other tweets are included as well, but tweets including 'dankmeme' are weighted heavier in the markov dictionary
	markovGen('stuff_search.txt', 'impuremarkov.txt', False)
	markovGen('really_search.txt', 'impuremarkov.txt')
	markovGen('haha_search.txt', 'impuremarkov.txt')
	for i in range(3):
		markovGen('dankmeme_search.txt', 'impuremarkov.txt')
		markovGen('dankmeme_search1.txt', 'impuremarkov.txt')
		markovGen('dankmeme_search2.txt', 'impuremarkov.txt')
	return((markovMemer('impuremarkov.txt', 'notquitedankmemes.txt', False)))

if __name__ == '__main__':
	# print(markovGen('dankmeme_search2.txt', 'mark2.txt'))
	# print(markovMemer('mark2.txt', 'normiememes.txt'))
	# print(purelyDankMemes())
	print(wateredDownMemes())