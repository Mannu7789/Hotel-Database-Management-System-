
from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
import tkinter as tk
import sqlite3

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')

# calling functions
def click_vacancy():
    call(["python", "G:\Manz\Project\\vacancy.py"])
def click_allcust():
    call(['python', 'G:\Manz\Project\\all_details.py'])
def click_employee():
    call(['python', 'G:\Manz\Project\\employee.py'])

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
Phone = IntVar()
Email = StringVar()
Address = StringVar()
Room_no = IntVar()
Room_type = IntVar()
Room_type.set(1)
No_days = IntVar()


# Database Submitted
def click_submit():
    f_name = F_name.get()
    l_name = L_name.get()
    phone = Phone.get()
    email = Email.get()
    address = Address.get()
    room_no = Room_no.get()
    room_type = Room_type.get()
    no_days = No_days.get()


    if f_name == '' or l_name == '' or phone == 0 or email == '' or address == '' or room_no == 0 or room_type == '' or no_days == 0:
        messagebox.showwarning("Warning", "Incomplete Data Entry")

    else:
        mydb = sqlite3.connect('G:\Manz\Project\hotel_database.db')
        
       
        cur = mydb.cursor()
        cur.execute('Select Exists(select * from guests where roomno=?)', (room_no,))
        res = cur.fetchall()
        avail = 0

        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 0:
            cur.execute('INSERT INTO guests'
                        '(fname,lname, mob,email,addr,roomno,dur,rtype)'
                        
                        ' VALUES(?,?,?,?,?,?,?,?)',
                        (f_name, l_name, phone, email,address,room_no,no_days,room_type))

          
            mydb.commit()
            	

            fname_entry.delete(0, 'end')
            lname_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            ad_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')

            messagebox.showinfo("Check in", "Room Allotment Successful")
            root.destroy()
        else:
        	messagebox.showinfo("Room", "Room Already Occupied")
        	rn_entry.delete(0, 'end')



# heading
newWindow = tk.Toplevel(root)
heading_label = tk.Label(root, text="---------  CUSTOMER CHECK IN FORM  ---------", font=('Orbitron', 15), bg="black",
                      fg="white")
heading_label.pack(fill=X)

black_space = tk.Label(root, text="\n\n")
black_space.pack()

# form Design

top_frame = Frame(root)
top_frame.pack()

# Name Label
fname_label = tk.Label(top_frame, text="First Name : ", font=('Orbitron', 20))
lname_label = tk.Label(top_frame, text="Last Name : ", font=('Orbitron', 20))
fname_entry = tk.Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
lname_entry = tk.Entry(top_frame, bd=5, textvar=L_name, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
lname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
lname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# phone number
phone_label = Label(top_frame, text="Mobile Number : ", font=('Orbitron', 20))
phone_entry = Entry(top_frame, textvar=Phone, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

phone_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
phone_entry.grid(row=2, column=1, ipady=5, ipadx=60)

# Email Address
email_label = Label(top_frame, text="Email Address : ", font=('Orbitron', 20))
email_entry = Entry(top_frame, textvar=Email, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

email_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
email_entry.grid(row=3, column=1, ipady=5, ipadx=60)

# Address
ad_label = Label(top_frame, text=" Address : ", font=('Orbitron', 20))
ad_entry = Entry(top_frame, bd=5, textvar=Address, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

ad_label.grid(row=4, column=0, padx=15, pady=10, sticky=E)
ad_entry.grid(row=4, column=1, ipady=5, ipadx=60)

# Room Number

rn_label = Label(top_frame, text="Room Number : ", font=('Orbitron', 20))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))

rn_label.grid(row=5, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=5, column=1, ipady=5, ipadx=60, sticky=W)	

# Number of Days
day_label = Label(top_frame, text="Number of Days : ", font=('Orbitron', 20))
day_box = Spinbox(top_frame, textvar=No_days, bg="#ccefff", fg='blue', from_=1, to=30, width=5, bd=5,
                  font=('Orbitron', 15))

day_label.grid(row=6, column=0, padx=15, pady=10, sticky=E)
day_box.grid(row=6, column=1, ipady=5, sticky=W)

# room Type
room_label = Label(top_frame, text="Room Type : ", font=('Orbitron', 20))
ac_rb = Radiobutton(top_frame, variable=Room_type, text="AC Room", fg='blue', font=('Arial', 12, 'bold'), value=1)
nac_rb = Radiobutton(top_frame, variable=Room_type, text="Non-AC Room", fg='blue', font=('Arial', 12, 'bold'), value=2)

room_label.grid(row=7, column=0, padx=15, pady=10, sticky=E)
ac_rb.grid(row=7, column=1, sticky=W)
nac_rb.grid(row=7, column=1, sticky=E)


# vacancy Button
v_button = Button(top_frame, text="Vacancy", font=('ARIAL BLACK', 15), bg='#80002a',
                  fg='White', width=10, command=click_vacancy)
v_button.grid(row=5, column=1, ipadx=7, sticky=E)

# Submit Button
submit_button = tk.Button(root, text="SUBMIT", width=15, bg="#269900", fg='Black', font=('ARIAL BLACK', 20), relief=RAISED,
                       command=click_submit)
submit_button.place(relx=0.5, rely=0.85, anchor=S)

root.mainloop()