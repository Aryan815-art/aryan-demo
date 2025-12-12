#aryan.demo
import numpy as np

def get_matrix(n):
    print(f"\nEnter values for Matrix {n} (row by row, separated by spaces):")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix = []
    print("Enter each row:")
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    return np.array(matrix)

def menu():
    print("\n===== MATRIX CALCULATOR =====")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of a Matrix")
    print("5. Determinant")
    print("6. Inverse")
    print("7. Exit")
    return int(input("Choose an option: "))

while True:
    choice = menu()

    # ADD
    if choice == 1:
        A = get_matrix("A")
        B = get_matrix("B")
        if A.shape == B.shape:
            print("\nResult of Addition:\n", A + B)
        else:
            print("Matrices must be of the same size!")

    # SUBTRACT
    elif choice == 2:
        A = get_matrix("A")
        B = get_matrix("B")
        if A.shape == B.shape:
            print("\nResult of Subtraction:\n", A - B)
        else:
            print("Matrices must be of the same size!")

    # MULTIPLY
    elif choice == 3:
        A = get_matrix("A")
        B = get_matrix("B")
        try:
            print("\nResult of Multiplication:\n", A @ B)
        except:
            print("Column of A must match row of B!")

    # TRANSPOSE
    elif choice == 4:
        A = get_matrix("A")
        print("\nTranspose:\n", A.T)

    # DETERMINANT
    elif choice == 5:
        A = get_matrix("A")
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant:", np.linalg.det(A))
        else:
            print("Matrix must be square!")

    # INVERSE
    elif choice == 6:
        A = get_matrix("A")
        if A.shape[0] == A.shape[1]:
            try:
                print("\nInverse:\n", np.linalg.inv(A))
            except np.linalg.LinAlgError:
                print("Matrix is singular! No inverse exists.")
        else:
            print("Matrix must be square!")

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
