from tkinter import *
import tkinter.ttk as ttk
import csv
import AttendanceProject

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 900
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

topFrame = Frame(root)


TableMargin = Frame(root, height=200, width=500)
TableMargin.pack(side=LEFT)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Name", "Date", "Time"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.pack()

with open('Attendance.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        Name = row['Name']
        Date = row['Date']
        Time = row['Time']
        tree.insert("", 0, values=(Name, Date, Time))

R = ttk.Button(text="Run", command=AttendanceProject.project)
R.pack(side = RIGHT)

if __name__ == '__main__':
    root.mainloop()