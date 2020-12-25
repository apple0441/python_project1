import datetime as dt
import time as t
from tkinter import *
import tkinter.messagebox as tmg

# Function for calcualting the date:-

def calculate():
    status.set('Calculating...')
    s.update()
    t.sleep(0.6)
    status.set(' ')
    s.update()
    if function.get()=="Before":
        tmg.showinfo("Date",f'{ndays.get()} days before {day.get()}/{month.get()}/{year.get()} is {dt.date(year.get(),month.get(),day.get())-dt.timedelta(days=ndays.get())}')
    elif function.get()=="After":
        tmg.showinfo("Date",f'{ndays.get()} days after {day.get()}/{month.get()}/{year.get()} is {dt.date(year.get(),month.get(),day.get())+dt.timedelta(days=ndays.get())}')

# Base Design:-

root = Tk()
root.geometry('900x600')
root.title("Date Calculator")
f1 = Frame(root, borderwidth=10, bg='red', relief=SUNKEN)
Label(f1, text="Date Calculator", font='lucid 13 italic bold', padx=5).pack()
f1.pack()
f2 = Frame(root, borderwidth=10, relief=SUNKEN, bg='cyan')
f2.pack(pady=20)

# Labels for entries:-

Label(f2, text="Year(yyyy):-", font='lucid 10 bold', padx=14).grid(row=0, column=0, pady=3)
Label(f2, text="Month(mm):-", font="lucid 10 bold", padx=12).grid(row=1, column=0, pady=3)
Label(f2, text="Day(dd):-", font='lucid 10 bold', padx=23).grid(row=2, column=0, pady=3)
Label(f2, text="Number Of Days", font='lucid 10 bold').grid(row=3, column=0, pady=3)
Label(f2, text="Which function you want to use:-", font='lucid 10 bold', pady=2).grid(row=4,column=1, padx=3)

# Variables :-

year = IntVar()
year.set(2020)
month = IntVar()
day = IntVar()
ndays = IntVar()
function = StringVar()
function.set("Before")
status = StringVar()
status.set(' ')

# Entries:-

Entry(f2, textvariable=year, font='lucid 11 italic bold').grid(row=0, column=1, padx=3)
Entry(f2, textvariable=month, font='lucid 11 italic bold').grid(row=1, column=1, padx=3)
Entry(f2, textvariable=day, font='lucid 11 italic bold').grid(row=2, column=1, padx=3)
Entry(f2, textvariable=ndays, font='lucid 11 italic bold').grid(row=3, column=1, padx=3)

# Checkbuttons:-

radio = Radiobutton(f2, variable=function, text="Before", value="Before").grid(row=4, column=2, pady=12)
radio = Radiobutton(f2, variable=function, text="After", value="After").grid(row=4, column=3, pady=12)

# Creating Button:-

Button(root, text="Calculate", font='lucid 12 bold', bg='orange', command=calculate).pack(pady=20)

# Creating Status Bar:-

s = Label(root, textvariable=status, anchor='w', relief=SUNKEN, bg='grey', fg='white', font='lucid 10 bold')
s.pack(side='bottom', fill=X)

root.mainloop()
