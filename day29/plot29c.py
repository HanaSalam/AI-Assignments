"""
3. Using the following data, draw a bar chart to show monthwise High/Low temperature in Kerala state.
	Months should be in X axis. There should be two bars for each month, one for High and the other for Low. 

	Jan	Feb	Mar	Apr	May	Jun	Jul	Aug	Sep	Oct	Nov	Dec
HighC	32	32	33	33	32	30	30	30	30	30	31	31

LowC	23	23	24	25	25	24	24	24	24	24	23	23

4. Draw a horizontal bar chart for the above problem.

"""
import matplotlib.pyplot as plt
import numpy as np

fobj1 = plt.figure(figsize=(8,8))
sub1 = fobj1.add_subplot(111)

month = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
x_val = np.arange(len(month))

high = [32,32,33,33,32,30,30,30,30,30,31,31]
low = [23,23,24,25,25,24,24,24,24,24,23,23]

bar_width = 0.3

sub1.bar(x_val,high,color='b',alpha=0.5,label='high',width=bar_width)
sub1.bar(x_val+bar_width,low,label='low',width=bar_width,alpha=0.5,color='r')

sub1.set_xticks(x_val+bar_width)
sub1.set_xticklabels(month)
sub1.set_xlabel('Months')
sub1.set_ylabel('Temperature')
sub1.set_title('Temp in Kerala')


#4. Draw a horizontal bar chart for the above problem.

fobj2 = plt.figure(figsize=(8,8))
sub2 = fobj2.add_subplot(111)

sub2.barh(x_val,high,color='b',alpha=0.5,label='high',height=bar_width)
sub2.barh(x_val+bar_width,low,label='low',height=bar_width,alpha=0.5,color='r')

sub2.set_yticks(x_val+bar_width)
sub2.set_yticklabels(month)
sub2.set_ylabel('Months')
sub2.set_xlabel('Temperature')
sub2.set_title('Temp in Kerala(Horizontal bar chart)')

plt.show()


