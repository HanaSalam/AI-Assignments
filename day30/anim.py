
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


#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anm
fo=plt.figure(figsize=(6,6))
so=fo.add_subplot(111)
x=np.arange(4)
xlabels='sony mi lg asus'.split()
sa = [10,20,30,40,50]
bc1=so.bar(x,0,align='center')
so.set_xticks(x)
so.set_xticklabels(xlabels)
so.set_yticks(sa)
def animbar(i):
 global bc1
 sa=np.random.randint(1,90,4)
 print sa
 for bar1,h1 in zip(bc1,sa):
  bar1.set_height(h1)
 return bc1
anm1=anm.FuncAnimation(fo,animbar,interval=3000)
plt.show()
"""
def animbar(i):
 global bc1
 sa = open('a1.txt','r').readlines()
 print list(sa)
 for line in sa:
  print line
 #sa=np.random.randint(1,50,4)
 #print sa
 for line in sa:
  print line
  for bar1,h1 in zip(bc1,sa):
   bar1.set_height(h1)
  return bc1
anm1=anm.FuncAnimation(fo,animbar,interval=3000)
plt.show()

"""
