import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
root=tk.Tk()
root.title("contact book")
root.geometry("500x600")
root.resizable(0,0)

contdata=[]


def loadcontact():
    for item in recordtable.get_children():
        recordtable.delete(item)

    for r in range(len(contdata)):
        recordtable.insert(parent='',index='end',text='',iid=r,values=contdata[r])


def putcontinentry(index):
    stuname.delete(0,tk.END)
    stuphone.delete(0, tk.END)
    stumail.delete(0, tk.END)
    stuaddress.delete(0, tk.END)

    stunamee=contdata[index][0]
    stuphonee = contdata[index][1]
    stumaill = contdata[index][2]
    stuaddresss = contdata[index][3]

    stuname.insert(0,stunamee )
    stuphone.insert(0, stuphonee)
    stumail.insert(0, stumaill)
    stuaddress.insert(0, stuaddresss)


def cleardata():
    stuname.delete(0, tk.END)
    stuphone.delete(0, tk.END)
    stumail.delete(0, tk.END)
    stuaddress.delete(0, tk.END)
    searchent.delete(0,tk.END)
    loadcontact()

def addcontact(contname,contno,contemail,contaddress):
    contdata.append([contname,contno,contemail,contaddress])

    loadcontact()
    cleardata()

def updatecont(contname,contno,contemail,contaddress,index):
    contdata[index]=[contname,contno,contemail,contaddress]
    loadcontact()
    cleardata()

def deletecont(index):
    del contdata[index]
    loadcontact()
    cleardata()

def findcont(contname):
    if stuname !='':
        contdata_index=[]

        for data in contdata:
            if str(stuname) in str(data[0]):
                contdata_index.append(contdata.index(data))

        for item in recordtable.get_children():
            recordtable.delete(item)

        for r in contdata_index:
            recordtable.insert(parent='', index='end', text='', iid=r, values=contdata[r])
    else:
        loadcontact()


frame=tk.Frame(root)
heading=tk.Label(frame,text='Contact book',font=('bold',13),bg='blue',fg='white').pack(fill=tk.X,pady=5)
namee=tk.Label(frame,text="NAME :",font=('Bold',10)).place(x=0,y=50)
stuname=tk.Entry(frame,font=('Bold',10)).place(x=110,y=50,width=180)

namee=tk.Label(frame,text="NAME :",font=('Bold',10)).place(x=0,y=50)
stuname=tk.Entry(frame,font=('Bold',10))
stuname.place(x=110,y=50,width=180)

phone=tk.Label(frame,text="PHONE NO :",font=('Bold',10)).place(x=0,y=100)
stuphone=tk.Entry(frame,font=('Bold',10))
stuphone.place(x=110,y=100,width=180)

mail=tk.Label(frame,text="EMAIL :",font=('Bold',10)).place(x=0,y=150)
stumail=tk.Entry(frame,font=('Bold',10))
stumail.place(x=110,y=150,width=180)

address=tk.Label(frame,text="ADDRESS :",font=('Bold',10)).place(x=0,y=200)
stuaddress=tk.Entry(frame,font=('Bold',10))
stuaddress.place(x=110,y=200,width=180)

#buttons
add=tk.Button(frame,text='Add',font=('Bold',12),command=lambda: addcontact(stuname.get(),stuphone.get()
                                                                           ,stumail.get(),
                                                                           stuaddress.get()))

add.place(x=20,y=250)
update=tk.Button(frame,text='Update',font=('Bold',12),command=lambda: updatecont(stuname.get(),stuphone.get()
                                                                           ,stumail.get(),
                                                                           stuaddress.get(),index=int(recordtable.selection()[0])))
update.place(x=83,y=250)
delete=tk.Button(frame,text='Delete',font=('Bold',12),command=lambda: deletecont(index=int(recordtable.selection()[0])))
delete.place(x=163,y=250)
clear=tk.Button(frame,text='Clear',font=('Bold',12),command=lambda: cleardata())
clear.place(x=240,y=250)



frame.pack(pady=10)
frame.pack_propagate(False)
frame.configure(width=400,height=300)

search=tk.Frame(root)
searchlb=tk.Label(search,text="Search Contact by Name :",font=('Bold',10)).pack(anchor=tk.W)
searchent=tk.Entry(search,font=('Bold',10))
searchent.pack(anchor=tk.W)
searchent.bind('<KeyRelease>',lambda e: findcont(searchent.get()))

search.pack(pady=0)
search.pack_propagate(False)
search.configure(width=400,height=50)

recordframe=tk.Frame(root)
recordlb=tk.Label(recordframe,text='Select Record for delete or update',bg='red',font=('Bold',13))
recordlb.pack(fill=tk.X)

recordtable=ttk.Treeview(recordframe)
recordtable.pack(fill=tk.X,pady=5)

recordtable.bind('<<TreeviewSelect>>',lambda e: putcontinentry(int(recordtable.selection()[0])))
recordtable['columns']=('name','phone','email','address')
recordtable.column('#0',anchor=tk.W,width=0,stretch=tk.NO)
recordtable.column('name',anchor=tk.W,width=50)
recordtable.column('phone',anchor=tk.W,width=100)
recordtable.column('email',anchor=tk.W,width=120)
recordtable.column('address',anchor=tk.W,width=160)

recordtable.heading('name',anchor=tk.W,text='NAME')
recordtable.heading('phone',anchor=tk.W,text='PHONE NO')
recordtable.heading('email',anchor=tk.W,text='EMAIL')
recordtable.heading('address',anchor=tk.W,text='ADDRESS')
recordframe.pack(pady=10)
recordframe.pack_propagate(False)
recordframe.configure(width=400,height=200)

loadcontact()




root.mainloop()