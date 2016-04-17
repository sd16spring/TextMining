""" This code was written by Rebecca Gettys, except where otherwise noted.  """
#### MAIN SECIOTN ####
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





def tale_slicing(tale):
    """Slices the tales (strings) up into a list of words without spaces or punctuation
     NOTE: https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal method that I used
    Arguments: list of strings (texts of the gutenberg tales)
    Returns: lists of words"""
    tale_no_punc = ''
    for char in tale: #killing punctuation
        if not is_punct_char(char):
            tale_no_punc = tale_no_punc+char #so extend the string everytime we run into a letter
    list_of_words = []
    list_of_words = tale_no_punc.split( ) #splitting the string into the list)
    return list_of_words





def is_punct_char(char):
    """From python.org (link above), all this does is check if a character is puncutation or not! the ultimate helper funcion!
    Arguments: character
    Returns: True/False if the character it is given is a puncuation mark - 1 is punctuation, 0 is not """
    return char in string.punctuation #1 is punctuation, 0 is not punctuation




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

### END OF MAIN SECTION ###

### GRAPHING AND DATA PROCESSING ###



## patrick is amazing for helping with this!!



def universal_graph_func(text_variable,title_string,save_file_name_string):
    sns.set(font_scale=.8)
    sns.axlabel('Color', 'Frequency')
    # colors from http://www.color-hex.com and wikipedia
    flatui = ["#4b0082", "#ffd700", "#e6e6fa", "#ffff00", "#FF2400", "#ff6eb4", "#d2b48c", "#ff00ff", "#0000ff",
              "#C8A2C8",
              "#800080", "#FF007F", "#FD3F92", "#000000", "#dc143c", "#CCCCFF", "#ffffff", "#ff0000", "#631919",
              "#fffff0",
              "#ffa500", "#730000", "#808000", "#00ffff", "#c0c0c0", "#808080", "#7fffd4", "#808080", "#008000",
              "#f5f5dc",
              "#329999", "#f0ffff", "#FFEF00"]
    custom_palette = sns.color_palette(flatui)
    colors = text_variable[0]
    occurences = text_variable[1]
    ax = sns.barplot(colors, occurences, palette = custom_palette)
    fig = ax.get_figure()
    for item in ax.get_xticklabels():
        item.set_rotation(45)
    sns.plt.title(title_string)
    fig.savefig(save_file_name_string)
    fig.clf()



