from tkinter import *
import tkinter.messagebox as tmg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)
    # Delete from 1-> First Line , .0->Oth Character to END of file.


def openFile():
    global file
    file = askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- NotePad")
        TextArea.delete(1.0, END)
        f = open(file, 'r')
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                 filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == '':
            file = None
        else:
            # Save as new file:-
            f = open(file, 'w')
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "- NotePad")
    else:
        # Save the file:-
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    # Cut Function using event generator:-
    TextArea.event_generate(("<<Cut>>"))


def copy():
    # Copy Function using event generator:-
    TextArea.event_generate(("<<Copy>>"))


def paste():
    # Paste Function using event generator:-
    TextArea.event_generate(("<<Paste>>"))


def about():
    tmg.showinfo('NotePad', "Notepad by Aritra (Python Developer) ")


if __name__ == '__main__':
    # Basic Tkinter Setup:-
    root = Tk()
    root.geometry('900x600')
    root.title('Untitled Notepad')
    root.wm_iconbitmap('Notepad_22553.ico')

    # Add TextArea:-
    TextArea = Text(root, font='lucid 11 italic bold')
    TextArea.pack(fill=BOTH, expand=True)
    # File:-
    file = None

    # Menu_bar:-
    Menu_bar = Menu(root)

    # File Menu Starts:-
    FileMenu = Menu(Menu_bar, tearoff=0)

    # To open new File:-
    FileMenu.add_command(label='New', command=newFile)

    # To open an existing File:-
    FileMenu.add_command(label='Open', command=openFile)

    # To save the current File:-
    FileMenu.add_command(label='Save', command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=quitApp)
    Menu_bar.add_cascade(menu=FileMenu, label='File')
    # FileMenu Ends

    # EditMenu Starts:-
    EditMenu = Menu(Menu_bar, tearoff=0)
    # To give a feature of cut:-
    EditMenu.add_command(label='Cut', command=cut)
    # To give a feature of Copy:-
    EditMenu.add_command(label='Copy', command=copy)
    # To give a feature of Paste:-
    EditMenu.add_command(label='Paste', command=paste)
    Menu_bar.add_cascade(label='Edit', menu=EditMenu)
    # EditMenu Ends

    # Help Menu Starts:-
    HelpMenu = Menu(Menu_bar, tearoff=0)
    HelpMenu.add_command(label='About Notepad', command=about)
    Menu_bar.add_cascade(label='Help', menu=HelpMenu)
    # Help Menu Ends
    root.config(menu=Menu_bar)
    # Adding ScrollBar:-
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side='right', fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()
