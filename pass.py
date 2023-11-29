#password generator
import tkinter
import random
from tkinter import *
upc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smc="abcdefghijklmnopqrstuvwxyz"
num="1234567890"
sym="@$&"
up,sm,nu,sy=True,True,True,True
all=("")
if up:
    all+=upc
if sm:
    all+=smc
if nu:
    all+=num
if sy:
    all+=sym
root=Tk()
root.title("password generator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#004953")
inputtxt=int()
heading=Label(root,text='PASSWORD GENERATOR',font='arial 30 bold',fg='black',bg='#56C4C1')
heading.place(x=30,y=50)

ask=Label(root,text='Enter the length of password :',font='arial 15 italic',fg='black',bg='#56C4C1')
ask.place(x=30,y=200)

ask=Label(root,text='Random password generated :',font='arial 15 italic',fg='black',bg='#56C4C1')
ask.place(x=30,y=350)

ask=Label(root,bg='white')
ask.place(x=160,y=400,height=45,width=220)

en=Entry(font = ('courier', 15, 'bold'),textvariable = inputtxt)
en.place(x=160,y=250,height=45,width=220)
def get_value():
   global len
   len = int(en.get())
   amt = 1
   for x in range(amt):
      password = "".join(random.sample(all, len))
      op=Label(root, text=password, font=('Century 15 bold'))
      op.place(x=160, y=400, height=45, width=220)


def getu():
   amt = 1
   for x in range(amt):
      password = "".join(random.sample(all, len))
      op = Label(root, text=password, font=('Century 15 bold'))
      op.place(x=160, y=400, height=45, width=220)


button= Button(root, text="ENTER", command= get_value)
button.place(x=400,y=260)

button= Button(root, text="REGENERATE", command= getu)
button.place(x=400,y=415)




root.mainloop()