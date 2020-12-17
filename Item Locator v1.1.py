import tkinter.messagebox as tmg
from tkinter import *
import time

import mysql.connector


def string_formatter(string):
    a = string.replace(" ", "")
    return a.lower()


def forget(*values):
    for i in values:
        i.pack_forget()


def packer(a, b, c):
    a.pack()
    b.pack(pady=70)
    c.pack(pady=100)


def enter():
    def back_it():
        forget(f4, f5, b1, b2)
        packer(f1, f2, f3)

    def enter_it():
        status.set('Entering the Items in The Database...')
        s.update()
        time.sleep(0.6)
        correct = []
        error = []
        for i in items.get().split(','):
            my_cursor.execute(
                'select count(search_name) from item_location where search_name="%s"' % string_formatter(i))
            for u in my_cursor:
                for t in u:
                    if t == 1:
                        error.append(i)
                    else:
                        fe = 'insert into item_location values(%s,%s,%s,%s)'
                        se = i, string_formatter(i), location.get(), string_formatter(location.get())
                        my_cursor.execute(fe, se)
                        my_db.commit()
                        correct.append(i)
        status.set(' ')
        if len(error) != 0 and len(correct) != 0:
            tmg.showerror('Validation',
                          f' We have successfully entered {correct} but we were not able to enter {error} as they already exist in our database.')
        elif len(correct) != 0 and len(error) == 0:
            tmg.showinfo('Validation', 'We have successfully updated our database.')
        elif len(correct) == 0:
            tmg.showerror('Validation', f'We were not able to enter {error} as they already exist in our database.')

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth='10', relief=SUNKEN, bg='cyan')
    f4.pack()
    Label(f4, text="Enter the items' Locations", font='ALGERIAN 19 bold').pack()
    f5 = Frame(root, borderwidth=7, relief=SUNKEN)
    f5.pack(pady=20)
    Label(f5, text='Enter the Location:-', padx=76, font='lucid 12 bold').grid(row=0, column=0, pady=3)
    Label(f5, text='Enter the items you want to put in this location:-', font='lucid 12 bold').grid(row=1, column=0)
    location = StringVar()
    items = StringVar()
    Entry(f5, font='lucid 12 bold', textvariable=location).grid(row=0, column=1, pady=3)
    Entry(f5, font='lucid 12 bold', textvariable=items).grid(row=1, column=1, pady=3)
    b1 = Button(root, text='Submit', command=enter_it, font='lucid 12 bold', bg='yellow')
    b1.pack()
    b2 = Button(root, text='Back', command=back_it, font='lucid 12 bold', bg='yellow', padx=8)
    b2.pack(pady=6)


def search():
    def back_it():
        forget(f4, f5, b2, b3, b6, f6)
        packer(f1, f2, f3)

    def search_it():
        def searching():
            status.set('Searching...')
            s.update()
            time.sleep(0.6)
            my_cursor.execute('select actual_location from item_location where actual_name="%s"'%(clicked.get()))
            for h in my_cursor:
                for g in h:
                    status.set(' ')
                    s.update()
                    tmg.showinfo('Location', f"{clicked.get()} is in {g}")
        status.set('Searching...')
        s.update()
        time.sleep(0.6)
        my_cursor.execute('select actual_name from item_location where search_name like "%{}%"'.format(string_formatter(item.get())))
        item_list = []
        for i in my_cursor:
            for j in i:
                item_list.append(j)
        if len(item_list)!=0:
            forget(f5, b2, b3)
            clicked = StringVar()
            global f6
            f6 = Frame(root, borderwidth=12, relief=SUNKEN, bg='cyan')
            f6.pack(pady=30)
            l1 = Label(f6, text='Select your item:-', font='lucid 12 italic bold')
            l1.grid(row=0, column=2, ipadx=15, padx=10)
            o = OptionMenu(f6, clicked, *item_list)
            o.grid(row=0,column=4)
            o.config(bg='red')
            global b6
            b6 = Button(text='Search', bg='orange', command=searching, font='lucid 12 bold')
            b6.pack()
            b3.pack(pady=12)
            status.set(' ')
            s.update()
        else:
            status.set(' ')
            s.update()
            tmg.showerror('Error','No such item exists in our database.')
    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth='10', relief=SUNKEN, bg='cyan')
    f4.pack()
    Label(f4, text="Search Your Items", font='ALGERIAN 19 bold').pack()
    f5 = Frame(root, borderwidth=7, relief=SUNKEN)
    f5.pack(pady=20)
    Label(f5, text='Enter the Item :-', padx=76, font='lucid 12 bold').grid(row=0, column=0, pady=3)
    item = StringVar()
    Entry(f5, textvariable=item, font='lucid 12 bold').grid(row=0, column=1)
    b2 = Button(root, text='Search', command=search_it, font='lucid 12 bold', bg='yellow')
    b2.pack()
    b3 = Button(root, text='Back', command=back_it, font='lucid 12 bold', bg='yellow', padx=8)
    b3.pack(pady=20)


