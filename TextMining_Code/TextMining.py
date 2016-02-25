# from bs4 import BeautifulSoup
import pickle

from pattern.web import *
# ts_eliot_texts_FULL = URL('http://www.gutenberg.org/cache/epub/1567/pg1567.txt').download()

# # Save data to a file (will be part of your data fetching script)
# f = open('ts_eliot_full.pickle','w')
# pickle.dump(ts_eliot_texts_FULL,f)
# f.close()


# oscar_wilde_dorian_gray_FULL = URL('http://www.gutenberg.org/cache/epub/26740/pg26740.txt').download()


# Save data to a file (will be part of your data fetching script)
# f = open('oscar_wilde_full.pickle','w')
# pickle.dump(oscar_wilde_dorian_gray_FULL,f)
# f.close()

lincoln_speeches_FULL = URL('http://www.gutenberg.org/cache/epub/14721/pg14721.txt').download()

f = open('lincoln_speeches.pickle','w')
pickle.dump(lincoln_speeches_FULL,f)
f.close()