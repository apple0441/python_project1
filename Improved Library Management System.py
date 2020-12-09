import mysql.connector
from tkinter import *
import tkinter.messagebox as tmg

my_db = mysql.connector.connect(host='localhost', user='tesla', passwd='1234', database='library')
my_cursor = my_db.cursor()


def packer(a, b, c):
    a.pack(side='top')
    b.pack(pady=50)
    c.pack()


def forget(*values):
    for i in values:
        i.pack_forget()


def borrow():
    def back():
        forget(f4, f5, b5, b2)
        packer(f1, f2, f3)

    def search_it():
        def submit():
            sql = 'insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            val = (
                f_name.get(), l_name.get(), addr.get(), dob.get(), mobile.get(), gender.get(), email.get(), se,
                date.get())
            my_cursor.execute(sql, val)
            my_db.commit()
            change = Q - 1
            my_cursor.execute('update book set number=%s where name="%s"' % (change, se))
            my_db.commit()
            tmg.showinfo('Validator', 'Database Updated Successfully.You can take the book right now.')
            forget(b3, f6, f7, b5)
            packer(f1, f2, f3)

        se = book.get()
        fe = ('select count(name) from book where name="%s"' % (se))
        te = ('select number from book where name="%s"' % (se))
        my_cursor.execute(fe)
        result1 = my_cursor.fetchall()
        my_cursor.execute(te)
        result2 = my_cursor.fetchall()
        f6 = Frame(root, borderwidth=12, bg='yellow', relief=SUNKEN)
        f6.pack()
        f7 = Frame(root, borderwidth=12, relief=SUNKEN)
        f7.pack(pady=10)
        for i in result1:
            for j in i:
                if j == 1:
                    for k in result2:
                        global Q
                        for Q in k:
                            m = tmg.askquestion("Search Result",
                                                f'{Q} {se} books are available.Do you want to continue?')
                            if m == "yes":
                                forget(f4, f5, b2, b5)
                                Label(f6, text='Enter your Details', font='ALGERIAN 19 bold').pack()
                                entries = ['First Name:-', 'Last Name:-', 'Address:-', 'DOB:-', 'Mobile:-', 'Gender',
                                           'Email:-', 'Date:-']
                                f_name = StringVar()
                                l_name = StringVar()
                                addr = StringVar()
                                dob = StringVar()
                                mobile = IntVar()
                                gender = StringVar()
                                email = StringVar()
                                date = StringVar()
                                enter = [f_name, l_name, addr, dob, mobile, gender, email, date]
                                for u in range(len(entries)):
                                    Label(f7, text=entries[u], font='lucida 10 bold').grid(row=u, column=0)
                                    Entry(f7, textvariable=enter[u], font='lucida 10 bold').grid(row=u, column=1,
                                                                                                 padx=5)
                                b3 = Button(root, text='Submit', bg='orange', command=submit)
                                b3.pack()
                            else:
                                tmg.showinfo("Ok", "Ok.Thanks")
                                forget(f4, f5, b2, b5)
                                packer(f1, f2, f3)
                elif j == 0:
                    tmg.showinfo("Search Result", f'Sorry {se} is not available at the present time.')

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth=12, bg='red', relief=SUNKEN)
    f4.pack(side='top')
    f5 = Frame(root, borderwidth=12, bg='yellow', relief=RIDGE)
    f5.pack(pady=20)
    Label(f4, text='Borrow A Book', font='ALGERIAN 19 bold').pack()
    Label(f5, text='Search Your Book:-', font='lucida 10 bold').grid(row=0, column=0)
    book = StringVar()
    Entry(f5, font='lucida 10 bold', textvariable=book).grid(row=0, column=1, padx=10)
    b2 = Button(root, text='Search', font='7', bg='purple', command=search_it)
    b2.pack()
    b5 = Button(root, text='Go Back', font='10', command=back, bg='yellow')
    b5.pack(pady=5)


