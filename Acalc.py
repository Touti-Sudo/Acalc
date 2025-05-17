import pyfiglet
import numpy as np

result = pyfiglet.figlet_format("Acalc", font="slant")
print(result)
print("Welcome to Acalc, the world's first and best calculator (just terminal) with Python programming language. If you want to square root a number enter this 789123, and if you want to do matrix calculation enter 753951.")

def input_float(prompt):
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def input_matrix_line(prompt, expected_size=None):
    while True:
        try:
            line = input(prompt)
            items = line.split(',')
            if expected_size and len(items) != expected_size:
                print(f"Please enter exactly {expected_size} numbers separated by commas.")
                continue
            return list(map(int, items))
        except ValueError:
            print("Invalid input! Please enter integers separated by commas.")

while True:
    try:
        number = input_float("\nPlease enter the first number: ")

        if number == 789123:
            print("You have entered the square root mode.")
            number_root = input_float("Please enter the number to square root it: ")
            if number_root < 0:
                print("Error: Cannot take the square root of a negative number.")
            else:
                result = number_root ** 0.5
                print(f"The square root is: {result}")
            continue

        if number == 753951:
            print("Matrix mode activated. Please enter 2x2 matrices.")
            a = input_matrix_line("First row of the first matrix (comma-separated, 2 numbers): ", 2)
            b = input_matrix_line("Second row of the first matrix (comma-separated, 2 numbers): ", 2)
            aa = input_matrix_line("First row of the second matrix (comma-separated, 2 numbers): ", 2)
            bb = input_matrix_line("Second row of the second matrix (comma-separated, 2 numbers): ", 2)

            symbole = input("Choose an operation (+, x, /): ")
            matrix1 = np.array([a, b])
            matrix2 = np.array([aa, bb])

            try:
                if symbole == "x":
                    matrix = np.dot(matrix1, matrix2.T)
                    print(f"Result: {matrix}")
                elif symbole == "+":
                    matrix = matrix1 + matrix2
                    print(f"Result: {matrix}")
                elif symbole == "/":
                    matrix2inverse = np.linalg.inv(matrix2)
                    matrix = np.dot(matrix1, matrix2inverse)
                    print(f"Result: {matrix}")
                else:
                    print("Invalid operation selected. Please choose +, x, or /.")
            except np.linalg.LinAlgError:
                print("Error: The second matrix is not invertible.")
            except Exception as e:
                print(f"Matrix calculation error: {e}")
            continue

        symbole = input("Choose an operation (+, -, x, /): ")
        number2 = input_float("Please enter your second number: ")

        if symbole == "x":
            print(f"Result: {number * number2}")
        elif symbole == "+":
            print(f"Result: {number + number2}")
        elif symbole == "-":
            print(f"Result: {number - number2}")
        elif symbole == "/":
            if number2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {number / number2}")
        else:
            print("Invalid operation. Please choose +, -, x, or /.")

    except KeyboardInterrupt:
        print("\nThe program will be terminated by user request.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Returning to main menu.")
