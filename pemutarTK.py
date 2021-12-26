from tkinter import *
from tkinter import filedialog
from tkinter import font
from pygame import mixer
from direct.showbase.ShowBase import ShowBase

root = Tk()
root.title('pemutar musik')
root.config(background="yellow")

mixer.init()

Label(root, text="pemutar musik MP3", bg='white',
    font="Normal 40").grid(row=0, column=0, columnspan=3, pady=10)


#membuat cari
def cari():
    file = filedialog.askopenfilename(filetypes=[('mp3', '*.mp3')])
    if file == "":
        return
    mixer.music.load(file)
    t.config(state=NORMAL)
    t.delete(1.0, END)
    t.insert(END, file)
    t.config(state=DISABLED)

b = Button(root, text='cari', font='Normal 25',
        command=cari, relief=RIDGE, bd=10,
        activebackground='blue')
b.grid(row=1, column=1, ipadx=30, pady=5)


#membuat tempat cari
t = Text(root, font='Normal 15', bg='white',
        wrap=WORD, height=3, width=50)
t.grid(row=2, columnspan=3, pady=15)
t.config(state=DISABLED)


#membuat pause
def pause():
    mixer.music.pause()
b1 = Button(root, text='pause', font="Normal 25",
            command=pause, relief=RIDGE, bd=10,
            activebackground='blue')
b1.grid(row=3, column=0, padx=15, ipadx=15)


#membuat mainkan
def play():
    mixer.music.play(-1)
b2 = Button(root, text='mainkan', font='Normal 25',
            command=play, relief=RIDGE, bd=10,
            activebackground='blue')
b2.grid(row=3, column=1, pady=10)


#membuat unpause
def unpause():
    mixer.music.unpause()
b3 = Button(root, text='unpause', font='Normal 25',
            command=unpause, relief=RIDGE, bd=10,
            activebackground='blue')
b3.grid(row=3, column=2, pady=10)


#membuat berhenti
def stop():
    mixer.music.stop()
b4 = Button(root, text='berhenti', font='Normal 25',
            command=stop, relief=RIDGE, bd=10,
            activebackground='blue')
b4.grid(row=4, column=1, padx=10, pady=20)


root.mainloop()
