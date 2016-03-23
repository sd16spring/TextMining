""" CODE FOR SOFTDES MINI PROJECT 3: TEXT MINING
	SPRING 2016

	PLOTTING FUNCTION FOR BROKEN BELLS ANALYSIS
	### NOT FUNCTIONAL AS INDEPENDENT CODE ###

	@author: Gaby Clarke

"""


def plot(artist):
	""" uses matplotlib's scatter to plot each song by the given artist on a polar 
		plot, where the r-component of the position is the difference between the 
		polarity of that song and the average polarity of that artist's songs

		artist: artist name
		generates: polar plot of all songs by that artist according to the polarity
		of the lyrics
	"""
	data = analyzeAllLyrics(artist)
	comparison = compare(artist, data)

	ax = plt.subplot(111, projection='polar')

	ax.grid(True)
	ax.set_xticklabels(['', '', '', '', '', '', '', ''])
	ax.set_yticklabels(['', '', '', '', '', '', '', ''])
	

	deltaTheta = 2 * np.pi / len(comparison)
	index = 0
	

	# HARDCODING FOR DESIRED PLOT: BROKEN BELLS
	ax.set_title("Polarity of the Broken Bells' lyrics compared to the average polarity", va='bottom')
	
	# Albums
	BrokenBells = ['The-High-Road', 'Vaporize', 'Your-Head-Is-On-Fire', 'The-Ghost-Inside', 'Sailing-to-Nowhere', 'Trap-Doors', 'Citizen', 'October', 'Mongrel-Heart', 'The-Mall-&-Misery']
	MeyrinFields = ['Meyrin-Fields', 'Windows', 'An-Easy-Life', 'Heartless-Empire']
	AfterTheDisco = ['Perfect-World', 'After-the-Disco', 'Holding-On-for-Life', 'Leave-It-Alone', 'The-Changing-Lights', 'Control', 'Lazy-Wonderland', 'Medicine', "No-Matter-What-You're-Told", 'The-Angel-and-the-Fool', 'The-Remains-of-Rock-&-Roll']
	ItsThatTalkAgain = ["It's-That-Talk-Again"]

	# Colors for each album
	palevioletred = '#DB7093' # Broken Bells
	mediumaquarmarine = '#66CDAA' # Meyrin Fields
	darkmagenta = '#8B008B' # After the Disco
	dodgerblue = '#1E90FF' # It's That Talk Again



	for song in comparison:
		r = comparison.get(song)
		theta = index * deltaTheta

		if song in BrokenBells:
			bb = scatter(theta, r, s=100, c=palevioletred, linewidth=0, label='Broken Bells (2010)')
		elif song in MeyrinFields:
			mf = scatter(theta, r, s=100, c=mediumaquarmarine, linewidth=0, label='Meyrin Fields (2011)')
		elif song in AfterTheDisco:
			atd = scatter(theta, r, s=100, c=darkmagenta, linewidth=0, label='After The Disco (2014)')
		elif song in ItsThatTalkAgain:
			itta = scatter(theta, r, s=100, c=dodgerblue, linewidth=0, label="It's That Talk Again (2015)")
		
		index += 1

	legend(handles=[bb, mf, atd, itta], loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=4)	
	show()