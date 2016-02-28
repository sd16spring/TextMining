''' Import code for textmining project. '''
from pattern.web import *
from os.path import exists
import pickle

def get_booktext(url_string,file_name):
	''' Given the url of the plaintext book from the Gutenberg Project, saves it as a pickled file.
		Inputs:
		url_string: String. address of plaintext book text.
		file_name: String. desired file name of the pickled file. To be saved in ~/TextMining directory.
		Outputs:
		None. Just writes the pickle to the given file_name.'''

	if exists(file_name) == True:
		print "You've already downloaded the dang book. Returning None."
		return None
	else:
		f = open(file_name,'w')
		full_text = URL(url_string).download() #very long string
		f.write(full_text)
		f.close()
		print 'Done!'
		return None


#The import/download calls
get_booktext('http://eremita.di.uminho.pt/gutenberg/2/4/241/241.txt','Clotelle.txt')
get_booktext('http://www.gutenberg.org/cache/epub/46160/pg46160.txt','Malaeska.txt')
get_booktext('http://gutenberg.readingroo.ms/3/1/8/6/31869/31869.txt','Lamplighter.txt')
get_booktext('http://gutenberg.readingroo.ms/2/7/0/2701/2701.txt','MobyDick.txt')
get_booktext('http://www.mirrorservice.org/sites/ftp.ibiblio.org/pub/docs/books/gutenberg/3/33/33.txt','ScarletLetter.txt')
get_booktext('http://eremita.di.uminho.pt/gutenberg/2/0/203/203.txt','UncleToms.txt')
get_booktext('http://www.mirrorservice.org/sites/ftp.ibiblio.org/pub/docs/books/gutenberg/1/1/2/1/11214/11214.txt','Garies.txt')
get_booktext('http://eremita.di.uminho.pt/gutenberg/5/8/584/584.txt','OurNig.txt')
