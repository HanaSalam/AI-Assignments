"""
1.In Tom's icecream shop,he observed and drawn a chart for the number of hours of sunshine vs
 the number of icecreams sold as follows.

	hours of sunshine	icecreams sold
	2			4
	3			5
	5			7
	7			10
	9			15 

	Draw a line of best fit for the above.
"""

import scipy as sp
import numpy as np
import scipy.optimize as spo
import matplotlib.pyplot as plt
x = np.array([2,3,5,7,9])
y = np.array([4,5,7,10,15])
f1 = lambda m,x,c:m*x+c

opt,cov = spo.curve_fit(f1,x,y)
print opt
print 'm=',opt[0],'\t','c=',opt[1]


#to get y value with new value of x
print 'y=',f1(opt[0],10,opt[1]),' for x=10'

vf1 = sp.vectorize(f1)
#calculated y =cy
cy = vf1(opt[0],x,opt[1])
print 'observed values-y:',y
print 'calculated values-cy:',cy

plt.plot(x,y,'r:o',label='observed')
plt.plot(x,cy,'b-v',label='calculated')
plt.legend(loc = 'best')
plt.show()
