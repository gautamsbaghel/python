import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = [
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "abandon",
    "balance",
    "baggage",
    "bank",
    "quarter",
    "quit",
    "aeroplane",
    "banana",    
]

words = [
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "nbonada",
    "lanceab",
    "agebagg",
    "knab",
    "uarertq",
    "tiuq",
    "roaneplae",
    "nanaba",
    
    
]

hints=[
    " programming language name starts with 'j' ",
    "happening quickly or promptly. ",
    " country in the northern part of North America ",
    " country in asia with 2nd largest population on earth",
    "country with president 'Donald trump",
    " the capital of England ",
    "cease to support",
    "an equally distribution of weight",
    "suitcases and bags",
    "association which allows you to keep money and withdraw anytime",
    "one fourth of a pound weight",
    "leave or exiting out of it ",
    "fastest transportation vehicle",
    "fruit of all season",
    
   
 ]   


num =  random.randrange(0, len(words), 1)

def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    hintlbl.config(text = "Your hint will appear here, click on hint button to get it")
    e1.delete(0, END)

def hint ():
    hintlbl.config(text = hints[num])

      
def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("CONGRATULATION" , "This is correct word , play more .")
        res()
    else:
        messagebox.showerror("OOPS ", "WRONG ANSWER , TRY AGAIN")
        e1.delete(0, END)

root = tkinter.Tk()
root.geometry("1200x1200+150+150")
root.title("Jumbbled words")
root.configure(background = "#ffb3ff")

lbl = Label( root, text = "Your here" , font  = ("Verdana", 40), bg = "#cc7a00",fg = "#FFFFFF",)
lbl.pack(pady = 30,ipady=10,ipadx=10)

hintlbl = Label( root, text = "Your hint will appear here, click on ""get a hint button ""to get it." , font  = ("Verdana", 25), bg = "#cc7a00",fg = "#FFFFFF",)
hintlbl.pack(pady = 30)

ans1 = StringVar()
e1 = Entry( root , font = ("Verdana",16) ,textvariable=ans1,)
e1.pack(ipady=5)

checkbutton = Button( root, text = "Check",  font = ("Comic sans ms", 16), width = 20 ,bg = "#000000", fg = "#ff4000", relief = SOLID, command = checkans)
checkbutton.pack(pady = 40)

resetbutton = Button( root, text = "Reset and get new word",font = ("Comic sans ms", 16),  width = 20,    bg = "#000000",fg = "#ff4000",relief = SOLID, command = res,)
resetbutton.pack()

hintbutton=Button(root,text ="Get a HiNt", font = ("Comic sans ms", 16),  width = 20,    bg = "#40ff00",fg = "#000000",relief = SOLID, command = hint,)
hintbutton.pack(pady=45)
default()
root.mainloop()
