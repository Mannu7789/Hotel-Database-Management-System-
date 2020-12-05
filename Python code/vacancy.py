from tkinter import *
from subprocess import call
import mysql.connector
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
newWindow = tk.Toplevel(root)
heading_label = tk.Label(root, text="---------  ALL VACANCIES  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# label
o_label = Label(top_frame, text='OCCUPIED', fg='red', font=('Orbitron', 25))
u_label = Label(top_frame, text='UN-OCCUPIED', fg='green', font=('Orbitron', 25))
o_label.grid(row=0, column=0)
u_label.grid(row=0, column=1)

# text bar
text_o = Text(top_frame, bd=5, fg="red", width=50, bg='#b3ffe6', font=('Teko SemiBold', 20))
text_o.grid(row=1, column=0)

text_u = Text(top_frame, bd=5, fg="green", width=50, bg='#b3ffe6', font=('Teko SemiBold', 20))
text_u.grid(row=1, column=1)

# data Show
rooms = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
         200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210,
         300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310,
         400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410,
         500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510]

mydb = sqlite3.connect('G:\Manz\Project\hotel_database.db')
cur = mydb.cursor()
cur.execute('SELECT roomno from guests')
result = cur.fetchall()
occupied_rooms = []
for i in result:
    a = list(i)
    occupied_rooms.append(a[0])
c1 = 0
c2 = 0
for j in rooms:
    if j in occupied_rooms:
        text_o.insert(INSERT, str(j))
        text_o.insert(INSERT, "\t")
        c1 = c1 + 1
        if c1 == 6:
            text_o.insert(INSERT, "\n")
            c1 = 0
    else:
        text_u.insert(INSERT, str(j))
        text_u.insert(INSERT, "\t")
        c2 = c2 + 1
        if c2 == 6:
            text_u.insert(INSERT, "\n")
            c2 = 0
root.mainloop()