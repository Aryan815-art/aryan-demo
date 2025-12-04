import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)    # Speed of speech

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def menu():
    print("\n===== TALKING CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (×)")
    print("4. Division (÷)")
    print("5. Square Root (√)")
    print("6. Square (x²)")
    print("7. Cube (x³)")
    print("8. Percentage (%)")
    print("9. Exit")
    return int(input("Choose one option: "))

def get_two_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

while True:
    choice = menu()


    if choice == 1:
        a, b = get_two_numbers()
        result = a + b
        speak(f"The answer is {result}")
    elif choice == 2:
        a, b = get_two_numbers()
        result = a - b
        speak(f"The answer is {result}")

    elif choice == 3:
        a, b = get_two_numbers()
        result = a * b
        speak(f"The answer is {result}")

    elif choice == 4:
        a, b = get_two_numbers()
        if b == 0:
            speak("Error. Division by zero is not allowed.")
        else:
            result = a / b
            speak(f"The answer is {result}")

    elif choice == 5:
        import math
        a = float(input("Enter number: "))
        result = math.sqrt(a)
        speak(f"The square root is {result}")

    elif choice == 6:
        a = float(input("Enter number: "))
        result = a * a
        speak(f"{a} squared is {result}")

    elif choice == 7:
        a = float(input("Enter number: "))
        result = a ** 3
        speak(f"The cube of {a} is {result}")
    
    elif choice == 8:
        a = float(input("Enter total value: "))
        b = float(input("Enter percentage: "))
        result = (a * b) / 100
        speak(f"{b} percent of {a} is {result}")

    elif choice == 9:
        speak("Thank you for using the talking calculator. Goodbye.")
        break

    else:
        speak("Invalid option. Please try again.")