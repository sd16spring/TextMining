from pickling_import_text import *
from text_filter import *
import sys


#def run_func(name_string = 'grimm', url_string='http://www.gutenberg.org/cache/epub/2591/pg2591.txt', graph_title_string='Color Word Frequencies in Brothers Grimm Stories', save_image_string = 'grimm_chart.png'):
def run_func(name_string, url_string, graph_title_string, save_image_string):
    get_text(url_string,name_string)
    a_text=text_importing(name_string)
    tale_list_of_words = tale_slicing(a_text)
    tale_dict = color_searching (tale_list_of_words)
    item_dump_list = tale_dict.items()
    tale_color_freq = list_dumping(item_dump_list)
    universal_graph_func(tale_color_freq,graph_title_string,save_image_string)



user_input_name = raw_input("Please input a Name of Story (letters and underscores only)")
user_input_url = raw_input("Please input a URL to a text file to be analysed")
user_input_title = raw_input("Please input what your desired title for the graph that will be generated")
user_input_save = raw_input("Please input the file name you would like the graph to be saved to (letters and underscores only)") + '.png'

run_func(user_input_name,user_input_url, user_input_title, user_input_save)



#if len(sys.argv) ==0:
#    run_func()
#elif len(sys.argv) ==4:
#    run_func(name_string=str(sys.argv[0]) , url_string=str(sys.argv[1]),
#             graph_title_string=str(sys.argv[2]), save_image_string= str(sys.argv[3]))

#else:
#    print "Incorrect Number of Arguements. Please run without arguements for Grimm anaylsis or follow the following format: name url graph_title save_image_name)





#run_func('grimm', 'http://www.gutenberg.org/cache/epub/2591/pg2591.txt','Color Word Frequencies in Brothers Grimm Stories', 'grimm_chart_2.png' )
#run_func('perrault','https://ia600302.us.archive.org/15/items/thefairytalesofc29021gut/pg29021.txt', 'Color Word Frequencies in Charles Perrault Stories','perrault_chart_2.png', "perrault_chart_2.png")
#run_func('andersen','https://archive.org/download/fairytalesofhans27200gut/27200.txt', 'Color Word Frequencies in Hans Christian Andersen Stories', 'andersen_chart_2.png')

