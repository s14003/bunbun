from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(frame, text="Full name:", foreground="#FF0000").grid(column=1, row=1)

def generate():
    import random
    hand.set(random.choice(('グー', 'チョキ', 'パー')))

ttk.Button(frame, text='ランダム！', command=generate).grid(column=1, row=2)
hand = StringVar()
hand.set('グー')
ttk.Label(frame, textvariable= hand).grid(column=2,row=2)


root.mainloop()
