import tkinter as tk

# Global variables to store state
first_number = None
operation = None

def number_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    global first_number, operation
    entry.delete(0, tk.END)
    first_number = None
    operation = None

def add():
    global first_number, operation
    first_number = float(entry.get())
    operation = "+"
    entry.delete(0, tk.END)

def subtract():
    global first_number, operation
    first_number = float(entry.get())
    operation = "-"
    entry.delete(0, tk.END)

def multiply():
    global first_number, operation
    first_number = float(entry.get())
    operation = "*"
    entry.delete(0, tk.END)

def divide():
    global first_number, operation
    first_number = float(entry.get())
    operation = "/"
    entry.delete(0, tk.END)

def calculate():
    global first_number, operation
    try:
        second_number = float(entry.get())
        entry.delete(0, tk.END)

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                entry.insert(0, "Error")
                return
            result = first_number / second_number
        else:
            entry.insert(0, "Error")
            return

        entry.insert(0, str(result))
        first_number = None
        operation = None

    except Exception:
        entry.insert(0, "Error")

# ==== GUI ====
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=20, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Number buttons
tk.Button(root, text='7', width=5, height=2, command=lambda: number_click('7')).grid(row=1, column=0)
tk.Button(root, text='8', width=5, height=2, command=lambda: number_click('8')).grid(row=1, column=1)
tk.Button(root, text='9', width=5, height=2, command=lambda: number_click('9')).grid(row=1, column=2)
tk.Button(root, text='/', width=5, height=2, command=divide).grid(row=1, column=3)

tk.Button(root, text='4', width=5, height=2, command=lambda: number_click('4')).grid(row=2, column=0)
tk.Button(root, text='5', width=5, height=2, command=lambda: number_click('5')).grid(row=2, column=1)
tk.Button(root, text='6', width=5, height=2, command=lambda: number_click('6')).grid(row=2, column=2)
tk.Button(root, text='*', width=5, height=2, command=multiply).grid(row=2, column=3)

tk.Button(root, text='1', width=5, height=2, command=lambda: number_click('1')).grid(row=3, column=0)
tk.Button(root, text='2', width=5, height=2, command=lambda: number_click('2')).grid(row=3, column=1)
tk.Button(root, text='3', width=5, height=2, command=lambda: number_click('3')).grid(row=3, column=2)
tk.Button(root, text='-', width=5, height=2, command=subtract).grid(row=3, column=3)

tk.Button(root, text='0', width=5, height=2, command=lambda: number_click('0')).grid(row=4, column=0)
tk.Button(root, text='.', width=5, height=2, command=lambda: number_click('.')).grid(row=4, column=1)
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=4, column=2)
tk.Button(root, text='+', width=5, height=2, command=add).grid(row=4, column=3)

# Clear button
tk.Button(root, text='C', width=22, height=2, command=clear).grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()
