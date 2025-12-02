import tkinter as tk
from tkinter import ttk

def calculate_emi():
    try:
        principal = float(entry_amount.get())
        rate = float(entry_rate.get()) / 12 / 100  # Monthly interest rate
        tenure = int(entry_tenure.get()) * (12 if tenure_type.get() == "Years" else 1)

        # EMI Formula
        emi = (principal * rate * (1 + rate) ** tenure) / ((1 + rate) ** tenure - 1)

        total_payment = emi * tenure
        total_interest = total_payment - principal

        label_result_emi.config(text=f"EMI: ₹ {emi:.2f}")
        label_result_interest.config(text=f"Total Interest: ₹ {total_interest:.2f}")
        label_result_total.config(text=f"Total Payment: ₹ {total_payment:.2f}")

    except:
        label_result_emi.config(text="Error in input!")
        label_result_interest.config(text="")
        label_result_total.config(text="")


# GUI Setup
root = tk.Tk()
root.title("EMI Loan Calculator")
root.geometry("350x400")
root.config(bg="#1e1e1e")

font_large = ("Arial", 14)
font_small = ("Arial", 12)

# Loan Amount
tk.Label(root, text="Loan Amount (₹):", font=font_small, fg="white", bg="#1e1e1e").pack(pady=5)
entry_amount = tk.Entry(root, font=font_large)
entry_amount.pack()

# Interest Rate
tk.Label(root, text="Interest Rate (%):", font=font_small, fg="white", bg="#1e1e1e").pack(pady=5)
entry_rate = tk.Entry(root, font=font_large)
entry_rate.pack()

# Tenure Type
tk.Label(root, text="Tenure Type:", font=font_small, fg="white", bg="#1e1e1e").pack(pady=5)
tenure_type = tk.StringVar(value="Years")
ttk.Combobox(root, textvariable=tenure_type, values=["Years", "Months"], font=font_small).pack()

# Tenure Input
tk.Label(root, text="Tenure:", font=font_small, fg="white", bg="#1e1e1e").pack(pady=5)
entry_tenure = tk.Entry(root, font=font_large)
entry_tenure.pack()

# Calculate Button
tk.Button(
    root,
    text="Calculate EMI",
    font=("Arial", 14),
    bg="#4caf50",
    fg="white",
    command=calculate_emi
).pack(pady=15)

# Result Labels
label_result_emi = tk.Label(root, text="", font=font_small, fg="yellow", bg="#1e1e1e")
label_result_emi.pack()

label_result_interest = tk.Label(root, text="", font=font_small, fg="skyblue", bg="#1e1e1e")
label_result_interest.pack()

label_result_total = tk.Label(root, text="", font=font_small, fg="orange", bg="#1e1e1e")
label_result_total.pack()

root.mainloop()
