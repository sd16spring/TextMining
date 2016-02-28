import pickle


def remove_junk_beginning(textBody):
	''' Trims unnecessary stuff off the beginning of a gutenberg book.
		Looks for 'chapter 1' or 'chapter I' and returns everything after that.
		Input is textBody, the text of the book file.
		Outputs the sliced text unless Chapter 1/I never makes an appearance, then outputs None.'''
	
	index = textBody.lower().find('chapter 1')
	alt_index = textBody.lower().find('chapter i')

	if index >= 0:
		return textBody[index:]
	elif alt_index >= 0:
		return textBody[alt_index:]
	else:
		print "You've already trimmed that shiz down!"
		return None

def remove_junk_end(textBody):
	''' Trims unnecessary stuff off the end of a gutenberg book.
		Finds the index of the first mention of Gutenberg (happens once the actual book content is over)
		and returns everything before that.
		Input is textBody, the text of the book file
		Outputs the sliced text unless 'Gutenberg' never makes an appearance, then outputs None.'''
	index = textBody.lower().find('gutenberg')
	if index >= 0:
		return textBody[:index]

	else:
		print "You've already trimmed that shiz down!"
		return None


def trim_booktext(file_name):
	''' Input book file name (string);
		this function trims off anything before Chapter 1 and after the end of the novel.
		Re-saves text file once it's trimmed so you only need run it once.
		Returns None.'''
	#Open er up
	f = open(file_name,'r')
	full_text = f.read()
	f.close()

	#Process: delete everything before the start of chapter 1 
	trimmed_text = remove_junk_beginning(full_text)
	trimmed_text = remove_junk_end(trimmed_text)

	#Rewrite the file w/trimmed version
	f = open(file_name,'w')
	f.write(trimmed_text)
	f.close
	print 'Done!'


#Trim down the books to just the body, no extra junk
for fileName in ['Clotelle.txt', 'Malaeska.txt', 'Lamplighter.txt', 'MobyDick.txt', 'ScarletLetter.txt', 'UncleToms.txt', 'Garies.txt', 'OurNig.txt']:
	trim_booktext(fileName)
