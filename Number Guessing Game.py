from tkinter import *
from random import *
import time

window = Tk()
window.title("Main Menu")
window.geometry()
window.config(background="#72A0C1")
bottom = 0
over = 50
number = randint(bottom,over)
guess = 0
attempts = 10

bt = 0
t2=100
num= randint(bt,t2)
guess_1 = 0
tries= 10

under=0
above=1000
numy= randint(under,above)
guess_2 = 0
trials= 10

def Setup1to50():
    global number, attempts, prompt,bottom,over,E1,guess,E2,E3,T
    top= Toplevel()
    top.title("Easy")
    top.geometry("250x300")
    top.config(background="#8B008B")

    T = Text(top,width=30,height=1)
    T.grid(row=2,column=0,columnspan=2, pady=5, padx=2)
    
    L2 = Label(top,text="Please enter your guesss below",fg="Black",font="Courier 10 bold",bg="#E52B50")
    L2.grid(row=3, column=0,columnspan=2, pady=5)

    A = Button(top,text ="Submit",fg="blue",font="Times 10 bold",bg="Violet",command=click)
    A.place(x=93,y=94)

    B = Button(top,text="Restart",fg="Black",font="Calibri 10 bold",bg="cyan", command=Clear)
    B.place(x=107,y=190)
    
    E1 = Entry(top,bd = 1,justify=LEFT,width=25)
    E1.grid(row=4,column=0,columnspan=2, pady=5)

    E2 = Text(top,width=28,height=3)
    E2.place(x=10,y=125)

    E3 = Text(top,width= 5,bd=1,height= 1)
    E3.place(x=175,y=192)

    L3 = Label(top,text= "Attempts",font="Courier 10 bold")
    L3.place(x=25,y=190)

    prompt = "Enter a number between 0-50."
    T.delete(0.0,END)
    T.insert(0.0,prompt)
    E3.delete(0.0,END)
    E3.insert(0.0,attempts)

def restart():
    global bottom,over,number,guess,attempts,top
    bottom = 0
    over = 50
    number = randint(bottom,over)
    guess = 0
    attempts = 10
    prompt="Enter a number between 0-50."
    T.delete(0.0,END)
    T.insert(0.0,prompt)
    E3.delete(0.0,END)
    E3.insert(0.0,attempts)
    window.update()
    

def click():
    global attempts,E2,number,over,bottom,guess,E3
    guess = int(E1.get())
    E1.delete(0,END)
    attempts-=1
    if guess == number:
        time.sleep(1)
        message= "You Win!!"
    elif guess > over or guess < bottom:
        time.sleep(1)
        message ="This is not between the range above:(\n"
        time.sleep(1)
    elif guess > number:
        message="This is too high!!"
        time.sleep(1)
    elif guess < number:
        message="This is too low!!"

    if attempts <=0:
        message="Game Over\nThe number was...{0}".format(number)

    E3.delete(0.0,END)
    E3.insert(0.0,attempts)
    E2.delete(0.0,END)
    E2.insert(0.0,message)

def Clear():
    global E3,E2
    E3.delete(0.0,END)
    E2.delete(0.0,END)
    restart()
    
    
def Setup_1to100():
    global bt,t2,num,e1,guess_1,e2,e3,t,prompt_1,tries
    top_1= Toplevel()
    top_1.title("Medium")
    top_1.geometry("250x300")
    top_1.config(background="#8B008B")

    t = Text(top_1,width=30,height=1)
    t.grid(row=2,column=0,columnspan=2, pady=5, padx=2)
    
    l2 = Label(top_1,text="Please enter your guesss below",fg="Black",font="Courier 10 bold",bg="#E52B50")
    l2.grid(row=3, column=0,columnspan=2, pady=5)

    a = Button(top_1,text ="Submit",fg="blue",font="Times 10 bold",bg="Violet",command=touch)
    a.place(x=93,y=94)

    b = Button(top_1,text="Restart",fg="Black",font="Calibri 10 bold",bg="cyan", command=Clear_1)
    b.place(x=107,y=190)
    
    e1 = Entry(top_1,bd = 1,justify=LEFT,width=25)
    e1.grid(row=4,column=0,columnspan=2, pady=5)

    e2 = Text(top_1,width=25,height=3)
    e2.place(x=25,y=125)

    e3 = Text(top_1,width= 5,bd=1,height= 1)
    e3.place(x=175,y=192)

    l3 = Label(top_1,text= "Attempts",font="Courier 10 bold")
    l3.place(x=25,y=190)

    prompt_1 = "Enter a number between 0-100."
    t.delete(0.0,END)
    t.insert(0.0,prompt_1)
    e3.delete(0.0,END)
    e3.insert(0.0,tries)

def replay():
    global bt,t2,num,guess_1,tries,top_1
    bt = 0
    t2=100
    num= randint(bt,t2)
    guess_1 = 0
    tries= 10
    prompt_1="Enter a number between 0-100."
    t.delete(0.0,END)
    t.insert(0.0,prompt_1)
    e3.delete(0.0,END)
    e3.insert(0.0,tries)
    window.update()
    

