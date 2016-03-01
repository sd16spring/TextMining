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
L = f.read()
#english = {}
#for i in L)):9
#    L[i] = L[i].strip()
def real_word(word):
    """This is taking """
    word = word.strip()
    return word
english = L.split()

all_english = {}
frequency = {}


f.close()

# artists = 'http://www.azlyrics.com/19/2ne1.html'
# g = urllib2.urlopen(artists)
# html = g.read()
# #print html
# links = bs.BeautifulSoup(html)
# print links

def processing(numb):
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
    all_words = []
    bs_lyrics = []
    if numb > 41:
        return 'exceeding index length'
    elif numb == 0:
        f = open('lyrics'+str(0)+'.txt')
        read_lyrics = f.read()
        #print read_lyrics
        bs_lyrics = bs.BeautifulSoup(read_lyrics).prettify()
        lyrics = bs.BeautifulSoup(bs_lyrics).getText()
        words = lyrics.split()
        #kpop = words.splitlines()
        #print bs_lyrics
        #lyrics = bs_lyrics.getText()
        #print lyrics
        #lyrics = [bs_lyrics for bs_lyrics in bs_lyrics.stripped_strings]
        #[text for text in soup.stripped_strings]
        all_words += words
    else:
        num_songs = numb
        for j in range(num_songs+1):
            #bs = BeautifulSoup.BeautifulSoup.getText(read_lyrics)
            if num_songs == 15 or num_songs == 40:
                return 'This song is entirely in English and will not be counted'
            else:
                f = open('lyrics'+str(j)+'.txt')
                read_lyrics = f.read()
                #print read_lyrics
                #bs_lyrics = read_lyrics.getText()
                bs_lyrics = bs.BeautifulSoup(read_lyrics).prettify()
                lyrics = bs.BeautifulSoup(bs_lyrics).getText()
                #print bs_lyrics
                words = lyrics.split()
                #kpop = words.splitlines()
                #lyrics = bs_lyrics.getText()
                #print lyrics
                #lyrics = [bs_lyrics for bs_lyrics in bs_lyrics.stripped_strings]
                #[text for text in soup.stripped_strings]
                all_words += words
    for i in range(len(all_words)):
        try:
            all_words[i] = all_words[i].decode()
        except UnicodeEncodeError:
            all_words[i] = ''
    return all_words
kpop = processing(20)

"""def create_word_list(complete_string):
+	Takes a string of the complete Shakespeare and splits it into a list of words, while inserting 'ENDLINE' between lines
+	shake_list_lines=complete_string.splitlines()
+	shake_list=[]
+	for line in shake_list_lines:
+		inner_list=line.split()
+		if not inner_list==[]:
+			inner_list.append('ENDLINE')
+			shake_list.append(inner_list)
+	#print shake_list
+	new_shake_list=[]
+	for inner_list in shake_list:
+		for word in inner_list:
+			new_shake_list.append(word)
+	return new_shake_list"""



def sample(korean):
    for word in korean:
        if word in english:
            all_english[word] = all_english.get(word,0)+1

def histogram(korean):
    for word in korean:
        frequency[word] = frequency.get(word,0)+1

sample(kpop)
histogram(kpop)

print sorted(all_english.items(),lambda x,y:x[1]-y[1],reverse = True)
#print frequency
