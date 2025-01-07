import pyfiglet
import numpy as np

result = pyfiglet.figlet_format("Acalc", font="slant")
print(result)
print("Welcome to Acalc, the world's first and best Anes Dev calculator with Python programming language, if you want to square root a number enter this 789123, ")

while True:
    try:
        number = float(input("\nPlease enter the first number: "))
        
        
        if number == 789123:
            print("You have entered the square root mode.")
            number_root = float(input("Please enter the number to square root it: "))
            result = number_root ** 0.5
            print(f"The square root is: {result}")
            number = float(input("\nPlease enter the first number: "))
            exit()

        if number == 753951:
            a = list(map(int, input("What is the first line of the first matrix number (separate with comma): ").split(',')))
            b = list(map(int, input("What is the second line of the first matrix number (separate with comma): ").split(',')))
            aa = list(map(int, input("What is the first line of the second matrix number (separate with comma): ").split(',')))
            bb = list(map(int, input("What is the second line of the second matrix number (separate with comma): ").split(',')))

            symbole = input("Choose an operation (+, x, /): ")
            matrix1 = np.array([a, b])
            matrix2 = np.array([aa, bb])

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
            exit()
            
        symbole = input("Choose an operation (+, -, x, /): ")
        number2 = float(input("Please enter your second number: "))
        
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
    
    except ValueError:
        print("You must enter a number, not text. This is a calculator, not a notepad!")
    except KeyboardInterrupt:
        print("The program will be killed")
        break
    except np.linalg.LinAlgError:
        print("Error: Matrix2 is not invertible.")