def touch():
    global tries,e2,num,t2,bt,guess_1,e3
    guess_1 = int(e1.get())
    e1.delete(0,END)
    tries-=1
    if guess_1 == num:
        time.sleep(1)
        message= "You Win!!"
    elif guess > t2 or guess < bt:
        time.sleep(1)
        message ="This is not between the range above:(\n"
        time.sleep(1)
    elif guess_1 > num:
        message="This is too high!!"
        time.sleep(1)
    elif guess_1 < num:
        message="This is too low!!"

    if tries <=0:
        message="Game Over\nThe number was...{0}".format(num)

    e3.delete(0.0,END)
    e3.insert(0.0,tries)
    e2.delete(0.0,END)
    e2.insert(0.0,message)

def Clear_1():
    global e3,e2
    e3.delete(0.0,END)
    e2.delete(0.0,END)
    replay()
    
def Setup_1to1000():
    global under,above,numy,guess_2,g2,z,prompt_2,trial,f1,k3
    top_2= Toplevel()
    top_2.title("Hard")
    top_2.geometry("250x300")
    top_2.config(background="#8B008B")

    z = Text(top_2,width=30,height=1)
    z.grid(row=2,column=0,columnspan=2, pady=5, padx=2)
    
    b2 = Label(top_2,text="Please enter your guesss below",fg="Black",font="Courier 10 bold",bg="#E52B50")
    b2.grid(row=3, column=0,columnspan=2, pady=5)

    c = Button(top_2,text ="Submit",fg="blue",font="Times 10 bold",bg="Violet",command=show)
    c.place(x=93,y=94)

    d = Button(top_2,text="Restart",fg="Black",font="Calibri 10 bold",bg="cyan", command=Erase)
    d.place(x=107,y=190)
    
    f1 = Entry(top_2,bd = 1,justify=LEFT,width=25)
    f1.grid(row=4,column=0,columnspan=2, pady=5)

    g2 = Text(top_2,width=25,height=3)
    g2.place(x=25,y=125)

    k3 = Text(top_2,width= 5,bd=1,height= 1)
    k3.place(x=175,y=192)

    x3 = Label(top_2,text= "Attempts",font="Courier 10 bold")
    x3.place(x=25,y=190)

    prompt_2 = "Enter a number between 0-1000."
    z.delete(0.0,END)
    z.insert(0.0,prompt_2)
    k3.delete(0.0,END)
    k3.insert(0.0,tries)

def loop():
    global under,above,numy,guess_2,trials,top_2
    under=0
    above=1000
    numy= randint(under,above)
    guess_2 = 0
    trials= 10
    prompt_2="Enter a number between 1-1000."
    z.delete(0.0,END)
    z.insert(0.0,prompt_2)
    k3.delete(0.0,END)
    k3.insert(0.0,tries)
    window.update()

def show():
    global trials,g2,numy,above,under,guess_2,k3
    guess_2 = int(f1.get())
    f1.delete(0,END)
    trials-=1
    if guess_2 == numy:
        time.sleep(1)
        message= "You Win!!"
    elif guess_2 > above or guess_2 < under:
        time.sleep(1)
        message ="This is not between the range above:(\n"
        time.sleep(1)
    elif guess_2 > numy:
        message="This is too high!!"
        time.sleep(1)
    elif guess_2 < numy:
        message="This is too low!!"

    if trials <=0:
        message="Game Over\nThe number was...{0}".format(numy)

    k3.delete(0.0,END)
    k3.insert(0.0,trials)
    g2.delete(0.0,END)
    g2.insert(0.0,message)


def Erase():
    global k3,g2
    k3.delete(0.0,END)
    g2.delete(0.0,END)
    loop()   




L = Label(window, text="Welcome to the guessing game",fg="Black",bg="#CD9575",font="Courier 14 bold")
L.grid(row=0,column=0,columnspan=2, pady=2)

p1 = Label(window,text="Select the difficulty",fg="Black",bg="#9966CC",font="Courier 10 bold")
p1.grid(row=1,rowspan=1,column=0,columnspan=2, pady=2)

p2 = Button(window,text="Easy",fg="#8B008B",bg="#00BFFF",font="Courier 10 bold",command=Setup1to50)
p2.grid(row=2,rowspan=5,column=0,columnspan=2, pady=2)

p3 = Button(window,text="Medium",fg="#8B008B",bg="#00BFFF",font="Courier 10 bold",command=Setup_1to100)
p3.grid(row=7,rowspan=14,column=0,columnspan=2, pady=0)

p4 = Button(window,text="Hard",fg="#8B008B",bg="#00BFFF",font="Courier 10 bold",command=Setup_1to1000)
p4.grid(row=18,rowspan=20,column=0,columnspan=2, pady=29)
