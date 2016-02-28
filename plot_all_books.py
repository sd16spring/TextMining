import plotly.plotly as plot
import plotly.graph_objs as maketrace
from one_book_sentiment import *

# x0y0 = plot_storyline('Clotelle.txt')
trace0 = maketrace.Scatter( x = x0y0[0], y = x0y0[1], name = 'Clotelle',
	line = dict(color = ('rgb(205, 12, 24)'), width = 4))

# x1y1 = plot_storyline('Garies.txt')
trace1 = maketrace.Scatter( x = x1y1[0], y = x1y1[1], name = 'The Garies and Their Friends',
	line = dict(color = ('rgb(205, 12, 24)'), width = 4, dash = 'dash'))

# x2y2 = plot_storyline('OurNig.txt')
trace2 = maketrace.Scatter( x = x2y2[0], y = x2y2[1], name = 'Our Nig',
	line = dict(color = ('rgb(205, 12, 24)'), width = 4, dash = 'dashdot'))

# x3y3 = plot_storyline('UncleToms.txt')
trace3 = maketrace.Scatter( x = x3y3[0], y = x3y3[1], name = "Uncle Tom's Cabin",
	line = dict(color = ('rgb(205, 12, 24)'), width = 4, dash = 'dot'))

print "Part 1 Done"
###

# x4y4 = plot_storyline('Lamplighter.txt')
trace4 = maketrace.Scatter( x = x4y4[0], y = x4y4[1], name = 'The Lamplighter',
	line = dict(color = ('rgb(22, 96, 167)'), width = 4))

# x5y5 = plot_storyline('Malaeska.txt')
trace5 = maketrace.Scatter( x = x5y5[0], y = x5y5[1], name = 'Malaeska',
	line = dict(color = ('rgb(22, 96, 167)'), width = 4, dash = 'dash'))

# x6y6 = plot_storyline('MobyDick.txt')
trace6 = maketrace.Scatter( x = x6y6[0], y = x6y6[1], name = 'Moby Dick',
	line = dict(color = ('rgb(22, 96, 167)'), width = 4, dash = 'dashdot'))

# x7y7 = plot_storyline('ScarletLetter.txt')
trace7 = maketrace.Scatter( x = x7y7[0], y = x7y7[1], name = 'The Scarlet Letter',
	line = dict(color = ('rgb(22, 96, 167)'), width = 4, dash = 'dot'))

print "Part 2 Done"
###
data = [trace0, trace1, trace2, trace3, trace4, trace5, trace6, trace7]
layout = dict(title = 'Storyline Sentiment in Eight 1850s Novels: Contrasting black and white authors',
              xaxis = dict(title = 'Progression through novel'),
              yaxis = dict(title = 'Sentiment Value'),
              )

plot.iplot(dict(data=data, layout=layout), filename='allbooks-plot')