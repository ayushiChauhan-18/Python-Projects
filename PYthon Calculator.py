import tkinter as tk
from tkinter import messagebox
import math

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            entry_var.set(result)
            expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            expression = ""
    elif text == "C":
        expression = ""
        entry_var.set("")
    elif text == "DEL": 
        expression = expression[:-1]
        entry_var.set(expression)
    else:
        expression += text
        entry_var.set(expression)

# Initialize window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("500x600")
root.resizable(0, 0)
root.configure(bg="#99FFFF")

expression = ""
entry_var = tk.StringVar()

# Display field
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
button_texts = [
    ("C","#99FFFF"),( "","#D3D3D3"),( "DEL","#99FFFF"), ("=","#F9FBCB"),
    ("/","#F9FBCB"),( "(","#F9FBCB" ),(")","#F9FBCB"),("%","#F9FBCB"),
    ("1","#FFB3BA"), ("2","#FFB3BA"),( "3","#FFB3BA"),( "*","#F9FBCB"),
    ("4","#FFB3BA"),("5","#FFB3BA"), ("6","#FFB3BA") ,("-","#F9FBCB"),
    ("7","#FFB3BA"),("8","#FFB3BA"),( "9","#FFB3BA") ,("+","#F9FBCB"),
    ("log","#F9FBCB"),("0","#FFB3BA"),("00","#FFB3BA"), ("^","#F9FBCB"),
    ("sin","#F9FBCB"),("cos","#F9FBCB"),("tan","#F9FBCB"),(".","#F9FBCB")
]

row, col = 1, 0
for text,color in button_texts:
    if text:
        button = tk.Button(root, text=text, font="Arial 15", padx=20, pady=20,bg=color)
        button.grid(row=row, column=col, sticky="nsew")
        button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Extend functionality for scientific operations
def scientific_eval(event):
    global expression
    if "sin" in expression:
        expression = expression.replace("sin", "math.sin")
    if "cos" in expression:
        expression = expression.replace("cos", "math.cos")
    if "tan" in expression:
        expression = expression.replace("tan", "math.tan")
    if "sqrt" in expression:
        expression = expression.replace("sqrt", "math.sqrt")
    if "log" in expression:
        expression = expression.replace("log", "math.log10")
    if "^" in expression:
        expression = expression.replace("^", "")

entry.bind("<Return>", scientific_eval)

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()




