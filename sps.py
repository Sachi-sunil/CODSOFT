import tkinter
from tkinter import *
from PIL import Image,ImageTk
from random import randint

root=Tk()
root.title("Rock-Paper-Scissor")
root.configure(background="lavender")


rock=ImageTk.PhotoImage(Image.open("rock.png"))
paper=ImageTk.PhotoImage(Image.open("paper.png"))
sci=ImageTk.PhotoImage(Image.open("scissor.png"))
scicomp=ImageTk.PhotoImage(Image.open("scissorcomp.png"))
rockcomp=ImageTk.PhotoImage(Image.open("rockcomp.png"))
papercomp=ImageTk.PhotoImage(Image.open("papercomp.png"))

user=Label(root,image=sci,bg="lavender",width=500).grid(row=1,column=4)
comp=Label(root,image=scicomp,bg="lavender",width=500).grid(row=1,column=0)

playerscore=Label(root,text=0,font=100,bg="lavender",fg='black').grid(row=1,column=3)
compscore=Label(root,text=0,font=100,bg="lavender",fg='black').grid(row=1,column=1)

us=Label(root,font=('Times', 24),text="USER",bg="lavender",fg='black').grid(row=0,column=3)
com=Label(root,font=('Times', 24),text="COMPUTER",bg="lavender",fg='black').grid(row=0,column=1)

msg=Label(root,font=100,bg="lavender",fg="purple").grid(row=1,column=2)

def updmess(x):
    msg = Label(root,text=x, font=100, bg="lavender", fg="purple").grid(row=1, column=2)

#userscoreupdate
def upduserscore(usersc):
    score=str(usersc)
    playerscore = Label(root, text=score,font=("Helvetica 35 bold"), bg="lavender", fg='black').grid(row=1, column=3)

def updcompscore(compsc):
    score=str(compsc)
    compscore = Label(root, text=score,font=("Helvetica 35 bold"), bg="lavender", fg='black').grid(row=1, column=1)


compsc=0
usersc=0
def checkwin(player,computer):
    global compsc
    global usersc
    if player==computer:
        updmess("  ITS A TIE!   ")
    elif player=="rock":
        if computer=="paper":
            updmess(" YOU LOOSE ")
            compsc = compsc + 1
            updcompscore(compsc)

        else:
            updmess("  YOU WIN   ")
            usersc = usersc + 1
            upduserscore(usersc)

    elif player=="paper":
        if computer=="scissor":
            updmess(" YOU LOOSE ")
            compsc = compsc + 1
            updcompscore(compsc)

        else:
            updmess("  YOU WIN   ")
            usersc = usersc + 1
            upduserscore(usersc)

    elif player=="scissor":
        if computer=="rock":
            updmess(" YOU LOOSE ")
            compsc = compsc + 1
            updcompscore(compsc)

        else:
            updmess("  YOU WIN   ")
            usersc = usersc + 1
            upduserscore(usersc)

    else:
        pass



#choiceupdates
choice=["rock","paper","scissor"]
def updchoice(x,user):
    global compsc
    global usersc
    compchoice=choice[randint(0,2)]
    if compchoice=="rock":
        comp = Label(root, image=rockcomp, bg="lavender", width=500).grid(row=1, column=0)
    elif compchoice=="paper":
        comp = Label(root, image=papercomp, bg="lavender", width=500).grid(row=1, column=0)
    else:
        comp = Label(root, image=scicomp, bg="lavender", width=500).grid(row=1, column=0)

    if x=="rock":
        user = Label(root, image=rock, bg="lavender",width=500).grid(row=1, column=4)
    elif x=="paper":
        user = Label(root, image=paper, bg="lavender",width=500).grid(row=1, column=4)
    else:
        user = Label(root, image=sci, bg="lavender",width=500).grid(row=1, column=4)

    checkwin(x,compchoice)


rocky=Button(root,font=("Helvetica 15 bold"),text="ROCK",bg="red",fg="white",command=lambda :updchoice("rock",user)).place(x=550,y=350)
papy=Button(root,font=("Helvetica 15 bold"),text="PAPER",bg="yellow",fg="black",command=lambda :updchoice("paper",user)).place(x=650,y=350)
stony=Button(root,font=("Helvetica 15 bold"),text="SCISSOR",bg="green",fg="white",command=lambda :updchoice("scissor",user)).place(x=750,y=350)

root.mainloop()