'''
This short script gets data from the web and dumps them into pickle files 
'''
from pattern.web import *
import pickle 

#To get from wikipedia:
w=Wikipedia()
article=w.search('Le Petit Prince')
source_text=article.string
text_name='Bronte-Wuthering_heights'

# Downloding from link:

link='http://www.gutenberg.org/cache/epub/768/pg768.txt'

source_text= URL(link).download()

file = open(text_name+'.pickle','w')
pickle.dump(source_text,file)
file.close()