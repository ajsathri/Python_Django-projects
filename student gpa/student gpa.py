
import tkinter as tk
from tkinter.ttk import *

master = tk.Tk()



master.title("Student GPA Counter")
s = Style()
s.configure(master, bg='red')

master.geometry("700x250")
master.configure(background="#a9a9a9")


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)





def display():
    
    tot = 0

    
    
    if e4.get() == "A":
        
        
        
        tk.Label(master, text="40").grid(row=3, column=4)
        tot += 40

    
    
    if e4.get() == "B":
        tk.Label(master, text="36").grid(row=3, column=4)
        tot += 36

    
    
    if e4.get() == "C":
        tk.Label(master, text="32").grid(row=3, column=4)
        tot += 32

    
    
    if e4.get() == "D":
        tk.Label(master, text="28").grid(row=3, column=4)
        tot += 28

    
    
    if e4.get() == "P":
        tk.Label(master, text="24").grid(row=3, column=4)
        tot += 24

    
    
    if e4.get() == "F":
        tk.Label(master, text="0").grid(row=3, column=4)
        tot += 0

    
    if e5.get() == "A":
        tk.Label(master, text="40").grid(row=4, column=4)
        tot += 40
    if e5.get() == "B":
        tk.Label(master, text="36").grid(row=4, column=4)
        tot += 36
    if e5.get() == "C":
        tk.Label(master, text="32").grid(row=4, column=4)
        tot += 32
    if e5.get() == "D":
        tk.Label(master, text="28").grid(row=4, column=4)
        tot += 28
    if e5.get() == "P":
        tk.Label(master, text="28").grid(row=4, column=4)
        tot += 24
    if e5.get() == "F":
        tk.Label(master, text="0").grid(row=4, column=4)
        tot += 0

    if e6.get() == "A":
        tk.Label(master, text="30").grid(row=5, column=4)
        tot += 30
    if e6.get() == "B":
        tk.Label(master, text="27").grid(row=5, column=4)
        tot += 27
    if e6.get() == "C":
        tk.Label(master, text="24").grid(row=5, column=4)
        tot += 24
    if e6.get() == "D":
        tk.Label(master, text="21").grid(row=5, column=4)
        tot += 21
    if e6.get() == "P":
        tk.Label(master, text="28").grid(row=5, column=4)
        tot += 24
    if e6.get() == "F":
        tk.Label(master, text="0").grid(row=5, column=4)
        tot += 0

    if e7.get() == "A":
        tk.Label(master, text="40").grid(row=6, column=4)
        tot += 40
    if e7.get() == "B":
        tk.Label(master, text="36").grid(row=6, column=4)
        tot += 36
    if e7.get() == "C":
        tk.Label(master, text="32").grid(row=6, column=4)
        tot += 32
    if e7.get() == "D":
        tk.Label(master, text="28").grid(row=6, column=4)
        tot += 28
    if e7.get() == "P":
        tk.Label(master, text="28").grid(row=6, column=4)
        tot += 24
    if e7.get() == "F":
        tk.Label(master, text="0").grid(row=6, column=4)
        tot += 0

    
    totalcredits.insert("0",str(tot))
   
    
    CGPA.insert("0",str(tot/15))
    





tk.Label(master, text="Name", background="#a9a9a9").grid(row=0, column=0)


tk.Label(master, text="Reg.No", background="#a9a9a9").grid(row=0, column=3)


tk.Label(master, text="Roll.No", background="#a9a9a9").grid(row=1, column=0)



tk.Label(master, text="Srl.No", background="#a9a9a9").grid(row=2, column=0)
tk.Label(master, text="1", background="#a9a9a9").grid(row=3, column=0)
tk.Label(master, text="2", background="#a9a9a9").grid(row=4, column=0)
tk.Label(master, text="3", background="#a9a9a9").grid(row=5, column=0)
tk.Label(master, text="4", background="#a9a9a9").grid(row=6, column=0)


tk.Label(master, text="Subject", background="#a9a9a9").grid(row=2, column=1)
tk.Label(master, text="CSE 501", background="#a9a9a9").grid(row=3, column=1)
tk.Label(master, text="CSE 502", background="#a9a9a9").grid(row=4, column=1)
tk.Label(master, text="CSE 503", background="#a9a9a9").grid(row=5, column=1)
tk.Label(master, text="CSE 504", background="#a9a9a9").grid(row=6, column=1)


tk.Label(master, text="Grade", background="#a9a9a9").grid(row=2, column=2)
e4.grid(row=3, column=2)
e5.grid(row=4, column=2)
e6.grid(row=5, column=2)
e7.grid(row=6, column=2)


tk.Label(master, text="Sub Credit", background="#a9a9a9").grid(row=2, column=3)
tk.Label(master, text="4", background="#a9a9a9").grid(row=3, column=3)
tk.Label(master, text="4", background="#a9a9a9").grid(row=4, column=3)
tk.Label(master, text="3", background="#a9a9a9").grid(row=5, column=3)
tk.Label(master, text="4", background="#a9a9a9").grid(row=6, column=3)

tk.Label(master, text="Credit obtained", background="#a9a9a9").grid(row=2, column=4)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)


button1 = tk.Button(master, text="submit",bg="#D3D3D3",highlightbackground="#D3D3D3", command=display)
button1.configure(bg="light grey")
button1.grid(row=8, column=1)
tk.Label(master, text="Total credit", background="#a9a9a9").grid(row=7, column=3)
totalcredits=Entry(master)

totalcredits.grid(row=7, column=4)
tk.Label(master, text="CGPA", background="#a9a9a9").grid(row=8, column=3)
CGPA=Entry(master)

CGPA.grid(row=8, column=4)

master.mainloop()  