def update():
    def back():
        forget(f4, f5, b3, b4)
        packer(f1, f2, f3)

    def submit():
        status.set('Updating...')
        s.update()
        time.sleep(0.6)
        correct = []
        error = []
        for o in item.get().split(','):
            my_cursor.execute(
                'select count(search_name) from item_location where search_name="%s"' % string_formatter(o))
            for i in my_cursor:
                for j in i:
                    if j == 0:
                        error.append(o)
                    else:
                        my_cursor.execute(
                            'update item_location set search_location="%s",actual_location="%s" where search_name="%s"' % (
                                string_formatter(new_location.get()), new_location.get(), string_formatter(o)))
                        my_db.commit()
                        correct.append(o)
        status.set('')
        if len(error) != 0 and len(correct) != 0:
            tmg.showerror('Validation',
                          f" We have successfully updated {correct} but we were not able to update {error} as they don't exist in our database.")
        elif len(correct) != 0 and len(error) == 0:
            tmg.showinfo('Validation', 'We have successfully updated our database.')
        elif len(correct) == 0:
            tmg.showerror('Validation', f"We were not able to update {error} as they don't exist in our database.")

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth='7', relief=SUNKEN, bg='blue')
    f4.pack()
    Label(f4, text='UPDATE ITEMS LOCATION', font='ALGERIAN 19 bold').pack()
    f5 = Frame(root, borderwidth='7', relief=SUNKEN, bg='cyan')
    f5.pack(pady=10)
    Label(f5, text='Enter the item:-', font='lucid 12 bold', padx=33.4).grid(row=0, column=0, pady=4)
    Label(f5, text='Enter the new location:-', font='lucid 12 bold').grid(row=1, column=0)
    item = StringVar()
    new_location = StringVar()
    Entry(f5, textvariable=item, font='12').grid(row=0, column=1, padx=4)
    Entry(f5, textvariable=new_location, font='12').grid(row=1, column=1, padx=4)
    b3 = Button(root, bg='cyan', text='Submit', font='12', command=submit)
    b3.pack(pady=15)
    b4 = Button(root, bg='cyan', text='Back', font='12', command=back)
    b4.pack(pady=15)


def delete():
    def back():
        forget(f4, f5, b3, b4)
        packer(f1, f2, f3)

    def submit():
        status.set('Deleting...')
        s.update()
        time.sleep(0.6)
        correct = []
        error = []
        for o in item.get().split(','):
            my_cursor.execute(
                'select count(search_name) from item_location where search_name="%s"' % string_formatter(o))
            for i in my_cursor:
                for j in i:
                    if j == 0:
                        error.append(o)
                    else:
                        my_cursor.execute('delete from item_location where search_name="%s"' % string_formatter(o))
                        my_db.commit()
                        correct.append(o)
        status.set('')
        if len(error) != 0 and len(correct) != 0:
            tmg.showerror('Validation',
                          f" We have successfully deleted {correct} but we were not able to delete {error} as they don't exist in our database.")
        elif len(correct) != 0 and len(error) == 0:
            tmg.showinfo('Validation', 'We have successfully updated our database.')
        elif len(correct) == 0:
            tmg.showerror('Validation', f"We were not able to delete {error} as they don't exist in our database.")

    forget(f1, f2, f3)
    f4 = Frame(root, borderwidth='7', relief=SUNKEN, bg='purple')
    f4.pack()
    Label(f4, text='Delete Items', font='ALGERIAN 19 bold').pack()
    f5 = Frame(root, borderwidth='7', relief=SUNKEN, bg='blue')
    f5.pack(pady=10)
    Label(f5, text='Enter the item:-', font='lucid 12 bold', padx=33.4).grid(row=0, column=0, pady=4)
    item = StringVar()
    Entry(f5, textvariable=item, font='12').grid(row=0, column=1, padx=4)
    b3 = Button(root, bg='cyan', text='Submit', font='12', command=submit)
    b3.pack(pady=15)
    b4 = Button(root, bg='cyan', text='Back', font='12', command=back)
    b4.pack(pady=15)


my_db = mysql.connector.connect(host='localhost', user='tesla', passwd='1234', database='items')
my_cursor = my_db.cursor()

root = Tk()
root.geometry('900x700')
root.title('Search your items')

f1 = Frame(root, borderwidth='7', relief=SUNKEN, bg='red')
f1.pack()
Label(f1, text='ITEM MANAGER', font='ALGERIAN 19 bold').pack()

f2 = Frame(root, borderwidth='7', relief=SUNKEN, bg='red')
f2.pack(pady=70)
photo = PhotoImage(file='Search.png')
Label(f2, image=photo).pack()

f3 = Frame(root, borderwidth='7', relief=SUNKEN, bg='red')
f3.pack(pady=100)
Button(f3, text="Enter items' Locations", bg='yellow', font='lucid 10 bold', command=enter).grid(row=0, column=0,
                                                                                                 padx=10, pady=3)
Button(f3, text="Update items' Location", bg='yellow', font='lucid 10 bold', command=update).grid(row=0, column=1,
                                                                                                  padx=10, pady=3)

Button(f3, text='Delete items', bg='yellow', font='lucid 10 bold', command=delete).grid(row=0, column=2, padx=10,
                                                                                        pady=3)
Button(f3, text='Search Items', bg='yellow', font='lucid 10 bold', command=search).grid(row=0, column=3, padx=10,
                                                                                        pady=3)

status = StringVar()
status.set(' ')
s = Label(root, textvariable=status, anchor='w', relief=SUNKEN, bg='grey', fg='white', font='lucid 10 bold')
s.pack(side='bottom', fill=X)
root.mainloop()
