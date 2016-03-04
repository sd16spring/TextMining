"""This code filters a robin williams stand up special and returns the average sentimentality of the performance along with an ordered list of the most commonly used words. Also, I decided not to do 
doctests because all of the functions depend on globalvariables. For this reason, there would be only one possible output, and it would be clear whether it was working or not by testing as I go.
This was my best judgement, but let me know if I should have done something differently."""
from pattern.web import *
from pattern.en import *
data = URL('http://www.script-o-rama.com/movie_scripts/r/robin-williams-live-on-broadway-script.html').download()
"""I filtered the data by replacing some characters with empty strings, making everything lowercase, and splitting the data into a list"""
(before,data) = data.split('<pre>')
(data,after) = data.split('</pre>')
data = data.replace('?','')
data = data.replace('.','')
data = data.replace(',','')
data = data.replace('!','')
data = data.replace("'s",'')
data = data.replace('"','')
data = data.replace(':','')
data = data.replace(';','')
data = data.lower()
datalist = data.split()


filename = open('standuptext.txt','w')
filename.write(data)
filename.close()

#This function uses the previously defined data to determine the average sentimentality of a stand up comedians performance
def sentimentality():
	totalsent = 0
	totalsentnum = 0
	linelist = data.split('\n')
	# import pdb; pdb.set_trace()
	for line in linelist:
		#If the line is not blank
		if line != '':			
			sent = sentiment(line)
			#If the sentiment is not zero
			if sent[0] != 0.0:
				totalsent = sent[1] + totalsent
				totalsentnum += 1
	return totalsent/totalsentnum

#Fill the histogram using all of the words from the performance
def fill_hist():
	hist = dict()
	for word in datalist:
		hist[word] = hist.get(word,0)+1;
	return hist

#Sorts the histogram using lambda and the predefined sorted function
def sort_hist(dictionary):
	"""
		>>> sort_hist({"bought":1,"sold":5, "created":3})
		[('bought', 1), ('created', 3), ('sold', 5)]
		>>> sort_hist({})
		[]
		>>> sort_hist({"two":2,"one":1})
		[('one', 1), ('two', 2)]
	"""
	histlist = dictionary.items()
	return sorted(histlist, key = lambda tuple: tuple[1])

#def sentiment(dictionary):

#Reverses the sorted histogram list and prints average sentiment and the word count.
def result():
	dictionary = fill_hist()
	sorteddictionary = sort_hist(dictionary)
	wordtotal = 0
	oncetotal = 0
	for wordtuple in sorteddictionary:
		if wordtuple[1] == 1:
			oncetotal += 1.0
		wordtotal += 1.0
	print oncetotal/wordtotal
	print sentimentality()
	print sorteddictionary[::-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
result()