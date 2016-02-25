""" Finds frequency of all words in the fist 22 chapters of My Immortal. 
AN: WARNING: SUM OF DIS CODE IS XTREMLY SCRAY. VIOWER EXCRETION ADVISD.
"""
def get_frequency(filename):
	""" Gets frequencies of words in a file"""
	d = {}
	f = open(filename, 'r')
	text = f.read()
	wordlist = text.split()
	for word in wordlist:
		word = word.lower()
		d[word] = d.get(word, 0) + 1
	return d

def words_between(a, b):
	""" Gets words between a certain number of occurences. """
	words = []
	for number in range(a,b):
		try:
			words += [reversefreq[number]]
		except KeyError:
			pass
	return words


freq = get_frequency('my_immortal122new.txt')
reversefreq = {v: k for k, v in freq.items()} #gets the reverse list. Doesn't work perfectly because there are multiple keys that
#map to the same value, but for large enough numbers it shouldn't matter because its highly unlikely that there are multiple words
#with exactly 115 instances.
print freq['flam'] + freq['flame'] + freq['flamming'] + freq['flaming']
print freq['prepz'] + freq['prep'] + freq['preps'] + freq['prepz!']
#print words_between(59,400)
