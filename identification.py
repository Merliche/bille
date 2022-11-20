from tkinter import *
import sqlite3
   

def callbackFunc():
    identifiants = resultString.set("{} - {}".format(CBString.get(),
                                      PinInt.get()))
    return identifiants
     
OptionList = [
"5136405006383498",
"3285548746932323",
"5764831715489314",
"5434 8952 2314 7594",
"5129 0309 5703 7668",
"5395 3319 9090 6720"
] 

#Il  faut que les Numeros CB soit sous forme DE menue deroulant
app = Tk() 
app.geometry('400x300')

labelCB = Label(app,
                    text = "CB")

labelCB.grid(column=0, row=0, sticky=W)
labelPin = Label(app,
                    text = "Code Pin")
labelPin.grid(column=0, row=1, sticky=W)

CBString = StringVar()
PinInt = IntVar()
entryCB = OptionMenu(app,CBString, *OptionList)
entryPin = Entry(app, width=20, show="*",textvariable=PinInt)

entryCB.grid(column=1, row=0, padx=10)
entryPin.grid(column=1, row=1, padx=10)


resultButton = Button(app, text = 'Connexion',
                         command=callbackFunc)

resultButton.grid(column=0, row=2, pady=10, sticky=W)

resultString= StringVar()
resultLabel = Label(app, textvariable=resultString)
resultLabel.grid(column=1, row=2, padx=10, sticky=W)

app.mainloop()