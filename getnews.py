# import urllib
# from bs4 import BeautifulSoup

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re

def main():
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    mainurl = 'http://www.cnn.com/'
    # url = 'http://www.cnn.com/2013/10/29/us/florida-shooting-cell-phone-blocks-bullet/index.html?hpt=ju_c2'
    # url = 'http://www.cnn.com/2016/02/24/middleeast/swedish-teen-freed-from-isis/index.html'
    soup = BeautifulSoup(opener.open(mainurl))

    # print type(soup.find("div", {"class":"share-bar-whatsapp-container"}))
    #1) Link to the website 

    #2) title of article
	# title = soup.findAll("span", {"class":"cd__headline-text"})

    #3) Text of the article
    # paragraphs = soup.findAll("p", {"class":"zn-body__paragraph"})
    # text = " ".join([ paragraph.text.encode('utf-8') for paragraph in paragraphs])

    # print url
    # print title 
    # print text

def getlinks():
	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	mainurl = 'http://cnnespanol.cnn.com'
	# mainurl = 'http://cnn.com'
	soup = BeautifulSoup(opener.open(mainurl))

	urls = soup.findAll("a", {"href":re.compile("/index.html")})
	text = " ".join([ url.text.encode('utf-8') for url in urls])
	text_file = open('CNNtext.txt', 'a')
	text_file.write(text)
	text_file.close()
	return text

# def process_file(filename):
#     hist = dict()
#     fp = open(filename)
#     for line in fp:
#         process_line(line, hist)
#     return hist

# def process_line(line, hist):
#     line = line.replace('-', ' ')
    
#     for word in line.split():
#         word = word.strip(string.punctuation + string.whitespace)
#         word = word.lower()

#         hist[word] = hist.get(word, 0) + 1


# def most_common(hist):
#     t = []
#     for key, value in hist.items():
#         t.append((value, key))

#     t.sort(reverse=True)
#     return t

# 	hist = process_file()

# 	t = most_common(hist)
# 	common_words = ['the']
# 	print 'The most common words are:'
# 	for freq, word in t[0:10]:
# 	    if word not in common_words:
# 	        print word, '\t\t', freq


if __name__ == '__main__': 
	getlinks()
    # main()
