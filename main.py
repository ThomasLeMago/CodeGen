from tkinter import Tk, Label, Entry, Button, font
from tkinter import filedialog as fd
from tkinter import messagebox as box
import json

BG = "#23272a"
FG = "white"
CONFIG = json.loads(open("./config.json", "r").read())

app = Tk()
app.geometry("500x500")
app.config(bg="#23272a")
app.title("Code Gen")

def listGen():
    f = open(fd.askopenfilename(), "r").read()
    f = f.split(CONFIG["listgensplit"])
    tmp = []

    for i in range(len(f)):
        tmp.append(f[i])
    
    app.clipboard_clear()
    app.clipboard_append(str(tmp))
    box.showinfo("Success", "List generated to clipboard")


def dicGen():
    f = open(fd.askopenfilename(), "r").read()
    f = f.split(CONFIG["listgensplit"])

    tmp = {}

    for i in range(len(f)):
        tmp[f[i].split(CONFIG["keysplit"])[0]] = f[i].split(CONFIG["keysplit"])[1]

    app.clipboard_clear()
    app.clipboard_append(str(tmp))
    box.showinfo("Success", "Dictionnary generated to clipboard")

def printGen():
    f = open(fd.askopenfilename(), "r").read()
    f = f.split(CONFIG["listgensplit"])
    tmp = ""

    for i in range(len(f)):
        tmp += CONFIG["printstatement"] + "(\"" + f[i] + "\")\n"
    
    app.clipboard_clear()
    app.clipboard_append(str(tmp))
    box.showinfo("Success", "Print generated to clipboard")

def htmlGen():
    f = open(fd.askopenfilename(), "r").read()
    f = f.split(CONFIG["listgensplit"])

    tmp = ""

    for i in range(len(f)):
        tmp += "<" + CONFIG["element"] + " class=\"" + f[i].split(CONFIG["keysplit"])[0] + "\">" + f[i].split(CONFIG["keysplit"])[1] + "</" + CONFIG["element"] +">\n"

    app.clipboard_clear()
    app.clipboard_append(str(tmp))
    box.showinfo("Success", "HTMl generated to clipboard")

consolas24 = font.Font(family="Consolas", size=24)
consolas16 = font.Font(family="Consolas", size=16)

title = Label(app, text="Code Gen", font=consolas24, bg=BG, fg=FG)
title.pack()

listGen = Button(app, text="List Gen", font=consolas16, bg=BG, fg=FG, command=listGen)
listGen.place(x = 10, y = 70)

dicGen = Button(app, text="Dictionnary Gen", font=consolas16, bg=BG, fg=FG, command=dicGen)
dicGen.place(x = 140, y = 70)

printGen = Button(app, text="Print Gen", font=consolas16, bg=BG, fg=FG, command=printGen)
printGen.place(x = 360, y = 70)

htmlGen = Button(app, text="HTML Gen", font=consolas16, bg=BG, fg=FG, command=htmlGen)
htmlGen.place(x = 10, y = 140)

app.mainloop()