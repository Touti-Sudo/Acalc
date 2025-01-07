import pyfiglet

result = pyfiglet.figlet_format("Acalc", font="slant")
print(result)
print("Welcome to Acalc, the world's first Anes Dev calculator with Python programming language")

while True:
    try:
        number = float(input("\nPlease enter the first number: "))
        
        if number == 789123:
            print("You have entered the square root mode.")
            number_root = float(input("Please enter the number to square root it: "))
            result = number_root ** 0.5
            print(f"The square root is: {result}")
            number = float(input("\nPlease enter the first number: "))
         
        
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
