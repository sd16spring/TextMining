from pattern.web import *
import pickle

w=Wikipedia()

def Book_Summary(search_term):
    """
    Input = book title
    output: prints the summary of the book
    """
    article = w.search(search_term)
    if article:
        store = article.sections
        i = 0
        while i < len(store):
            section = store[i]
            if section.title in ['Overview', 'Plot', 'Summary', 'Plot summary', 'Synopsis']:
                #pull the summary and encode in utf-8
                text = section.content.encode('utf-8')
                print text
            else:
                "yikes. is that a book?"
            i+=1
    else:
        print "Couldn't find your book. Try again."

# search_term = "Mice and Men"
# search_term = "Moby Dick"
search_term = "The Great Gatsby"
Book_Summary(search_term)
