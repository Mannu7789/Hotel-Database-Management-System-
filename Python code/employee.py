from tkinter import *
from subprocess import call
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

# heading
heading_label = Label(root, text="---------  ALL EMPLOYEES  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# employee text view
text = Text(root, bd=5, bg="white", fg='blue', width=200, font=('Arial', 15))
text.place(rely=0.1)

# database
mydb = sqlite3.connect('G:\Manz\Project\hotel_database.db')
cur = mydb.cursor()
cur.execute('SELECT * from employee')
result = cur.fetchall()

title = "First Name\t\t Last Name\t\t Phone Number\t\t Email id\t\t\t    Address\t\t Designation\n"
text.insert(INSERT, title)
formatting = "-------------------------------------------------------------------------------------------" \
             "-------------------------------------------------------------------------------------------" \
             "------------------------------------------------------------------------------------------\n"
text.insert(INSERT, formatting)
text.insert(INSERT, formatting)
for i in result:
    a = list(i)
   
    s = a[0] + "\t\t" + a[1] + "\t\t" + str(a[2]) + "\t\t" + a[3] + "\t\t\t   " + a[4] + "\t\t" + a[5] + "\n\n"
    text.insert(INSERT, s)

root.mainloop()