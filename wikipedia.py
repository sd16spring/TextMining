from pattern.web import *
import pickle
from pattern.en import *

w=Wikipedia()

def save_data(title, input):
    # Save data to a file 
    # remove spaces
    title.replace(' ', '')
    filename = "books/" + title + '.pickle'
    f = open(filename,'w')
    pickle.dump(input,f)
    f.close()

def get_data(title):
    # Load data from a file
    title.replace(' ', '')
    filename = "books/" + title + '.pickle'
    input_file = open(filename,'r')
    reloaded_copy_of_texts = pickle.load(input_file)
    return reloaded_copy_of_texts

def book_summary(title):
    """
    Input = book title
    output: prints the summary of the book
    """
    try:
        text = get_data(title)
        return text
    except:
        article = w.search(title)
        if article:
            store = article.sections
            i = 0
            while i < len(store):
                section = store[i]
                if section.title in ['Overview', 'Plot', 'Summary', 'Plot summary', 'Synopsis']:
                    #pull the summary and encode in utf-8
                    text = section.content.encode('utf-8', errors='ignore')
                    save_data(title, text)
                    return text
                else:
                    "yikes. is that a book?"
                i+=1
        else:
            print "Couldn't find your book. Try again."



def book_compare(title_list):
    """
    Compares two books

    Input: Two strings in a list
    Output: String with recommendation

    >>> book_compare(["The Great Gatsby", "If You Give a Mouse a Cookie"])
    If You Give a Mouse a Cookie is definitely better

    """

    #Find the text, establish a "rating" for each book, and a relative difference
    text1 = book_summary(title_list[0])
    text2 = book_summary(title_list[1])
    rating1 = sentiment(text1)[0]
    rating2 = sentiment(text2)[0]
    delta = (rating1 - rating2)

    #Print the name of the "better" book first
    if delta > 0.01:
        print title_list[0],
    elif delta < -0.01:
        print title_list[1],
    elif delta <= .01 and delta >= -.01:
        print "They're equally good"

    #Print a statement that tells
    if delta > .02 or delta < -.02:
        print "is definitely better"
    elif (delta >= .01 and delta <=.02) or (delta <= -.01 and delta >= -.02):
        print "is a better option"


title = [["Mice and Men" , "Moby Dick"] ,
         ["The Great Gatsby", "If You Give a Mouse a Cookie"],
         ["Nineteen Eighty-Four", "Great Expectations"],
         ["To Kill a Mockingbird", "Pride and Prejudice"],
         ["Jane Eyre", "The Hobbit"],
         ["Canary Row", "East of Eden"],
         ["The Grapes of Wrath", "Adventures of Huckleberry Finn"],
         ["The Catcher in the Rye", "Wuthering Heights"]]
for i in title:
    book_compare(i)

