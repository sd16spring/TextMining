
import pickle
from pattern.web import *

the_book_of_nature_myths_full_text = URL('http://www.gutenberg.org/cache/epub/22420/pg22420.txt').download()
#print the_book_of_nature_myths_full_text
the_phoenix_and_the_carpet_full_text = URL('http://www.gutenberg.org/cache/epub/836/pg836.txt').download()
#print the_book_of_nature_myths_full_text


#Pickling!!
# Save data to a file (will be part of your data fetching script)
f1 = open('nature_myths_texts.pickle','w')
pickle.dump(the_book_of_nature_myths_full_text,f1)
f1.close()

# Save data to a file (will be part of your data fetching script)
f2 = open('phoenix_and_carpet_texts.pickle','w')
pickle.dump(the_phoenix_and_the_carpet_full_text,f2)
f2.close()