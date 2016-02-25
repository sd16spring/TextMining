from pattern.en import *
from langdetect import *
from re import match
import string,pickle

def sentimentAnalyzer(commentList):
	"""takes the sentiment of each commetnaccording to the pattern module.
		calculates the average polarity of all the comments and the average extremity of 
		all the comments
		Returns in the format (averagePolarity, averageExtremity)
		"""
	#takes sentiment of each comment
	#adds 1 to total comments
	#adds polarity to polarity
	#adds abs polarity to extremity
	totalComments = 0
	polarity = 0.0
	extremity = 0.0
	for c in commentList:
		pol = sentiment(c)[0]
		totalComments += 1
		polarity += pol
		extremity += abs(pol)
	if totalComments==0:
		return (0,0)
	return (polarity/totalComments, extremity/totalComments)

def getAllWords(commentList):
	"""Extracts all words in the comments, without leading or trailing whitespace and 
		punctuation, in lowercase
		Returns a dictionary of all the words, where (key,value) is (lang,comments)"""
	allWords = []

	for c in commentList:
		for w in c.split():
			if match('.*[A-Za-z0-9]+.*',w):
				allWords.append(w.strip(string.punctuation).lower())
	return allWords

def wordFrequency(commentList):
	"""Calculates the frequency of the words in the given comments
		Returns a sorted list of tuples (word, numberOfAppearances)

		>>> wordFrequency(['hello how are you', 'hello hello hello', 'how you you'])
		[('hello', 4), ('you', 3), ('how', 2), ('are', 1)]

		"""
	allWords = getAllWords(commentList)
	wordFreq = {}
	for w in allWords:
		wordFreq[w]=wordFreq.get(w,0)+1
	return sorted(wordFreq.items(),key=lambda x: x[1],reverse=True)

def spellCheck(commentList):
	"""Compares the list of words to a set of words and sees how many
		words are not in the word list
		Words are the single and compound words from the Moby Project
		Returns the tuple (numCorrectWords, numMisspelledWords, misspelledWords)
		>>> spellCheck(['gross', 'wow! great vedio', 'i can\\'t spel'])
		(5, 2, ['vedio', 'spel'])
		"""
	dictWords = set()
	reader = open('256772co.mpo')
	for w in reader:
		dictWords.add(w.strip().lower())
	reader = open('354984si.ngl')
	for w in reader:
		dictWords.add(w.strip().lower())
	allWords = getAllWords(commentList)
	numCorrect=0
	numWrong=0
	misspelled=[]

	for w in allWords:
		if w in dictWords:
			numCorrect+=1
		else:
			numWrong+=1
			misspelled.append(w)
	return (numCorrect,numWrong,misspelled)

if __name__=='__main__':
	# import doctest
	# doctest.testmod()
	masterList = {}
	from ReadFiles import CATEGORY_IDS
	for vidCat in CATEGORY_IDS:
		reader = open('comments'+str(vidCat)+'.txt')
		comments = pickle.load(reader)
		miniLangList = {}
		#seperate by languages; short strings and strings without letters default to en
		for c in comments:
			#print [c]
			lang = 'en'
			try:
				if len(c)>15:
					lang = detect(c)
			except lang_detect_exception.LangDetectException:
				pass
			x = miniLangList.get(lang,[])
			x.append(c)
			miniLangList[lang]=x
			y=masterList.get(lang,[])
			y.append(c)
			masterList[lang]=y

		#print comments
		print 'ID: '+ str(vidCat)
		if 'en' in miniLangList.keys():
			
			sent = sentimentAnalyzer(miniLangList['en'])
			print 'Average Polarity: {:1.5f}'.format(sent[0])
			print 'Average Extremity: {:1.5f}'.format(sent[1])
			freqs = wordFrequency(miniLangList['en'])
			print 'Top 20:'
			print freqs[0:20]
			spell = spellCheck(miniLangList['en'])
			print 'Spelled Right: {}\nSpelled Wrong: {}'.format(spell[0], spell[1])#,spell[2])
			print[(k, len(miniLangList[k])) for k in sorted(miniLangList.keys())]
			print ''
	print 'ALL'
	sent = sentimentAnalyzer(masterList['en'])
	print 'Average Polarity: {:1.5f}'.format(sent[0])
	print 'Average Extremity: {:1.5f}'.format(sent[1])
	freqs = wordFrequency(masterList['en'])
	print 'Top 20:'
	print freqs[0:100]
	spell = spellCheck(masterList['en'])
	print 'Spelled Right: {}\nSpelled Wrong: {}'.format(spell[0], spell[1])#,spell[2])
	print 'Percentage Mispelled: {}'.format(spell[1]*100.0/(spell[0]+spell[1]))
	langs = [(k, len(masterList[k])) for k in masterList.keys()]
	print sorted(langs, key=lambda x:x[1],reverse=True)