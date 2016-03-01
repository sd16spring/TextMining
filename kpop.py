"""
Finds English words sampled in the lyrics of the kpop girl group 2NE1 and
analyzes their sentiment and frequency

@author: Katie Butler
"""

import urllib#.request
#import urllib.error
#import urllib.parse
#import bs4
#from bs4
import BeautifulSoup as bs
from pattern.web import *

#g = open('/usr/share/dict/korean')
#M = g.readlines(L)
#for i in range(len(M)):
#    M[i] = M[i].strip()
#g.close()
L = []
f = open('/usr/share/dict/american-english')
L = f.readlines()
#english = {}
#for i in L)):9
#    L[i] = L[i].strip()
def real_word(word):
    """This is taking """
    word = word.strip()
    return word
english = map(real_word,L)

f.close()

# artists = 'http://www.azlyrics.com/19/2ne1.html'
# g = urllib2.urlopen(artists)
# html = g.read()
# #print html
# links = bs.BeautifulSoup(html)
# print links

def processing():
    # song_links = links.find('div',id='listAlbum')
    # #print song_links
    # songs = song_links.findAll('a',href=True)
    #i = 0
    # for url in songs:
    #     if 'http://www.amazon.com' not in url['href']:
    #         song_url = 'http://www.azlyrics.com' + url['href'][2:]
    #         song = urllib2.urlopen(song_url)
    #         read_lyrics = song.read()
    #         f = open('song'+str(i)+'.txt','w')
    #         f.write(read_lyrics)
    #         f.close()
    #         i+=1
    num_songs = 1#42
    for j in range(num_songs):
        #bs = BeautifulSoup.BeautifulSoup.getText(read_lyrics)
        f = open('song'+str(j)+'.txt')
        read_lyrics = f.read()
        bs_lyrics = bs.BeautifulSoup(read_lyrics)
        #print bs_lyrics
        #break
        divs = bs_lyrics.findAll('div')
        lyrics = ''
        for d in divs:
            #print '------------------------------------------------------------'
            #print d
            if len(d) > len(lyrics):
        text = d
        text = bs_lyrics.find("form",id="addsong")
        print text
        print text.find_previous_siblings()
        break

first_link = soup.a
first_link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

first_link.find_all_previous("p")
# [<p class="story">Once upon a time there were three little sisters; ...</p>,
#  <p class="title"><b>The Dormouse's story</b></p>]

first_link.find_previous("title")
# <title>The Dormouse's story</title>



        divs = bs_lyrics.findAll('div')
        lyrics = ''
        for d in divs:
            #print '------------------------------------------------------------'
            #print d
            if len(d) > len(lyrics):
                text = d

        #print lyrics
        #break
        #lyrics = text.getText()
        #print lyrics
        #lyrics = [x.getText() for x in lyrics]
    """f = open('kpop.pickle','w')
    pickle.dump(lyrics,f)
    f.close()

    # Load data from a file (will be part of your data processing script)
    input_file = open('kpop.pickle','r')
    bad_taste = pickle.load(input_file)
    input_file.close()
    print kpop"""

processing()

def sample(kpop,english):
    for i in kpop:
        if kpop[i] not in english:
            kpop.remove[i]
    print kpop

#sample(kpop,english)

"""def printing(artist, title, save, lyrics):
    for x in lyrics:
        print(x, end="\n\n")
    if save == True:
        saving(artist, title, lyrics)
    elif save == False:
        pass

def saving(artist, title, lyrics):
        f = open(artist + '_' + title + '.txt', 'w')
        f.write("\n".join(lyrics).strip())
        f.close()"""
