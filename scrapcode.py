# from pattern.web import *
import pickle 
text_names=['prince','Dickens-Great_expectations',
'Austen-Love_and_friendship','Austen-Persuasion','Austen-Sense_and_sensibility',
'Bronte-Wuthering_heights','Austen-Emma',
'Dickens-A_tale_of_two_cities','Sand-La_mare_au_Diable','Sand-Correspondance1','Sand-Correspondance2'
'Sand-Correspondance3','Sand-Correspondance4','Sand-Correspondance5',
'Sand-Elle_et_lui','Sand-hiver_a_majorque','Sand-contes_une_grand_mere',
'Sand-Andre','Sand-Le_petit_fadette','Sand-Pauline']

pickle_files=[x+'.pickle' for x in text_names]

pickle_files.sort()
print (pickle_files)

# #To get from wikipedia:
# w=Wikipedia()
# article=w.search('Le Petit Prince')
# source_text=article.string
# text_name='Bronte-Wuthering_heights'

# # Downloding from link:

# link='http://www.gutenberg.org/cache/epub/768/pg768.txt'

# source_text= URL(link).download()

# file = open(text_name+'.pickle','w')
# pickle.dump(source_text,file)
# file.close()

# input_file=open(text_name+'.pickle','r',encoding='utf8')
# text = pickle.load(input_file)

# print source_text[:80]

# print source_text.string.encode('utf8')

# #Google translate is a paid service?
# s="Moi,je suis chinoise."
# g = Google()
# print g.translate(s, input='fr', output='en', cached=False)
# print g.identify(s)



# titles=w.index()
# counter=1
# while counter<100:
# 	print next(titles).encode('utf8')
# 	counter+=1