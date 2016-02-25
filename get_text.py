"""
This code is run to save the text from The Wonderful Wizard of Oz 
by Frank Baum and Robin Hood by J. Walker McSpadden.

Two .pickle files can be created to save the text of both books.

These files are used in analyze_text.py

@REBECCA PATTERSON 02-25-16
"""
import pickle
from pattern.web import *


#downloading the text
wizard_of_oz_full_text = URL('http://www.gutenberg.org/cache/epub/55/pg55.txt').download()
robin_hood_full_text = URL('http://www.gutenberg.org/cache/epub/832/pg832.txt').download()

# Save data to a file
f1 = open('wizard_of_oz_text.pickle','w')
pickle.dump(wizard_of_oz_full_text,f1)
f1.close()

f2 = open('robin_hood_text.pickle','w')
pickle.dump(robin_hood_full_text,f2)
f2.close()