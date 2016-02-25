""" Since the only source I could find for My Immortal was a webpage with html, I had to get rid
of the html elements. Much thanks to Alex Hoppe for helping me out with beautiful soup and un-htmling the text."""

import htmlentitydefs as html
from bs4 import BeautifulSoup
from pattern.web import *


# Load data from a file (will be part of your data processing script)
# input_file = open('my_immortal122.html','r')
# recycled_trash = pickle.load(input_file)
# input_file.close()
# print recycled_trash[0]

#BeautifulSoup (hopefully gets rid of some of the html bits)
soup = BeautifulSoup.BeautifulSoup(open('my_immortal122.html','r'))

body = str(soup.find('div', {'class':'fw-text'})) #finds where the header of the html ends and the text begins


### Trying to get the tags out.
tag = True
trimmed = ''
# iterate along the string, if a tag is open, stop adding chars to the output string until we hit a close tag
for char in body:
	if char == '<':
		tag = True
	elif char == '>':
		tag = False
	elif not tag:
		trimmed += char
	#else don't print anything. 



# Replace html entities with ascii
# for char in  
codedefs = {v: k for k, v in html.entitydefs.items()}
#print codedefs
code = False
codestring = ''
output = ''
for char in trimmed:
	if char == "&":
		code = True
		codestring += '&'
	elif char == ';' and code:
		code = False
		codestring += ';'
		output += ' '
		codestring = ''
	elif code:
		codestring += char
	elif not code:
		output += char

f = open('my_immortal122new.txt','w')
f.write(output)
f.close()


