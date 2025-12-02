import math

print("----- Simple Calculator with Square Root -----")

op = input("Enter operator (+, -, *, /, sqrt): ")

if op == "sqrt":
    num = float(input("Enter number: "))
    print("Result =", math.sqrt(num))

else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if op == "+":
        print("Result =", num1 + num2)

    elif op == "-":
        print("Result =", num1 - num2)

    elif op == "*":
        print("Result =", num1 * num2)

    elif op == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid operator!")
