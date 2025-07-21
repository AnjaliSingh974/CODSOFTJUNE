from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("600x500")
root.minsize(600,500)

root.title("Contact Book")
contact=[]
l1=Label(root,text="Select an option:",font=("Arial",10))
l1.grid(row=0,column=0)

list1=Listbox(root,width=55,height=14)
lname=Label(root,text="Name:",font=("Arial",10))
ename=Entry(root,width=20,font=("Arial",10))
lphone=Label(root,text="Phone:",font=("Arial",10))
ephone=Entry(root,width=20,font=("Arial",10))
lemail=Label(root,text="Email:",font=("Arial",10))
eEmail=Entry(root,width=20,font=("Arial",10))
ladress=Label(root,text="Adress:",font=("Arial",10))
eadress=Entry(root,width=20,font=("Arial",10))


def addContact():
    lname.grid(row=1,column=5,padx=100,sticky="w")
    ename.grid(row=1,column=5,padx=150)
    lphone.grid(row=2,column=5,padx=100,pady=0,sticky="w")
    ephone.grid(row=2,column=5,padx=150)
    lemail.grid(row=3,column=5,padx=100,sticky="w")
    eEmail.grid(row=3,column=5,padx=150)
    ladress.grid(row=4,column=5,padx=100,sticky="w")
    eadress.grid(row=4,column=5,padx=150)
    badd2.grid(row=5,column=5,padx=150)

def save():
    name=ename.get()
    phone=ephone.get()
    email=eEmail.get()
    adress=eadress.get()
    newcontact= {"name":name,
                 "phone":phone,
                 "email":email,
                 "adress":adress}
    contact.append(newcontact)
    messagebox.showinfo("","Contact Saved!")
    ename.delete(0,END)
    ephone.delete(0,END)
    eEmail.delete(0,END)
    eadress.delete(0,END)

def view():
    lname.grid_forget()
    lphone.grid_forget()
    lemail.grid_forget()
    ladress.grid_forget()
    ename.grid_forget()
    ephone.grid_forget()
    eEmail.grid_forget()
    eadress.grid_forget()
    badd2.grid_forget()
    list1.grid(row=2,column=5,padx=100)
    for i in contact:
        list1.insert(END, f"Name: {i['name']} | Phone: {i['phone']} | Email: {i['email']} | Address: {i['adress']}")

esearch=Entry(root,width=20,font=("Arial",10))

def search():
    esearch.grid(row=1,column=5,padx=150)
    bsearch2.grid(row=2,column=5,padx=150)
    lname.grid_forget()
    lphone.grid_forget()
    lemail.grid_forget()
    ladress.grid_forget()
    ename.grid_forget()
    ephone.grid_forget()
    eEmail.grid_forget()
    eadress.grid_forget()
    badd2.grid_forget()

    

lresult=Label(root,text="", font=("Arial", 12))
def find():
    search = esearch.get()
 
    found = False
    for i in contact:
        if i["name"] == search:
            lresult.config(text=f"Name: {i['name']}, Phone: {i['phone']}, Email: {i['email']}, Address: {i['adress']}")
            lresult.grid(row=3, column=5, padx=150, pady=10)
            found = True
            break

    if not found:
        lresult.config(text="Contact not found.")
        lresult.grid(row=3, column=5, padx=150, pady=10)

def delete():
    esearch.grid(row=1,column=5,padx=150)
    bdelete2.grid(row=2,column=5,padx=150)
    lname.grid_forget()
    lphone.grid_forget()
    lemail.grid_forget()
    ladress.grid_forget()
    ename.grid_forget()
    ephone.grid_forget()
    eEmail.grid_forget()
    eadress.grid_forget()
    badd2.grid_forget()

def delete2():
    search = esearch.get()
    for i in contact:
        if i["name"] == search:
            contact.remove(i)
            lresult.config(text=f"Contact '{search}' deleted successfully.")
            lresult.grid(row=3, column=5, padx=150, pady=10)
            break
    else:
        lresult.config(text="Contact not found.")
        lresult.grid(row=3, column=5, padx=150, pady=10)

bdelete2=Button(root,text="Delete Contact",width=10,height=2,command=lambda:delete2())
bsearch2=Button(root,text="Search",width=10,height=2,command=lambda:find())
badd2=Button(root,text="Save",width=10,height=2,command=lambda:save())
badd=Button(root,text="Add Contact",width=15,height=3,command=addContact).grid(row=1,column=0,padx=5,pady=4)
bview=Button(root,text="View Contact",width=15,height=3,command=lambda:view()).grid(row=2,column=0,padx=5,pady=4)
bsearch=Button(root,text="Search Contact",width=15,height=3,command=lambda:search()).grid(row=3,column=0,padx=5,pady=4)
#bupdate=Button(root,text="Update Contact",width=15,height=3).grid(row=4,column=0,padx=5,pady=4)
bdelete=Button(root,text="Delete Contact",width=15,height=3,command=lambda:delete()).grid(row=5,column=0,padx=5,pady=4)
root.mainloop()