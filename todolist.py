from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("500x400")
root.minsize(500,400)
root.maxsize(500,400)
root.title("TO DO LIST")
value=StringVar()
task=[]
e1=Entry(root,width=38,font=("Arial",15),textvariable=value)
e1.grid(row=0,column=0,columnspan=3,pady=20)
lst1=Listbox(root,width=40,height=8)
lst1.grid(row=3,column=0,columnspan=3,padx=10,pady=20)
def addtask():
    data=value.get()
    task.append(data)
    messagebox.showinfo("","Task Added!")
    e1.delete(0,END)

def track():
    lst1.delete(0,END)
    for i in task:
        lst1.insert(END,i)

def update():
    index=lst1.curselection()
    i=index[0]
    data2=value.get()
    task[i]=data2
    lst1.delete(i)
    lst1.insert(i,data2)
badd=Button(root,text="Add Task",command=addtask).grid(row=1,column=0)
bupdate=Button(root,text="Update Task",command=update).grid(row=1,column=1)
btrack=Button(root,text="Track Task",command=track).grid(row=1,column=2)


root.mainloop()