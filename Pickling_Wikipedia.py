#Printing out the title of every Wikipedia article:
from pattern.web import *
import pickle

w = Wikipedia()
sanders_article = w.search('Political positions of Bernie Sanders')
#The paragraphs for each section. 
sanders_results = sanders_article.string.encode('utf-8')

clinton_article = w.search('Political positions of Hillary Clinton')
clinton_results = clinton_article.string.encode('utf-8')

#print clinton_results

#load data from a file
f = open('dempresidential_candidate_sanders.pickle', 'w')

# Save data to a file (will be part of your data fetching script)
pickle.dump(sanders_results, f)
f.close()


#load data from a file
g = open('dempresidential_candidate_clinton.pickle', 'w')
pickle.dump(clinton_results, g)
#print vars(clinton_article.sections[0])
#pickle.dump(clinton_article.sections[0].title, f)
g.close()

##load data from a file
#input_file = open('presidential_candidate.pickle', 'r')
#reloaded_copy_of_texts = pickle.load(input_file)