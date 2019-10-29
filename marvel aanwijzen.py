from tkinter import *

x=0
z=0
punten=25

def hint():
    global x
    hint.counter+=1
    L['text'] = 'Button clicked: ' + str(hint.counter)
    x=hint.counter
    x=x*-3
    return x

def raden():
    global z
    raden.counter +=1
    R['text'] = 'Button clicked: ' + str(raden.counter)
    z=raden.counter
    return z

def close_window ():
    window.destroy()
    print(punten+x-z)


window = Tk()
hint.counter = 0
raden.counter=0

hulp= Button(window, text="Hint", command = hint)
hulp.pack(padx=20,pady=20)

gok = Button (window, text = "Raden", command = raden)
gok.pack(padx=20,pady=20)

L = Label(window, text="No clicks yet.")
L.pack(padx=20,pady=20)

R = Label(window, text="No clicks yet.")
R.pack(padx=20,pady=20)

frame = Frame(window)
frame.pack()
afsluiten = Button (frame, text = "Good-bye.", command = close_window)
afsluiten.pack(padx=20,pady=20)

window.mainloop()
