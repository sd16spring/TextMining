

import pickle 

#Step 1: Get text file (done in code before.) 
#Step 2: Search for words (searchable_words)
#Step 3: Count the words (return the number of each word within a file.)
#Step 4: Save these words. 
#Step 5: Move on to the next file (repeat)

search_terms = ['cloning', 'genetic engineering', 'gene therapy', 'CRISPR', 'genetically modified organisms', 'genetics', 'conservation genetics']
negative_searchable_words = ['not', 'no', 'lack', 'questionable', 'cannot', 'controversial', 'controversy', 'painful', 'bad', 'beneath', "can't", 'confused', 'contradictory', 'contrary', 'corrupt', 'cruel', 'dead', 'decaying', 'damaging', 'deplorable', 'deformed', 'deny', 'detrimental', 'dirty', 'cold', 'dishonest', 'disheveled', 'dismal', 'distress', "don't", 'enraged', 'eroding', 'fail', 'faulty', 'fear', 'feeble', 'filthy', 'frighten', 'gruesome', 'grim', 'grotesque', 'guilty', 'hard', 'harmful', 'hate', 'horrible', 'hostile', 'hurt', 'hurtful', 'ignore', 'ignorant', 'ill', 'immature', 'imperfect', 'impossible', 'inane', 'inelegant', 'infernal', 'injure', 'injurious', 'insane', 'insidious', 'insipid', 'jealous', 'junky', 'lose', 'lousy', 'lumpy', 'malicious', 'mean', 'menacing', 'messy', 'misshapen', 'missing', 'misunderstood', 'moan', 'moldy', 'monstrous', 'naive', 'nasty', 'naughty', 'negate', 'negative', 'never', 'no', 'nobody', 'nondescript', 'nonsense', 'noxious', 'objectionable', 'odious', 'offensive', 'old', 'oppressive', 'pain', 'perturb', 'pessimistic', 'petty', 'plain', 'poisonous', 'poor', 'prejudice', 'questionable', 'quirky', 'quit', 'reject', 'renege', 'repellant', 'reptilian', 'repulsive', 'repugnant', 'revenge', 'revolting', 'rocky', 'rotten', 'rude', 'ruthless', 'sad', 'savage', 'scare', 'scary', 'scream', 'severe', 'shoddy', 'shocking', 'sick', 'sickening', 'sinister', 'slimy', 'smelly', 'sobbing', 'sorry', 'spiteful', 'sticky', 'stinky', 'stormy', 'stressful', 'stuck', 'stupid', 'substandard', 'suspect', 'suspicious', 'tense', 'terrible', 'terrifying', 'threatening', 'ugly', 'undermine', 'unfair', 'unfavorable', 'unhappy', 'unhealthy', 'unjust', 'unlucky', 'unpleasant', 'upset', 'unsatisfactory', 'unsightly', 'untoward', 'unwanted', 'unwelcome', 'unwholesome', 'unwieldy', 'unwise', 'vice', 'vicious', 'vile', 'villainous', 'vindictive', 'wary', 'weary', 'wicked', 'woeful', 'worthless', 'wound', 'yell', 'yucky', 'zero']
positive_searchable_words = ['trusted', 'reliable', 'safe', 'effective', 'helpful', 'can', 'capable', 'absolutely', 'adorable', 'accepted', 'acclaimed', 'accomplish', 'accomplishment', 'achievement', 'action', 'active', 'admire', 'adventure', 'affirmative', 'affluent', 'agree', 'agreeable', 'amazing', 'angelic', 'appealing', 'approve', 'aptitude', 'attractive', 'awesome', 'beaming', 'beautiful', 'believe', 'beneficial', 'bliss', 'bountiful', 'bounty', 'brave', 'bravo', 'brilliant', 'bubbly', 'calm', 'celebrated', 'certain', 'champ', 'champion', 'charming', 'cheery', 'choice', 'classic', 'classical', 'clean', 'commend', 'composed', 'congratulation', 'constant', 'cool', 'courageous', 'creative', 'cute', 'dazzling', 'delight', 'delightful', 'distinguished', 'divine', 'earnest', 'easy', 'ecstatic', 'effective', 'effervescent', 'efficient', 'effortless', 'electrifying', 'elegant', 'enchanting', 'encouraging', 'endorsed', 'energetic', 'energized', 'engaging', 'enthusiastic', 'essential', 'esteemed', 'ethical', 'excellent', 'exciting', 'exquisite', 'fabulous', 'fair', 'familiar', 'famous', 'fantastic', 'favorable', 'fetching', 'fine', 'fitting', 'flourishing', 'fortunate', 'free', 'fresh', 'friendly', 'fun', 'funny', 'generous', 'genius', 'genuine', 'giving', 'glamorous', 'glowing', 'good', 'gorgeous', 'graceful', 'great', 'green', 'grin', 'growing', 'handsome', 'happy', 'harmonious', 'healing', 'healthy', 'hearty', 'heavenly', 'honest', 'honorable', 'honored', 'hug', 'idea', 'ideal', 'imaginative', 'imagine', 'impressive', 'independent', 'innovate', 'innovative', 'instant', 'instantaneous', 'instinctive', 'intuitive', 'intellectual', 'intelligent', 'inventive', 'jovial', 'joy', 'jubilant', 'keen', 'kind', 'knowing', 'knowledgeable', 'laugh', 'legendary', 'light', 'learned', 'lively', 'lovely', 'lucid', 'lucky', 'luminous', 'marvelous', 'masterful', 'meaningful', 'merit', 'meritorious', 'miraculous', 'motivating', 'moving', 'natural', 'nice', 'novel', 'now', 'nurturing', 'nutritious', 'okay', 'one', 'one-hundred percent', 'open', 'optimistic', 'paradise', 'perfect', 'phenomenal', 'pleasurable', 'plentiful', 'pleasant', 'poised', 'polished', 'popular', 'positive', 'powerful', 'prepared', 'pretty', 'principled', 'productive', 'progress', 'prominent', 'protected', 'proud', 'quality', 'quick', 'quiet', 'ready', 'reassuring', 'refined', 'refreshing', 'rejoice', 'reliable', 'remarkable', 'resounding', 'respected', 'restored', 'reward', 'rewarding', 'right', 'robust', 'safe', 'satisfactory', 'secure', 'seemly', 'simple', 'skilled', 'skillful', 'smile', 'soulful', 'sparkling', 'special', 'spirited', 'spiritual', 'stirring', 'stupendous', 'stunning', 'success', 'successful', 'sunny', 'super', 'superb', 'supporting', 'surprising', 'terrific', 'thorough', 'thrilling', 'thriving', 'tops', 'tranquil', 'transforming', 'transformative', 'trusting', 'truthful', 'unreal', 'unwavering', 'up', 'upbeat', 'upright', 'upstanding', 'valued', 'vibrant', 'victorious', 'victory', 'vigorous', 'virtuous', 'vital', 'vivacious', 'wealthy', 'welcome', 'well', 'whole', 'wholesome', 'willing', 'wonderful', 'wondrous', 'worthy', 'wow', 'yes', 'yummy', 'zeal', 'zealous']
s = ('cloning', 'genetic engineering')
neg = 'no'
pos = 'yes'
z = 0 , ''



def search_neg_pos (article_names, negative_search_words, positive_search_words): 
	''' This runs some examples 
	>>> s = ('cloning', 'genetic engineering')
	>>> neg = 'no'
	>>> pos = 'yes'
	>>> search_neg_pos(s, neg , pos)
	cloning : negative = 0
           positive = 2


	genetic engineering : negative = 0
	           positive = 1


	>>> search_neg_pos('', '', '')

	'''
	for element in article_names: 
		file = open(element +'.txt', 'r')
		n = dict()
		p = dict() 
		for line in file: 
			# Save data to a file (will be part of your data fetching script)
			b = line.split()
			for word in b: 
				for myword in negative_search_words: 
					if myword == word:
						n[myword] = n.get(myword, 0) + 1
				negative = sum(n.values())
		print element, ':', 'negative', '=', negative  
		file.seek(0)
		for line in file: 
			# Save data to a file (will be part of your data fetching script)
			b = line.split() 
			for word1 in b: 
				for myword1 in positive_search_words: 
					if myword1 == word1:
						p[myword1] = p.get(myword1, 0) + 1
					positive = sum(p.values()) 
		print ' ' * 10, 'positive', '=', positive
		print '\n'

search_neg_pos(search_terms, negative_searchable_words, positive_searchable_words)