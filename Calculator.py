from tkinter import *


def click(event):
    text = event.widget.cget('text')
    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            try:
                value = eval(sc_value.get())
            except Exception:
                value = 'Error...'
        sc_value.set(value)
        screen.update()
    elif text == "C":
        sc_value.set(' ')
        screen.update()
    else:
        sc_value.set(sc_value.get() + text)
        screen.update()


root = Tk()
root.geometry('645x800')
root.title('Calculator')
sc_value = StringVar()
sc_value.set(' ')
screen = Entry(root, textvar=sc_value, font='lucid 35 bold')
screen.pack(fill=X, pady=10, padx=5, ipadx=5)
f1 = Frame(root, bg='grey')
f1.pack(padx=10)
b1 = ['9', '8', '7']
for i in b1:
    b = Button(f1, text=i, font='lucid 40 bold', padx=28, pady=12)
    b.pack(side='left', padx=12, pady=5)
    b.bind('<Button-1>', click)
f2 = Frame(root, bg='grey')
f2.pack()
b2 = ['6', '5', '4']
for i in b2:
    b = Button(f2, text=i, font='lucid 40 bold', padx=28, pady=12)
    b.pack(side='left', padx=12, pady=5)
    b.bind('<Button-1>', click)
f3 = Frame(root, bg='grey')
f3.pack(ipadx=9)
b3 = ['3', '2', '1']
for i in b3:
    b = Button(f3, text=i, font='lucid 40 bold', padx=25, pady=12)
    b.pack(side='left', padx=12, pady=5)
    b.bind('<Button-1>', click)
f4 = Frame(root, bg='grey')
f4.pack(ipadx=8)
b4 = ['0', '/', 'C']
for i in b4:
    b = Button(f4, text=i, font='lucid 40 bold', padx=26, pady=12)
    b.pack(side='left', padx=12, pady=5)
    b.bind('<Button-1>', click)
f5 = Frame(root, bg='grey')
f5.pack(ipadx=4)
b5 = ['-', '+', '=']
for i in b5:
    b = Button(f5, text=i, font='lucid 40 bold', padx=28, pady=12)
    b.pack(side='left', padx=12, pady=5)
    b.bind('<Button-1>', click)
root.mainloop()
