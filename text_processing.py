def processing_file(filename):
	"""processing initial file, stripping out guttenberg extra stuff"""
	fp = open(filename)
	all_text = fp.read()
	index_start = all_text.find('CONTENTS')
	index_end = all_text.find('End of Project Gutenberg')
	content =  all_text[index_start: index_end]
	

	new_story = []
	for line in content.split('\n'):
		if any_lowercase(line):
			new_story.append(line)
			
	story = ''.join(new_story)
	return story
	   

def any_lowercase(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



processing_file('grimm_fairytales.txt')