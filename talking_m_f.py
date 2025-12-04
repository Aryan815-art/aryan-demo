import tkinter as tk
import pyttsx3
import threading

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Get available voices
voices = engine.getProperty('voices')

def set_voice(choice):
    if choice == "Male":
        engine.setProperty('voice', voices[0].id)  # Usually male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Usually female voice

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run).start()

# Calculator logic
def button_click(value):
    speak(str(value))
    entry.insert(tk.END, value)

def clear():
    speak("Clear")
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get()
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
        speak(f"The result is {result}")
    except:
        speak("Error")
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# GUI window
root = tk.Tk()
root.title("Talking Calculator - Male/Female Voice")
root.geometry("380x560")
root.config(bg="black")

# Voice selection
tk.Label(root, text="Select Voice:", bg="black", fg="white",
         font=("Arial", 14)).pack(pady=5)

voice_choice = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=voice_choice, value="Male",
               command=lambda: set_voice("Male"),
               bg="black", fg="white", font=("Arial", 12), selectcolor="black").pack()

tk.Radiobutton(root, text="Female", variable=voice_choice, value="Female",
               command=lambda: set_voice("Female"),
               bg="black", fg="white", font=("Arial", 12), selectcolor="black").pack()

# Entry box
entry = tk.Entry(root, font=("Arial", 26), justify="right", bd=8, relief="sunken")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Buttons
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]

for row in buttons:
    frame = tk.Frame(root, bg="black")
    frame.pack(expand=True, fill="both")
    for char in row:
        def make_lambda(x=char):
            if x == "=":
                return calculate
            return lambda: button_click(x)
        
        tk.Button(frame, text=char, font=("Arial", 22),
                  bg="#222", fg="white",
                  command=make_lambda(char),
                  width=4, height=2).pack(
                  side="left", expand=True, fill="both",
                  padx=5, pady=5)

# Clear button
tk.Button(root, text="CLEAR", font=("Arial", 22),
          bg="red", fg="white",
          command=clear).pack(
          expand=True, fill="both",
          padx=10, pady=10)

root.mainloop()
