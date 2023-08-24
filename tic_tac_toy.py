from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
ActivePlayer=1
p1=[]
p2=[]

root=Tk()
root.title('Tix Tak Toy')


b1=ttk.Button(root,text=' ')
b1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
b1.config(command=lambda: bu_clik(1))
b2=ttk.Button(root,text=' ')
b2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
b2.config(command=lambda: bu_clik(2))
b3=ttk.Button(root,text=' ')
b3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
b3.config(command=lambda: bu_clik(3))

b4=ttk.Button(root,text=' ')
b4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
b4.config(command=lambda: bu_clik(4))
b5=ttk.Button(root,text=' ')
b5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
b5.config(command=lambda: bu_clik(5))
b6=ttk.Button(root,text=' ')
b6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
b6.config(command=lambda: bu_clik(6))

b7=ttk.Button(root,text=' ')
b7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
b7.config(command=lambda: bu_clik(7))

b8=ttk.Button(root,text=' ')
b8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
b8.config(command=lambda: bu_clik(8))

b9=ttk.Button(root,text=' ')
b9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
b9.config(command=lambda: bu_clik(9))

def bu_clik(id):
    global ActivePlayer
    global p1
    global p2
    if (ActivePlayer==1):
        setl(id, 'X')
        p1.append(id)
        root.title('Tix Tak Toy: Player 2')
        ActivePlayer=2
        print('p1{}'.format(p1))
        #bot()
    elif (ActivePlayer == 2):
        setl(id,'O')
        p2.append(id)
        root.title('Tix Tak Toy: Player 1')
        ActivePlayer=1
        print('p2{}'.format(p2))
    winer()
def setl(id,text):
    if id==1:
        b1.config(text=text)
        b1.state(['disabled'])
    elif id==2:
        b2.config(text=text)
        b2.state(['disabled'])
    elif id==3:
        b3.config(text=text)
        b3.state(['disabled'])
    elif id==4:
        b4.config(text=text)
        b4.state(['disabled'])
    elif id==5:
        b5.config(text=text)
        b5.state(['disabled'])
    elif id==6:
        b6.config(text=text)
        b6.state(['disabled'])
    elif id==7:
        b7.config(text=text)
        b7.state(['disabled'])
    elif id==8:
        b8.config(text=text)
        b8.state(['disabled'])

    elif id==9:
        b9.config(text=text)
        b9.state(['disabled'])
def winer():
    winer=-1
    if (1 in p1) and (2 in p1) and (3 in p1):
        winer=1
        root.title('Tix Tak Toy: Player 1 is the winer')
    elif (4 in p1) and (5 in p1) and (6 in p1):
        winer=1
        root.title('Tix Tak Toy: Player 1 is the winer')
    elif (7 in p1) and (8 in p1) and (9 in p1):
        winer=1

    elif (1 in p1) and (4 in p1) and (7 in p1):
        winer=1

    elif (2 in p1) and (5 in p1) and (8 in p1):
        winer=1

    elif (3 in p1) and (6 in p1) and (9 in p1):
        winer=1

    elif (1 in p1) and (5 in p1) and (9 in p1):
        winer=1

    elif (3 in p1) and (5 in p1) and (7 in p1):
        winer=1

    if (1 in p2) and (2 in p2) and( 3 in p2):
        winer=2
    elif (4 in p2) and (5 in p2) and (6 in p2):
        winer=2
    elif (7 in p2) and (8 in p2) and (9 in p2):
        winer=2
    elif (1 in p2) and (4 in p2) and (7 in p2):
        winer=2
    elif (2 in p2) and (5 in p2) and (8 in p2):
        winer=2
    elif (3 in p2) and (6 in p2) and (9 in p2):
        winer=2
    elif (1 in p2) and (5 in p2) and (9 in p2):
        winer=2
    elif (3 in p2) and (5 in p2) and (7 in p2):
        winer=2
    if winer == 1:
        messagebox.showinfo(title='we have a win', message='player 1 is the winer')
    elif winer == 2:
        messagebox.showinfo(title='we have a win', message='player 2 is the winer')

def bot():
    global p1
    global p2
    ec=[]
    for e in range(9):
        if(not (e+1 in p1)or(e+1 in p2)):
            ec.append(e+1)
    #ranind=randint(0,len(ec)-1)
    #bu_clik(ranind)
    #if ActivePlayer == b1:
     #   if b5 in ec:
      #      buclik(b5)


#def AI()
root.mainloop()
