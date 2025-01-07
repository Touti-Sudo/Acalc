# Acalc - The Anes Dev Calculator 🚀

Acalc is a simple and interactive calculator built with Python. It allows users to perform basic arithmetic operations and even calculate square roots in a user-friendly command-line interface. The calculator is designed to make mathematical operations straightforward and accessible for everyday use. 🧮

## Features ✨

- Perform basic arithmetic operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x`)
  - Division (`/`)
- Square root mode: Easily calculate the square root of a number by entering a special code (789123).
- Interactive and user-friendly. 💻
- matrix mode : Easily do matrix calculations by entering a special code (753951).
  
## How It Works 🛠️

1. The user enters the first number.
2. If the user enters `789123`, the calculator switches to square root mode. 🧠
3. The user selects an operation (`+`, `-`, `x`, `/`) or inputs numbers for further calculations.
4. The program validates inputs and performs the requested operation.
5. The user can repeat operations until they choose to exit.

## Example Usage 📝

```
    ___              __    
   /   | _________ _/ /____
  / /| |/ ___/ __ `/ / ___/
 / ___ / /__/ /_/ / / /__  
/_/  |_\___/\__,_/_/\___/  

Welcome to Acalc, the world's first Anes Dev calculator with Python programming language

Please enter the first number: 10
Choose an operation (+, -, x, /): x
Please enter your second number: 5
Result: 50

Please enter the first number: 789123
You have entered the square root mode.
Please enter the number to square root it: 25
The square root is: 5.0
```

## Prerequisites 📋

- Python 3.6 or higher
- `pyfiglet` library (install with `pip install pyfiglet`)
- 'numpy' library (install with "pip install numpy")
## Installation 📥

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/acalc.git
   cd acalc
   ```

2.```bash
  pip install -r requirements
  ```

4. Run the script:
   ```bash
   python acalc.py
   ```

## Error Handling ⚠️

- Ensures only valid numbers are entered.
- Prevents division by zero.
- Guides users to choose valid operations.
- Handles keyboard interruptions gracefully.

## Disclaimer 🛑

This calculator is intended for educational and general use purposes. While it strives to ensure accurate calculations, it is not designed for high-precision scientific computations.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

