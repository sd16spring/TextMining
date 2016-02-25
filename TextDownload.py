"""
Downloads and saves the text of Little Women. Cleans the text by removing punctuation and capital letters.
"""

from pattern.web import*
import pickle
import string


LittleWomenURL = URL('http://gutenberg.readingroo.ms/5/1/514/514.txt').download()
LittleWomen = plaintext(LittleWomenURL)

exclude = set(string.punctuation)
LittleWomen = ''.join(ch for ch in LittleWomen if ch not in exclude)
LittleWomen = LittleWomen.lower()


f = open('LittleWomen.pickle', 'w')
pickle.dump(LittleWomen.encode('UTF-8'),f)
f.close()