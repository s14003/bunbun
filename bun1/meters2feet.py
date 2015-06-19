from tkinter import *
from tkinter import ttk

def calculate(*args):

    try:
        value = float(meters.get())
        feet.set((value * 3.2808))
    except ValueError:
        pass


root = Tk()
root.title("Meters to Feet(・∀・)")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

meters_entry = ttk.Entry(mainframe,width=7, textvariable = meters)

meters_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="meters").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=feet).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="feet").grid(column=3, row=2, sticky=S)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
    pass

meters_entry.focus()
root.bind('<Return>', calculate)


root.mainloop()

