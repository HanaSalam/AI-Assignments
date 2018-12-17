"""
2.Draw an animated bar chart for the sales of four mobile brands

	brand 	initial stock
	sony	50
	mi	50
	lg	50
	Asus	50

	 Upon starting the program the sales qty will be 0s and hence the bar heights are 0s.
	 max height of the bar may be 50(should be shown in Y)
	 the program should collect the sales of each item (via mysql/text file/etc.)
	 and should update the graph.
"""
import matplotlib.pyplot as plt
import numpy as np
import time
brand = 'sony mi lg asus'.split()
print np.zeros((1,4),dtype=)
