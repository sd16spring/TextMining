# TextMining

Mining Youtube comments off the most popular videos of each Youtube-defined category. I do basic analysis on them like sentiment analysis([Pattern module](https://pypi.python.org/pypi/Pattern)), word frequency, spelling (word list from the [Moby Project](http://icon.shef.ac.uk/Moby/)), and common languages ([langdetect module](https://pypi.python.org/pypi/langdetect)), as well os k-means clustering ([scikit-learn](http://scikit-learn.org/stable/)).

All the comments have already been pulled (pulled February 2016), so running Analysis.py should show the output of all the analysis, and the clusters will be outputted to 'clusters.txt'.