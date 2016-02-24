import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold
import pickle
import random



input_file = open('Wikipedia Med','r')
linksDict = pickle.load(input_file)	# get the dictionary of links
input_file.close()

dists = []
for title1 in linksDict:
	links1 = linksDict[title1]
	dists.append([])	# sets up the row
	for title2 in linksDict:
		links2 = linksDict[title2]
		if title1 == title2:
			dists[-1].append(0)
		else:
			dist12 = 7.389	# the default distance
			if title2 in links1:
				dist12 = dist12/2.718
			if title1 in links2:	# each link between them halves the distance
				dist12 = dist12/2.718
			dists[-1].append(dist12)

print "Catalogued!"

adist = np.array(dists)
amax = np.amax(adist)
adist /= amax

mds = manifold.MDS(n_components=2, dissimilarity="precomputed")
results = mds.fit(adist)

coords = results.embedding_

plt.subplots_adjust(bottom = 0.1)	# I think this part plots it. I don't really know; I just downloaded this part
plt.scatter(coords[:, 0], coords[:, 1], marker = 'o')

"""chance = 30.0/len(dists)
for label, x, y in zip(linksDict.keys(), coords[:, 0], coords[:, 1]):	# puts labels on it (for testing purposes only)
	if random.random() < chance:
	    plt.annotate(
	        label,
	        xy = (x, y), xytext = (-20, 20),
	        textcoords = 'offset points', ha = 'right', va = 'bottom',
	        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
	        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))"""

plt.show()