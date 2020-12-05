from subprocess import call
from tkinter import *
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import sqlite3

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')

def click_vacancy():
    call(["python", "G:\Manz\Project\\vacancy.py"])
def click_allcust():
    call(['python', 'G:\Manz\Project\\all_details.py'])
def click_employee():
    call(['python', 'G:\Manz\Project\\employee.py'])
def rate():
    varib=var.get()
    selection = "Value = " + str(var.get())
    label.config(text = selection)
    label.place(relx=0.95, rely=0.45, anchor=E)
    mydb = sqlite3.connect('G:\Manz\Project\hotel_database.db')
    cur = mydb.cursor()
    cur.execute('INSERT INTO rating'
               '(Rate)'
               ' VALUES(?)', 
               (varib,))
    mydb.commit()




# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

view_menu = Menu(menu_bar)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Guest list", command=click_allcust)
view_menu.add_separator()
view_menu.add_command(label="Employee list", command=click_employee)

# variables
F_name = StringVar()
L_name = StringVar()
Room_no = IntVar()

# Database Update
def click_proceed():
    f_name = F_name.get()
    l_name = L_name.get()
    room_no = Room_no.get()

    if f_name == '' or l_name == '' or room_no == 0:
        messagebox.showwarning("Warning", "Incomplete Data Entry")

    else:
        text.delete('1.0', END)
        mydb = sqlite3.connect('G:\Manz\Project\hotel_database.db')
        cur = mydb.cursor()

        cur.execute('Select Exists(select * from guests where fname=? and lname=? and roomno=?)',
                    (f_name, l_name, room_no))

        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]

        if avail == 1:
           cur.execute('SELECT fname,lname,roomno,dur,rtype from guests where roomno=?',
                       (room_no,))
           bill_detail = cur.fetchall()
           cur.execute('DELETE from guests where roomno =?', (room_no,))
           mydb.commit()

           fname_entry.delete(0, 'end')
           lname_entry.delete(0, 'end')
           rn_entry.delete(0, 'end')

            # bill detail
           text.insert(INSERT, "\t\tYou Have successfully checked out --- Kindly Make the payment at counter\n\n")
           formatting = "-------------------------------------------------------------------------------------------" \
                         "-------------------------------------------------------------------------------------------" \
                         "------------------------------------------------------------------------------------------\n"
           text.insert(INSERT, formatting)
           text.insert(INSERT, formatting)
           bill = []
           print(bill_detail)
           for i in bill_detail:
               bill = list(i)
               string_bill = "First Name :\t " + bill[0] + "\n" + "Last Name :\t " + bill[1] + "\n"
               text.insert(INSERT, string_bill)
           s1 = "Room Number :\t " + str(bill[2]) + "\n"
           s2 = "Number of Days :\t " + str(bill[3]) + "\n"
           s3 = "Room Type :\t " + str(bill[4]) + "\n"
           text.insert(INSERT, s1)
           text.insert(INSERT, s2)
           if bill[4] == 1:
               amount = bill[3] * 2000
           else:
               amount = bill[3] * 1500
           s4 = "\nTotal Amount To Be Paid : \t" + str(amount)
           text.insert(INSERT, s4)

        else:
            fname_entry.delete(0, 'end')
            lname_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')
            text.insert(INSERT, "INVALID DATA !!!!!!!\t\t Please Enter Correct Details   !!!!!")


# heading
newWindow = tk.Toplevel(root)
heading_label = tk.Label(root, text="---------  CUSTOMER CHECK OUT FORM  ---------", font=('Orbitron', 15), bg="black",
                      fg="white")
heading_label.pack(fill=X)

black_space = Label(root, text="\n\n")
black_space.pack()

# form Design

top_frame = Frame(root)
top_frame.pack()

# Name Label
fname_label = Label(top_frame, text="First Name : ", font=('Orbitron', 20))
lname_label = Label(top_frame, text="Last Name : ", font=('Orbitron', 20))
fname_entry = Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
lname_entry = Entry(top_frame, textvar=L_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
lname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
lname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# Room Number

rn_label = Label(top_frame, text="Room Number : ", font=('Orbitron', 20))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))

rn_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=2, column=1, ipady=5, ipadx=60, sticky=W)

# Proceed Button
proceed_button = Button(root, text="PROCEED", width=10, bg="#0000b3", fg='White', font=('ARIAL BLACK', 20),
                        relief=RAISED, command=click_proceed)
proceed_button.place(relx=0.5, rely=0.45, anchor=S)

#Rating
var = DoubleVar()
scale = Scale( root, variable = var, from_=0, to=5, orient=HORIZONTAL )
scale.place(relx=0.95, rely=0.40, anchor=E)
sbutton = Button(root, text="Rate",command=rate)
sbutton.place(relx=0.905, rely=0.45, anchor=E)
label = Label(root)
label.pack()

# Billing
text = Text(root, bd=5, bg="white", fg='blue', width=200, font=('Arial', 15))
text.place(rely=0.48)

root.mainloop()