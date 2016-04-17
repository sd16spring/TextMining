from pattern.web import *
import urllib2
import pickle



def get_text(URL_string, name):
    """This function grabs the text from a text file on the web and pickles it for future use.
Arguments: URL of text file to be saved as a string, name of the file for use in naming data variables and pickle files (also a string).
 Returns: Pickled data!"""

    tale = URL(URL_string).download()
    save_file = open(name + '.pickle', 'w')
    pickle.dump(tale, save_file)
    save_file.close()

