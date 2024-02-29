
from tkinter import *

from tkinter import messagebox
import threading
from datetime import datetime

tasks_list = []
timer= threading


taskist_Count = 1

def add_list(text, time):
    tasks_list.append([text, time])
    timer = threading.Timer(time, time_passed, [text])

    timer.start()
    
    

def time_passed(task):
    
	toplevel =Toplevel(Tk_root)
	toplevel.title("Pop_up")
	h1=Entry(toplevel)
	h1.grid(row=1, column=0)
	h1.insert("0",task)
	Button(toplevel, text="ok", command=exit).grid(row=2, column=0)
    

    
	

def inputError() :
	

	if taskName.get() == "" :
		
		
		messagebox.showerror("Input Error")
		
		return 0
	
	return 1


def clear_taskNumberField() :
	
	
	taskDelete.delete(0.0, END)


def clear_taskField() :

	
	taskName.delete(0, END)
	dateEntry.delete(0,END)
	timeEntry.delete(0,END)
	

def Taskinsertion():

	global taskist_Count
	
	
	value = inputError()

	
	if value == 0 :
		return

	
	content = taskName.get() +"\n"

	
	tasks_list.append(content)

	
	
	taskQueue.insert('end -1 chars', "" + str(taskist_Count) + "-" + content+"\n")

	
	taskist_Count += 1
	text=taskName.get()
	enteredTime=timeEntry.get()
	
	

	ftr = [3600,60]

	sec=sum([a*b for a,b in zip(ftr, map(int,enteredTime.split(':')))])
	now = datetime.now()

	current_time = now.strftime("%H:%M")
	seconds = sum([a*b for a,b in zip(ftr, map(int,current_time.split(':')))])
	if (sec> seconds):
		time=sec-seconds
	else:
		time=seconds-sec
	
	add_list(text, time)


    
	clear_taskField()


def Taskdeletion() :
	
	global taskist_Count
	
	
	if len(tasks_list) == 0 :
		messagebox.showerror("No task")
		return

	
	number = taskDelete.get(1.0, END)

	
	if number == "\n" :
		messagebox.showerror("input error")
		return
	
	else :
		tasknumber = int(number)

	
	clear_taskNumberField()
	
	
	tasks_list.pop(tasknumber - 1)

	
	taskist_Count -= 1
	
	
	taskQueue.delete(1.0, END)

	
	for i in range(len(tasks_list)) :
		taskQueue.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i]+"\n")
Tk_root= Tk()
Tk_root.title('upcoming tasks')
Label(Tk_root, text="Enter Task Name").grid(row=0, column=0)

taskName=Entry(Tk_root)

taskName.grid(row=0, column=1,padx=5,ipady=10, ipadx=20, sticky=W)
Label(Tk_root,text="enter Date").grid(row=0, column=2)
dateEntry= Entry(Tk_root)
dateEntry.grid(row=0, column=3,pady=20, ipady=10, ipadx=20)
Label(Tk_root,text="Enter Time").grid(row=1, column=2, sticky=N)
timeEntry= Entry(Tk_root)
timeEntry.grid(row=1, column=3,pady=10, ipady=10, ipadx=10,sticky=N)
Label(Tk_root,text="enter task number:").grid(row=2, column=2, sticky=W)
taskDelete= Text(Tk_root, height=2, width=4)
taskDelete.grid(row=2, column=3, sticky=W)
Label(Tk_root,text="taskQueue").grid(row=2, column=0)
taskQueue= Text(Tk_root,height = 5, width = 10 )
taskQueue.grid(row=2, column=1, padx=5)
Button1= Button(Tk_root,text='Submit',height = 1, width = 5, command=Taskinsertion )
Button1.grid(row=2, column=3, padx=70,sticky=NW)
Button2= Button(Tk_root,text='Delete',height = 1, width = 5, command=Taskdeletion)
Button2.grid(row=2, column=3,padx=60,pady=40,sticky=SW)

Button3= Button(Tk_root,text='Exit',height = 1, width = 5, command=exit)
Button3.grid(row=2, column=3,padx=60,sticky=SW)



Tk_root.mainloop()