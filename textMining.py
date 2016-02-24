from pattern.web import *
import pickle


def printAllLinks(title, wLog, wikipedia, iterationCount):
	"""
	Prints and stores all links from a given page
	title = the title of the article being examined
	wLog = a Dictionary<String><List<String>> storing all data thus far
	wikipedia = wikipedia
	iterationCount = the depth of recursion
	"""

	if iterationCount <= 0:
		return

	print title
	try:
		article = wikipedia.search(title)
	except URLError:
		return
	if article == None:
		return

	listOfLinks = article.links
	wLog[title] = listOfLinks
	for link in listOfLinks:
		if not wLog.has_key(link):
			printAllLinks(link, wLog, wikipedia, iterationCount-1)

	if iterationCount > 1:	# saves every once in a while
		f = open('Wikipedia','w')
		pickle.dump(linksDict,f)
		f.close()


startPage = "Adolf Hitler"
w = Wikipedia()
input_file = open('Wikipedia','r')
linksDict = pickle.load(input_file)
input_file.close()
printAllLinks(startPage, linksDict, w, 4)