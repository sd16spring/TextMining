#this script will scrape lyrics from a list of links

from urllib import urlopen
from bs4 import BeautifulSoup
import re
import pickle

input_file = open("links.pickle", "r")
links = pickle.load(input_file)
lyrics = []
i = 0

for link in links:

    print i
    i += 1

    html = urlopen(link)
    bsObj = BeautifulSoup(html)

    for verse in bsObj.findAll("", {"class":"verse"}):
        lyrics.append(verse.get_text())

print lyrics

f = open('lyrics.pickle', 'w')
pickle.dump(lyrics, f)
f.close()

#for link in bsObj.find("div", {"id":"artist-lyrics"}).findAll("a", href=re.compile("2pac.html$")):
#    if 'href' in link.attrs:
#        links.append(link.attrs["href"])

