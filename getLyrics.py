#this script will scrape lyrics from a list of links

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import pickle

#open the list of links
input_file = open("links.pickle", "r")
links = pickle.load(input_file)


lyrics = [] #lyrics will contain list of lyrics.  This will not be final format as we will still need to seperate by line and word in a assembleDataset.py

i = 0

for link in links:
    """
    open each link and gather the lyrics
    """

    print str(i) + " / " + str(len(links)) #step through i for each link to see visual progress
    i += 1

    html = urlopen(link)
    bsObj = BeautifulSoup(html)

    for verse in bsObj.findAll("", {"class":"verse"}):
        lyrics.append(verse.get_text())

print "expected number: " + str(len(lyrics)) 

#pickle the lyrics
f = open('lyrics.pickle', 'w')
pickle.dump(lyrics, f)
f.close()

