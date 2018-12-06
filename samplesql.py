from Tkinter import *
import MySQLdb as db
mwin = Tk()
mwin.title('Database')
con = db.connect("127.0.0.1", "root", "", "test")
cur = con.cursor()
def insert(a,b,c,d):
    q1 = "insert into testtable values(%s,'%s','%s',%s)"%(a,b,c,d)
    cur.execute(q1)
    con.commit()

def getdata(x):
    q2 = "select * from testtable where eno = %s"% x
    cur.execute(q2)
    #res = list()
    res = cur.fetchall()
    for item in res:
        t1.set(item[0])
        t2.set(item[1])
        t3.set(item[2])
        t4.set(item[3])


lb0 = Label(mwin)
lb0.config(text='Insert/Retrieve data')

lb1 = Label(mwin)
lb1.config(text='Id')

lb2 = Label(mwin)
lb2.config(text='Name')

lb3 = Label(mwin)
lb3.config(text='Designation')

lb4 = Label(mwin)
lb4.config(text='Salary')

t1 = StringVar()
tb1 = Entry(mwin,textvariable = t1)
t2 = StringVar()
tb2 = Entry(mwin,textvariable = t2)
t3 = StringVar()
tb3 = Entry(mwin,textvariable = t3)
t4 = StringVar()
tb4 = Entry(mwin,textvariable = t4)




b1 = Button(mwin,text = 'Insert',command = lambda:insert(tb1.get(),tb2.get(),tb3.get(),tb4.get()))
b2 = Button(mwin,text = 'Retrieve',command = lambda:getdata(tb1.get()))


lb0.grid(row=0,column=0)
lb1.grid(row=1,column=0)
lb2.grid(row=2,column=0)
lb3.grid(row=3,column=0)
lb4.grid(row=4,column=0)
tb1.grid(row=1,column=3)
tb2.grid(row=2,column=3)
tb3.grid(row=3,column=3)
tb4.grid(row=4,column=3)
b1.grid(row=5,column=1,columnspan=2)
b2.grid(row=5,column=2,columnspan=2)
mwin.mainloop()