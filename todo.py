import tkinter
from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("To-Do-List")
root.geometry("600x650+400+100")
root.resizable(False,False)

lst=[]
def add():
    task=entry.get()
    entry.delete(0,END)
    if task:
        fr=open("task.txt",'a')
        fr.write(f"\n{task}")
        box.insert(END,task)

def deletion():
    global lst
    task=str(box.get(ANCHOR))
    if task in lst:
        lst.remove(task)
        fz=open("task.txt",'w')
        fz.write(task+"\n")
    box.delete(ANCHOR)

def delall():
    box.delete(0,tkinter.END)

def taskfile():
    try:
        global lst
        fh=open("task.txt","r")
        rd=fh.readlines()
        for task in rd:
            if task!='\n':
                lst.append(task)
                box.insert(END,task)
    except:
        file=open("task.txt",'w')
        file.close()
#img=ImageTk.PhotoImage(file="sc.png")
#imlab=Label(root,image=img)
#imlab.grid(row=0,column=0)

imge=ImageTk.PhotoImage(file="blue.jpg")
imlabr=Label(root,image=imge,bg="#32405b").place(x=0,y=0)


heading=Label(root,text='ALL TASK',font='arial 30 bold',fg='black',bg='#56C4C1')
heading.place(x=200,y=50)
frame=Frame(root,width=1000,height=50,bg='white')
frame.place(x=0,y=180)
write=StringVar()
entry=Entry(frame,width=24,font='arial 20',bd=0)
entry.place(x=120,y=7)
entry.focus()
button=Button(frame,text="+",font='arial 20 bold',width=6,bg='#5a95ff',fg='#fff',bd=0,command=add)
button.place(x=500,y=0)


fr=Frame(root,bd=3,width=700,height=320,bg='#32405b')
fr.pack(pady=(260,0))

box=Listbox(fr,font=("arial",12),width=60,height=16,bg='#32405b',fg='white',cursor='hand2',selectbackground='#5a95ff')
box.pack(side=LEFT , fill=BOTH,padx=2)
scrolly = Scrollbar(fr)
scrolly.pack(side=RIGHT,fill=BOTH)
box.config(yscrollcommand=scrolly.set)
scrolly.config(command=box.yview())

taskfile()
dele=PhotoImage(file="del.png")
Button(root,image=dele,bd=0,command=deletion).pack(side=BOTTOM,pady=13)

buttoni=Button(frame,text="-",font='arial 20 bold',width=6,bg='#5a95ff',fg='#fff',bd=0,command=delall)
buttoni.place(x=0,y=0)
root.mainloop()