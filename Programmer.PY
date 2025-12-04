def menu():
    print("\n========== PROGRAMMER CALCULATOR ==========")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Bitwise AND")
    print("8. Bitwise OR")
    print("9. Bitwise XOR")
    print("10. Bitwise NOT")
    print("11. Left Shift")
    print("12. Right Shift")
    print("13. Exit")
    print("===========================================")
    return int(input("Enter your choice: "))

while True:
    choice = menu()

    # Decimal to Binary
    if choice == 1:
        d = int(input("Enter Decimal Number: "))
        print("Binary:", bin(d)[2:])

    # Decimal to Octal
    elif choice == 2:
        d = int(input("Enter Decimal Number: "))
        print("Octal:", oct(d)[2:])

    # Decimal to Hexadecimal
    elif choice == 3:
        d = int(input("Enter Decimal Number: "))
        print("Hexadecimal:", hex(d)[2:].upper())

    # Binary to Decimal
    elif choice == 4:
        b = input("Enter Binary Number: ")
        print("Decimal:", int(b, 2))

    # Octal to Decimal
    elif choice == 5:
        o = input("Enter Octal Number: ")
        print("Decimal:", int(o, 8))

    # Hex to Decimal
    elif choice == 6:
        h = input("Enter Hexadecimal Number: ")
        print("Decimal:", int(h, 16))

    # Bitwise AND
    elif choice == 7:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        print("AND =", a & b)

    # Bitwise OR
    elif choice == 8:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        print("OR =", a | b)

    # Bitwise XOR
    elif choice == 9:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        print("XOR =", a ^ b)

    # Bitwise NOT
    elif choice == 10:
        a = int(input("Enter number: "))
        print("NOT =", ~a)

    # Left Shift
    elif choice == 11:
        a = int(input("Enter number: "))
        s = int(input("Shift by: "))
        print("Left Shift =", a << s)

    # Right Shift
    elif choice == 12:
        a = int(input("Enter number: "))
        s = int(input("Shift by: "))
        print("Right Shift =", a >> s)

    elif choice == 13:
        print("Exiting Programmer Calculator...")
        break

    else:
        print("Invalid choice! Try again.")
