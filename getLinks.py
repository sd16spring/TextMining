#This script will scrape links that lead to 2pac lyrics
#base link http://www.metrolyrics.com/2pac-lyrics.html

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import pickle

links = []# list of links that we will save as links.pickle

baseurl = "http://www.metrolyrics.com/2pac-lyrics.html"

html = urlopen(baseurl)
bsObj = BeautifulSoup(html)

for link in bsObj.find("div", {"id":"artist-lyrics"}).findAll("a", href=re.compile("2pac.html$")):
    if 'href' in link.attrs:
        links.append(link.attrs["href"])


f = open("links.pickle", "w")
pickle.dump(links,f)
f.close()

#debuging print statements
print "number of links / songs = " + str(len(links))
