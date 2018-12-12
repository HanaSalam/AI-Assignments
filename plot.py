"""
 
1. Analyse and Execute all the given sample programs(Common/Python_Exercises/MPL_Samples).

2.Create a plot with different linestyle,color and marker for ,say, numbers less than 
50 and greater than or equal to 50 for an array of 10 random integers between 1 and 100
steps
		1. import pyplot and numpy
		2. create figure 
		3. add a subplot
		4. create and store 10 random integers between 1 and 100 in y array
		5. split the array into two y1 and y2. hint:less than 50 in y1 ,others in y2,boolen indexing 
		6. store last element of y1 as first in y2: hint numpy.insert(array,index,value)
		7. create 10 even numbers in x array hint arange
		8. call plot of step3 return value by supplying x array containg index values 0 thru size of y1
		9. again call plot of step3 return value by supplying the required values
		10. show the figure
		
	 	
  
"""

import matplotlib.pyplot as plt
import numpy as np
obj = plt.figure(figsize=(6,4),facecolor='0.8')
sobj1 = obj.add_subplot(221)
y = np.random.randint(1,100,10)
print 'y= ',y
y = np.sort(y)
print 'sort',y
y1 = y[y<50]
print 'y1= ',y1,y1.size
y2 = y[y>50]
#print y2

y2 = np.insert(y2,0,y1[y1.size-1])
print 'y2= ',y2

x = np.arange(2,21,2)
print 'x= ',x
sobj1.plot(x[:y1.size],y1,'ro:',marker='o')
sobj1.plot(x[y1.size-1:],y2,'bo:',marker='+')
plt.show()
