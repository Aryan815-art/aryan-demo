import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()

        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("π", "math.pi")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("e", "math.e")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("^", "**")

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def press(symbol):
    elif symbol == "SPACE":     # <-- NEW SPACE BUTTON
    if symbol == "C":
        entry.delete(0, tk.END)
    elif symbol == "=":
        calculate()
        entry.insert(tk.END, " ")
    elif symbol == "x²":
        entry.insert(tk.END, "**2")
    elif symbol == "x³":
        entry.insert(tk.END, "**3")
    elif symbol == "√":
        entry.insert(tk.END, "√(")
    elif symbol == "!":
        try:
            num = int(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, math.factorial(num))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, symbol)

root = tk.Tk()
root.title("Scientific Calculator")
root.configure(bg="#1e1e1e")

entry = tk.Entry(
    root, width=25, font=("Arial", 22),
    bd=8, relief=tk.RIDGE, justify="right"
)
entry.grid(row=0, column=0, columnspan=6, pady=10)

buttons = [
    ["7", "8", "9", "/", "sin", "cos"],
    ["4", "5", "6", "*", "tan", "log"],
    ["1", "2", "3", "-", "ln",  "√"],
    ["0", ".", "%", "+", "x²", "x³"],
    ["(", ")", "^", "π", "e", "!"],
    ["SPACE", "C", "="]   # <-- NEW SPACE BUTTON ADDED HERE
]

row_index = 1
for row in buttons:
    col_index = 0
    for symbol in row:
        tk.Button(
            root,
            text=symbol,
            width=6,
            height=2,
            font=("Arial", 16),
            bg="#2d2d2d",
            fg="white",
            activebackground="#4d4d4d",
            command=lambda x=symbol: press(x)
        ).grid(row=row_index, column=col_index, padx=5, pady=5)
        col_index += 1
    row_index += 1

root.mainloop()
