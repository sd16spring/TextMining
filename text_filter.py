""" This code was written by Rebecca Gettys, except where otherwise noted.  """
#### MAIN SECIOTN ####
from pattern.web import *
import urllib2
import pickle
import string
import seaborn as sns

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'grey', 'black', 'white', 'pink', 'ivory', 'tan', 'silver', 'gold', 'rose','gray', 'olive', 'crimson', 'maroon',
    'fuchsia', 'teal', 'lavender', 'lilac', 'aqua', 'azure', 'beige', 'indigo', 'magenta', 'cyan', 'scarlet',
    'canary', 'periwinkle']




def text_importing(name):
    """Imports previously-pickled fairy tale data (in string format from disk and returns a list of the strings.
    Arguements: name of the pickle file of previously pickled data (as a string, without the .pickle ending)!
    Returns: a pickle-imported string"""
    # Load data for each from from a file (will be part of your data processing script)
    input_file = open(name+ '.pickle','r')
    tale = pickle.load(input_file)
    return tale

def text_import (names):
    """ Runs imports on a list of names (strings) and returns them in a list.
    Arguments: list of strings (names)
    Returns: a list of three strings (the data from each pickle file)"
    """
    text_lists = []
    for string in names:
        text = text_importing(string)
        text_lists.append(text)
    return text_lists

#grimm_text = text_importing('grimm')
#perrault_text = text_importing('perrault')
#andersen_text = text_importing('andersen')
#text_lists = [andersen_text, perrault_text, grimm_text]



def color_searching(tale):
    """Searches the tale for a list of color words and counts the instances of these words up using a dictionary.
    Arguments: object (in this contex a list) to search, dictionary to search with
    Returns: dictionary containing keys and key-occurance frequencies (how many times the word showed up in the object)
    Due to the non-orderedness of dicionaries, hard to use a doctest"""
    color_dict = {color:0 for color in COLORS}
    for word in tale: #need to slice each tale into a list of words for this to work
        if word in color_dict:
            current_val = color_dict.get(word)
            val = current_val + 1
            color_dict[word] = val #made a dictionary of the string (color, frequnecy)
    return color_dict



def tale_searches(talelist):
    """Runs color_searching on each of the fairy tales and returns their dictionaries
    Arguments: list of tales (which are lists of strings (words))
    Returns: list of dictionaries, one for each tale (inside each dictionary, format is color-frequency)"""
    final_dict_list = [] #empty list
    for tale in talelist:
        tale_dict=color_searching(tale)
        final_dict_list.append(tale_dict)
    return final_dict_list

def tale_slicing(tale_list_text):
    """Slices the tales (strings) up into a list of words without spaces or punctuation and then puts each of those lists into another list.
     NOTE: https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal method that I used
    Arguments: list of strings (texts of the gutenberg tales)
    Returns: list of lists of words (a list containing lists whose items are the words of each tale)"""
   #print len(tale_list_text)
    tale_lists = []
    #print len(tale_list_text)

    for tale in tale_list_text:
        #print tale[0:100] #so both tales are coming in correctly so it is only going through index 1's input, ignoring index 0's
        tale_no_punc = ''
        for char in tale: #killing punctuation
            if not is_punct_char(char):
                tale_no_punc = tale_no_punc+char #so extend the string everytime we run into a letter
        list_of_words = []
        list_of_words = tale_no_punc.split( ) #splitting the string into the list
        #print type(list_of_words)
        #print list_of_words[0:100]
        tale_lists.append(list_of_words)
    #print len(tale_lists)
    return tale_lists



def is_punct_char(char):
    """From python.org (link above), all this does is check if a character is puncutation or not! the ultimate helper funcion!
    Arguments: character
    Returns: True/False if the character it is given is a puncuation mark - 1 is punctuation, 0 is not """
    return char in string.punctuation #1 is punctuation, 0 is not punctuation


#andersen, perrault, grimm is always the order
text_lists= text_import(['andersen', 'perrault', 'grimm']) # change these strings if you changed what got pickled
tale_lists = tale_slicing(text_lists)
output_dicts = tale_searches(tale_lists) #output dicts is a list of dictionaries and is your final output!
### END OF MAIN SECTION ###


### GRAPHING AND DATA PROCESSING ###

# Now just a ton of data processing
# just to make life easier, assign each dict inside output dict it's own variable

andersen_dict = output_dicts[0]
perrault_dict = output_dicts[1]
grimm_dict = output_dicts[2]
# dump dictionary to list of tuples
andersen_item_dump = andersen_dict.items()
perrault_item_dump = perrault_dict.items()
grimm_item_dump = grimm_dict.items()




def list_dumping (list):
    """This method I found on #http://stackoverflow.com/questions/7558908/unpacking-a-list-tuple-of-pairs-into-two-lists-tuples;
    just a convenient snippet of code which converts from the .items output to 2 lists in correct order
    Arguments: list (of two-item-tuples) that need to be seperated into lists
     Returns: a list containing keys as items in one list, values as items in the other list, in the correct order"""
    color = []
    frequency = []
    for i in list:
        color.append(i[0])
        frequency.append(i[1])
    return [color, frequency]
