"""Uses the pattern and pickle packages to fetch all of Shakespeare's works from Project Gutenberg and save the to disk"""

import pickle

from pattern.web import *
complete_shakespeare = URL('http://www.gutenberg.org/files/100/100.txt').download()

# Save data to a file (will be part of your data fetching script)
f = open('complete_shakespeare.pickle','w')
pickle.dump(complete_shakespeare,f)
print 
f.close()