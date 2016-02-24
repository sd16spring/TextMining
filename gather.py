from pattern.web import *
from os.path import exists
import sys
from pickle import dump, load

def twitterGather(hashtag, iters, sleep):
	fout = open(hashtag[1:] + '.txt', 'w')
	s = Twitter().stream(hashtag)
	for i in range(iters):
		time.sleep(sleep)
		s.update(bytes = 1024)
		ans = s[-1].text if s else ''
		print(ans)
		try:
			fout.write(ans + '\n')
		except UnicodeEncodeError:
			dump(ans, fout)
	fout.close()

def twitterSearch(query, iters, begin):
	fout = open(query + '_search.txt', 'w')
	t = Twitter()
	i = begin
	for j in range(iters):
		for tweet in t.search(query, start=i, count=10): 
			print(tweet.text)
			try:
				fout.write(tweet.text + '\n')
			except UnicodeEncodeError:
				dump(tweet.text, fout)
			i = tweet.id
	fout.close()
if __name__ == '__main__':
	#twitterGather('#dank', 200, 30)
	twitterSearch('dankmeme', 500, 4000)