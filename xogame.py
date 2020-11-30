from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("x o game")
root.config(bg = "Cadet Blue")

Tops = Frame(root, bg='Cadet Blue',pady=2,width=1350,height=100,relief=RIDGE)
Tops.grid(row=0,column=0)

#title on main frame
labtitle = Label(Tops,font=('arial',50,'bold'), text="Advanced x/o game",bd=21,bg='Cadet Blue',fg='cornsilk',justify=CENTER)
labtitle.grid(row=0,column=0)

#whole frame
MainFrame = Frame(root, bg= 'Powder Blue',pady=2,width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

#divide frame into 2 right and left
LeftFrame = Frame(MainFrame, bd=10,width=750,height=500,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
LeftFrame.pack(side=LEFT)


RightFrame = Frame(MainFrame, bd=10,width=560,height=500,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
RightFrame.pack(side=RIGHT)

#dividing right frame in 2 parts
RightFrame1 = Frame(RightFrame, bd=10,width=560,height=200,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
RightFrame1.grid(row=0,column=0)


RightFrame2 = Frame(RightFrame, bd=10,width=560,height=200,pady=2,padx=10,bg="Cadet Blue",relief=RIDGE)
RightFrame2.grid(row=1,column=0)

#inserting players with initial
playerX=IntVar()
playerO=IntVar()

playerX.set(0)
playerO.set(0)

 
buttons = StringVar()
click = True

#function to check values
def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()
         
#function for score
def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.config(bg='light green')
        button2.config(bg='light green')
        button3.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.config(bg='light green')
        button5.config(bg='light green')
        button6.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.config(bg='light green')
        button8.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.config(bg='light green')
        button5.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.config(bg='light green')
        button5.config(bg='light green')
        button7.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.config(bg='light green')
        button4.config(bg='light green')
        button7.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")
   
    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.config(bg='light green')
        button5.config(bg='light green')
        button8.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.config(bg='light green')
        button6.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerX.get())
        score = (n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")
#cases for O
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.config(bg='light green')
        button2.config(bg='light green')
        button3.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.config(bg='light green')
        button5.config(bg='light green')
        button6.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.config(bg='light green')
        button8.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.config(bg='light green')
        button5.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.config(bg='light green')
        button5.config(bg='light green')
        button7.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.config(bg='light green')
        button4.config(bg='light green')
        button7.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.config(bg='light green')
        button5.config(bg='light green')
        button8.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")

    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.config(bg='light green')
        button6.config(bg='light green')
        button9.config(bg='light green')
        n = float(playerO.get())
        score = (n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner X"," you won!!")


#function for reset button
def reset(): 
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.config(bg="white")
    button2.config(bg="white")
    button3.config(bg="white")
    button4.config(bg="white")
    button5.config(bg="white")
    button6.config(bg="white")
    button7.config(bg="white")
    button8.config(bg="white")
    button9.config(bg="white")

#function for newgame buton
def NewGame():
    reset()
    playerX.set(0)
    playerO.set(0)

labplayerX= Label(RightFrame1, font=('arial',40,'bold'), text='player X :',padx=2,pady=2,bg="Cadet Blue")
labplayerX.grid(row=0,column=0,sticky=W)

labplayerO= Label(RightFrame1, font=('arial',40,'bold'), text='player O :',padx=2,pady=2,bg="Cadet Blue")
labplayerO.grid(row=1,column=0,sticky=W)

#textbox to add players score in rightframe 1
txtplayerX =  Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg="black",textvariable =playerX,width=12,justify=LEFT)
txtplayerX.grid(row=0,column=1)

txtplayerO =  Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg="black",textvariable =playerO,width=12,justify=LEFT)
txtplayerO.grid(row=1,column=1)

#to add new button for reset and new game
buttonreset = Button(RightFrame2, text="RESET", font=('Times 26 bold'),height = 1,width = 28,bg='white',command=reset)
buttonreset.grid(row=2,column=0,padx=6,pady=11)

buttonnewgame = Button(RightFrame2, text="NEW GAME", font=('Times 26 bold'),height = 1,width = 28,bg='white',command=NewGame)
buttonnewgame.grid(row=3,column=0,padx=6,pady=10)

#to create 3x3 board
button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'),height = 3,width = 8, bg='white',command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)


root.mainloop()
