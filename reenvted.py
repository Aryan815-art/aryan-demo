import tkinter as tk
import math

def calculate():
    try:
        expr = entry.get()

        if "√" in expr:
            num = float(expr.replace("√", ""))
            result = math.sqrt(num)

        elif "^" in expr:
            base, exp = expr.split("^")
            result = float(base) ** float(exp)

        elif "%" in expr:
            num, per = expr.split("%")
            result = (float(num) * float(per)) / 100

        else:
            result = eval(expr)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 18), border=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "√","x²","x³","^",
    "%","C"
]

row = 1
col = 0

def press(val):
    if val == "=":
        calculate()
    elif val == "C":
        entry.delete(0, tk.END)
    elif val == "x²":
        entry.insert(tk.END, "^2")
    elif val == "x³":
        entry.insert(tk.END, "^3")
    elif val == "√":
        entry.insert(tk.END, "√")
    else:
        entry.insert(tk.END, val)

for b in buttons:
    tk.Button(root, text=b, width=5, height=2, font=("Arial", 14),
              command=lambda x=b: press(x)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
