"""
2. Show partywise seat share for following results of the Assembly Elections 2018
in a piechart.Party with highest percentage should be shown as detached (slightly). 

Madhya Pradesh	
	INC - Win (114)
        BJP - Win (15)
        Independent - Win (4)
        Others - Win (3)	
Rajasthan	
	INC - Win (99)
	BJP- Win (73)
	Independent- Win (3)
	Others- Win (14)
Chhattisgarh	
	INC- Win (68)
	BJP- Win (15)
	BSP+- Win (9)
	Others- Win (7)	
Telangana	
	TRS- Win (88)
	INC- Win (19)
	BJP- Win (1)
	Others- Win (11)	
Mizoram	
	MNF- Win (26)
	INC- Win (5)
	BJP- Win (1)
	Others- Win (8)	
"""

import matplotlib.pyplot as plt
fobj = plt.figure(figsize=(10,10))
s1 = fobj.add_subplot(321)
s2 = fobj.add_subplot(322)
s3 = fobj.add_subplot(323)
s4 = fobj.add_subplot(324)
s5 = fobj.add_subplot(325)
#states ='MP Raj Chh Tel Miz'.split()
P = 'INC BJP Ind Oth'.split()
P_seats = [114,15,4,3]
clrs = 'r y c g'.split()
expl=[0.1,0,0,0]
s1.pie(P_seats,shadow=True,colors=clrs,startangle=45,labels=P,explode=expl,autopct='%1.1f%%')
s1.set_title("MP")



state2_seats = [99,73,3,14]
expl=[0.1,0,0,0]
s2.pie(state2_seats,shadow=True,colors=clrs,startangle=45,labels=P,explode=expl,autopct='%1.1f%%')
s2.set_title("Rajasthan")


state3_seats = [68,15,9,7]
expl=[0.1,0,0,0]
s3.pie(state2_seats,shadow=True,colors=clrs,startangle=45,labels=P,explode=expl,autopct='%1.1f%%')
s3.set_title("Chhathisgarh")



state4_seats = [88,19,1,11]
expl=[0.1,0,0,0]
s4.pie(state2_seats,shadow=True,colors=clrs,startangle=45,labels=P,explode=expl,autopct='%1.1f%%')
s4.set_title("Telengana")

state5_seats = [99,73,3,14]
expl=[0.1,0,0,0]
s5.pie(state2_seats,shadow=True,colors=clrs,startangle=45,labels=P,explode=expl,autopct='%1.1f%%')
s5.set_title("Mizoram")

plt.show()

