import tkinter as tk
import math

# Main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.config(bg="#1e1e1e")
root.resizable(False, False)

expression = ""

# Entry display
entry = tk.Entry(root, font=("Arial", 22), bd=10,
                 relief=tk.FLAT, bg="#2d2d2d",
                 fg="white", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=20, padx=10, pady=15)

def press(value):
    global expression
    expression += str(value)
    entry.delete(0, tk.END)
    entry.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    entry.delete(0, tk.END)

def calculate():
    global expression
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        expression = ""

# Scientific functions
def sin():
    global expression
    try:
        result = math.sin(math.radians(float(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def cos():
    global expression
    try:
        result = math.cos(math.radians(float(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def tan():
    global expression
    try:
        result = math.tan(math.radians(float(expression)))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def log():
    global expression
    try:
        result = math.log10(float(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

def sqrt():
    global expression
    try:
        result = math.sqrt(float(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        expression = str(result)
    except:
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for btn in row:
        tk.Button(frame, text=btn, font=("Arial", 18),
                  bg="#3a3a3a", fg="white", bd=0,
                  command=lambda b=btn:
                  calculate() if b == '=' else press(b)
                  ).pack(side="left", expand=True, fill="both", padx=3, pady=3)

# Scientific buttons row
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

tk.Button(frame, text="sin", font=("Arial",16), bg="#505050", fg="white", command=sin).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame, text="cos", font=("Arial",16), bg="#505050", fg="white", command=cos).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame, text="tan", font=("Arial",16), bg="#505050", fg="white", command=tan).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame, text="log", font=("Arial",16), bg="#505050", fg="white", command=log).pack(side="left", expand=True, fill="both", padx=3, pady=3)

frame2 = tk.Frame(root, bg="#1e1e1e")
frame2.pack(expand=True, fill="both")

tk.Button(frame2, text="√", font=("Arial",16), bg="#505050", fg="white", command=sqrt).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame2, text="π", font=("Arial",16), bg="#505050", fg="white", command=lambda: press(math.pi)).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame2, text="e", font=("Arial",16), bg="#505050", fg="white", command=lambda: press(math.e)).pack(side="left", expand=True, fill="both", padx=3, pady=3)
tk.Button(frame2, text="C", font=("Arial",16), bg="red", fg="white", command=clear).pack(side="left", expand=True, fill="both", padx=3, pady=3)

root.mainloop()