# turn the lists of tuples into a list of 2 lists each
andersen_color_freq= list_dumping(andersen_item_dump)
perrault_color_freq = list_dumping(perrault_item_dump)
grimm_color_freq = list_dumping(grimm_item_dump) #


## patrick is amazing for helping with this!!

def graph_func(andersen):
    sns.set( font_scale=.8)
    sns.axlabel('Color', 'Frequency' )
    #colors from http://www.color-hex.com and wikipedia
    flatui = ["#4b0082","#ffd700", "#e6e6fa", "#ffff00", "#FF2400", "#ff6eb4", "#d2b48c", "#ff00ff", "#0000ff", "#C8A2C8",
              "#800080", "#FF007F", "#FD3F92", "#000000", "#dc143c", "#CCCCFF", "#ffffff", "#ff0000", "#631919", "#fffff0",
              "#ffa500","#730000", "#808000","#00ffff","#c0c0c0","#808080",  "#7fffd4", "#808080", "#008000", "#f5f5dc",
              "#329999", "#f0ffff", "#FFEF00"]
    custom_palette = sns.color_palette(flatui)
    colors = andersen[0]
    occurences = andersen[1]
    ax = sns.barplot(colors, occurences, palette = custom_palette)
    fig = ax.get_figure()
    for item in ax.get_xticklabels():
        item.set_rotation(45)
    sns.plt.title('Color Word Frequencies in Hans Christian Andersen Stories')
    fig.savefig('andersen_chart.png')
    fig.clf()   # Clear figure


def graph_func2(perrault):
    sns.set( font_scale=.8)
    sns.axlabel('Color', 'Frequency' )
    #colors from http://www.color-hex.com and wikipedia
    flatui = ["#4b0082","#ffd700", "#e6e6fa", "#ffff00", "#FF2400", "#ff6eb4", "#d2b48c", "#ff00ff", "#0000ff", "#C8A2C8",
              "#800080", "#FF007F", "#FD3F92", "#000000", "#dc143c", "#CCCCFF", "#ffffff", "#ff0000", "#631919", "#fffff0",
              "#ffa500","#730000", "#808000","#00ffff","#c0c0c0","#808080",  "#7fffd4", "#808080", "#008000", "#f5f5dc",
              "#329999", "#f0ffff", "#FFEF00"]
    custom_palette = sns.color_palette(flatui)
    colors = perrault[0]
    occurences = perrault[1]
    ax2 = sns.barplot(colors, occurences, palette = custom_palette)
    fig2 = ax2.get_figure()
    for item in ax2.get_xticklabels():
        item.set_rotation(45)
    sns.plt.title('Color Word Frequencies in Charles Perrault Stories')
    fig2.savefig('perrault_chart.png')
    fig2.clf()

def graph_func3(grimm):
    sns.set( font_scale=.8)
    sns.axlabel('Color', 'Frequency' )

    #colors from http://www.color-hex.com and wikipedia
    #flatui = ["#521515", "#fffff0", "#4b0082","#ffd700", "#7fffd4", "#e6e6fa", "#ffff00",
    #          "#dc143c", "#ffc0cb", "#660000", "#808000", "#00ffff", "#d2b48c", "#c0c0c0",
    #          "#ff00ff", "#0000ff", "#808080", "#ffec8b","#ab82ff", "#ee4000", "#993299",
    #          "#ffaeb9", "#FF00FF", "#808080", '#f0ffff', "#008000", "#f5f5dc", "#008080",
    #          "#CCCCFF","#ffa500", "#000000", "#ffffff", "#ff0000"]
    flatui = ["#4b0082","#ffd700", "#e6e6fa", "#ffff00", "#FF2400", "#ff6eb4", "#d2b48c", "#ff00ff", "#0000ff", "#C8A2C8",
              "#800080", "#FF007F", "#FD3F92", "#000000", "#dc143c", "#CCCCFF", "#ffffff", "#ff0000", "#631919", "#fffff0",
              "#ffa500","#730000", "#808000","#00ffff","#c0c0c0","#808080",  "#7fffd4", "#808080", "#008000", "#f5f5dc",
              "#329999", "#f0ffff", "#FFEF00"]
    custom_palette = sns.color_palette(flatui)
    colors = grimm[0]
    occurences = grimm[1]
    ax3 = sns.barplot(colors, occurences, palette = custom_palette)
    fig3 = ax3.get_figure()
    for item in ax3.get_xticklabels():
        item.set_rotation(45)
    sns.plt.title('Color Word Frequencies in Brothers Grimm Stories')
    fig3.savefig('grimm_chart.png')
    fig3.clf()
graph_func(andersen_color_freq)
graph_func2(perrault_color_freq)
graph_func3(grimm_color_freq)