def donate():
    def back():
        forget(f4, f5, b6, b5)
        packer(f1, f2, f3)

    def donate_it():
        global change2
        my_cursor.execute('select count(name) from book where name="%s"' % (book.get()))
        for w in my_cursor:
            for v in w:
                if v == 1:
                    my_cursor.execute('select number from book where name="%s"' % (book.get()))
                    for u in my_cursor:
                        for v in u:
                            change2 = v + number.get()
                    my_cursor.execute(
                        'update book set number=%s,date="%s" where name="%s"' % (change2, date.get(), (book.get())))
                    my_db.commit()
                    tmg.showinfo('Validator', 'Database Updated Successfully.Thanks for your donation :)')
                    forget(f4, f5, b6, b5)
                    packer(f1, f2, f3)
                elif v == 0:
                    my_cursor.execute('insert into book values(%s,%s,%s)', (book.get(), number.get(), date.get()))
                    my_db.commit()
                    tmg.showinfo('Validator', 'Database Updated Successfully.Thanks for your donation :)')
                    forget(f4, f5, b6, b5)
                    packer(f1, f2, f3)

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth=12, bg='red', relief=SUNKEN)
    f4.pack(side='top')
    f5 = Frame(root, borderwidth=12, relief=SUNKEN)
    f5.pack(pady=15)
    book = StringVar()
    number = IntVar()
    number.set(1)
    date = StringVar()
    entries = ['Book:-', 'Number:-', 'Date:-']
    enter = [book, number, date]
    for v in range(len(entries)):
        Label(f5, text=entries[v], font='lucida 10 bold').grid(row=v, column=0, padx=5)
        Entry(f5, textvariable=enter[v], font='lucida 10 bold').grid(row=v, column=1, padx=5)
    Label(f4, text='Donate a Book', font='ALGERIAN 19 bold').pack()
    b6 = Button(root, text='Submit', bg='yellow', command=donate_it, padx=9, font='10')
    b6.pack()
    b5 = Button(root, text='Go Back', font='10', command=back, bg='yellow')
    b5.pack(pady=5)


def Return():
    def back():
        forget(f4, f5, b7, b5)
        packer(f1, f2, f3)

    def return_it():
        my_cursor.execute('select count(email) from users where email="%s"' % (email.get()))
        for t in my_cursor:
            for j in t:
                if j == 1:
                    o = []
                    my_cursor.execute('select book,date from users where email="%s"' % (email.get()))
                    for h in my_cursor:
                        for v in h:
                            o.append(v)
                    t = tmg.askquestion('Confirmation', f'You have borrowed {o[0]} on {o[1]}.Do you want to continue?')
                    if t == 'yes':
                        my_cursor.execute('delete from users where email="%s"' % (email.get()))
                        my_db.commit()
                        my_cursor.execute('select number from book where name="%s"' % (o[0]))
                        change = 0
                        for i in my_cursor:
                            for k in i:
                                change = k + 1
                        my_cursor.execute('update book set number=%s where name="%s"' % (change, o[0]))
                        my_db.commit()
                        tmg.showinfo('Confirmation', 'Database Updated Successfully.')
                        forget(f4, f5, b5, b7)
                        packer(f1, f2, f3)
                    else:
                        tmg.showinfo('Ok', 'Ok')
                        forget(f4, f5, b5, b7)
                        packer(f1, f2, f3)
                else:
                    tmg.showinfo('Wrong Input',
                                 'No such email exists in our database . Please enter the email correctly.')

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth=7, bg='orange', relief=SUNKEN)
    f4.pack(side='top')
    Label(f4, text='Return your book', font='ALGERIAN 19 bold').pack()
    f5 = Frame(root, borderwidth=7, bg='purple', relief=SUNKEN)
    f5.pack(pady=10)
    Label(f5, text='Enter Your Email(That you entered during registration):-', font='lucida 10 bold').grid(row=0,
                                                                                                           column=0)
    email = StringVar()
    Entry(f5, textvariable=email, font='lucida 11 bold').grid(row=0, column=1, padx=5)
    b7 = Button(root, text='Submit', bg='yellow', font='lucida', command=return_it)
    b7.pack(pady=10)
    b5 = Button(root, text='Go Back', font='10', command=back, bg='yellow')
    b5.pack(pady=5)


root = Tk()
root.geometry('1998x1026')
f1 = Frame(root, borderwidth=12, bg='red', relief=SUNKEN)
f1.pack(side='top')
Label(f1, text="Welcome To Central Library", font='ALGERIAN 19 bold', bg='orange').grid()
photo = PhotoImage(file="Library.png")
f2 = Frame(root, borderwidth=12, bg='purple', relief=RIDGE)
f2.pack(pady=50)
f3 = Frame(root, borderwidth=12, relief=SUNKEN, bg='green')
f3.pack()
Button(f3, text='Borrow a Book', font='lucida 10 bold', bg='yellow', command=borrow).grid(row=0, column=1, padx=10,
                                                                                          pady=10)
Button(f3, text='Donate a Book', font='lucida 10 bold', bg='yellow', command=donate).grid(row=0, column=2, padx=10,
                                                                                          pady=10)
Button(f3, text='Return a Book', font='lucida 10 bold', bg='yellow', command=Return).grid(row=0, column=3, padx=10,
                                                                                          pady=10)
Label(f2, image=photo).grid()
root.mainloop()
