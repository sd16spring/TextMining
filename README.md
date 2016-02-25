This is a color frequency analysis tool. First, open pickling_import_text.py and run it - this will pickle the data for
project gutenberg books of grimm, perrault, and andersen fairy tales. Next, open text_filter.py and run it. This will
automatically output graphs of the color word frequencies in these tales, named grimm_chart.png, perrault_chart. png, and
 andersen_chart.png.

  If you would like to change the colors searched for in these tales, open text_filter.py and change the strings in COLORS
  (a global variable) to whatever you would like to be searched.  If you would like to use data other than the three fairy
  tales used automaticaly, change the get_text calls in pickling_import_text at the bottom of the file with the URL of the
  text file you would like analyze and the name you would like to use for it. Next, open text_filter.py and change the line at the bottom
  of the main section that says text_lists= text_import(['andersen', 'perrault', 'grimm']) to use the names that you used
  during pickling. You will get a list of dictionaries called output_dict which you can do whatever you like with.
  If you would like it to graph (and have those graphs make sense) while analyzing anything other than the set of fairytales
   mentioned above, you will need to change the text and variable names  used within the graphs or else they won't make much
   sense.