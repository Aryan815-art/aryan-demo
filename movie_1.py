import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.withdraw()   # Hide main screen


# 1. Movie Name
movie = simpledialog.askstring("Movie Name", "Enter Movie Name:")
if not movie:
    messagebox.showwarning("Warning", "Movie name is required!")
    exit()


# 2. Runtime (HH:MM)
time_input = simpledialog.askstring("Runtime", "Enter Runtime (HH:MM):")
if not time_input:
    messagebox.showwarning("Warning", "Runtime is required!")
    exit()

# Validate time 
try:
    hours, minutes = time_input.split(":")
    hours = int(hours)
    minutes = int(minutes)
    formatted_time = f"{hours:02d}:{minutes:02d}"
except:
    messagebox.showerror("Error", "Invalid time format! Use HH:MM")
    exit()


# 3. Budget
budget = simpledialog.askinteger("Budget", "Enter Budget (₹):")
if budget is None:
    messagebox.showwarning("Warning", "Budget is required!")
    exit()


# 4. Collection
collection = simpledialog.askinteger("Collection", "Enter Box Office Collection (₹):")
if collection is None:
    messagebox.showwarning("Warning", "Collection is required!")
    exit()


# 5. Music Director Name
music_director = simpledialog.askstring("Music Director", "Enter Music Director Name:")
if not music_director:
    messagebox.showwarning("Warning", "Music Director is required!")
    exit()


# -------------------------
# ⭐ HIT / SUPER HIT LOGIC
# -------------------------

status = ""

if collection < budget:
    status = "Flop"
elif collection >= budget * 1.80:
    status = "Super Hit"
elif collection >= budget * 1.50:
    status = "Hit"
else:
    status = "Average"


# Final Summary Message
messagebox.showinfo(
    "Movie Details",
    f"Movie: {movie}\n"
    f"Runtime: {formatted_time}\n"
    f"Budget: ₹{budget}\n"
    f"Collection: ₹{collection}\n"
    f"Music Director: {music_director}\n"
    f"Status: {status}\n\n"
    "Thank You for Visiting!"
)