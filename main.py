import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

window = tkinter.Tk()
window.geometry("500x500")

window.title("Find and Replace Window")
#canvas = Canvas(width=1200,height=1200)
#canvas.grid()
#image = PhotoImage(file ="C:/Users/PC HP/Downloads/dragon.png")
#canvas.create_image(20,20,image=image,anchor=NW)
#label = tkinter.label(window,image = image)
l1 = tkinter.Label(window,text='Upload File & read',width=30).grid(row=1,column=1)
b1 = tkinter.Button(window, text='Choisir un document', width=20,command = lambda:upload_file()).grid(row=2,column=2)
#b1.place(relx=1,rely=1,anchor=CENTER)
def upload_file():
    file = filedialog.askopenfilename()
    #fob=open(file,'r')
    #print(fob.read())
    print(file.read())

#1
lab1 = tkinter.Label(window, text = 'Copier votre texte ici :',foreground = "blue",font=("verdana",15)).grid(row = 0, column = 0 )
ent1 = tkinter.StringVar(value = "")
entr1 = tkinter.Entry(window, width = 100,textvariable = ent1).grid(row = 0, column = 1)
#2
lab2 = tkinter.Label(window, text = 'Cherche moi ca ? ',foreground = "blue",font=("verdana",15)).grid(row = 1, column = 0)
ent2 = tkinter.StringVar(value = "")
entr2 = tkinter.Entry(window, width = 100,textvariable = ent2).grid(row = 1, column = 1)
#3
lab3 = tkinter.Label(window, text = 'Remplace par ? *',foreground = "blue",font=("verdana",15)).grid(row = 2, column = 0)
ent3 = tkinter.StringVar(value = "")
entr3 = tkinter.Entry(window, width = 100 ,textvariable = ent3).grid(row = 2, column = 1)
lab5 = tkinter.Label(window,text = "Resultats du texte  : ",foreground = "blue",font=("verdana",15)).grid(row = 3, column = 0)
#4


def action():
    a = ent1.get()
    b = ent2.get()
    c = ent3.get()
    rep = a.replace(b,c)
    lab4 = tkinter.Label(window,width = 50,text = rep,foreground = "blue").grid(row = 3, column = 1)
#------------------------------------------------
btn = tkinter.Button(window,text = "Afficher le Texte",foreground = "purple",command = action,bg="#1b1b1b",font=("verdana",15)).grid(row = 4, column = 1)
button1 = Button( window, text = "Exit")
window.mainloop();