# CalculatorWithExceptions
This is a simple calculator program written in Python by Joshua Lemuel Z. Centina. The program allows the user to perform basic mathematical operations such as addition, subtraction, multiplication, and division. It also includes exception handling to handle possible errors during the calculations.

## Getting Started

### Installing
1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Copy the code from the repository.
3. Open an IDE and paste the code.
* If you don't have an IDE, you can use any text editor from your computer and paste the code.
4. Save the file with a .py  extension.
5. Run the code.
*  For text-editor users, open a command prompt or terminal window and locate the folder where the Python file was saved and enter the command provided below by typing it in the command-line interface. After typing the command, press the Enter key to execute.

```
python 'file_name'.py
```

6. It will ask you to enter a message and a keyword. Press Enter after inputting your message and after you input your keyword.
7. The encrypted text will be displayed in all uppercase letters.

## How to Use
1. Run the program in a Python environment.
2. The program will display a welcome message and load animation.
3. The user will be prompted to choose an operation by entering a number from 1 to 4:
  * 1: Addition
  * 2: Subtraction
  * 3: Multiplication
  * 4: Division
4. After selecting the operation, the user will be asked to enter two numbers.
5. The program will validate the inputs and handle any exceptions that may occur:
  * If the operation is invalid (not between 1 and 4), a 'ValueError' will be raised.
  * If the first or second number is invalid (not a float), a 'ValueError' will be raised.
  * If the second number is 0 during division, a 'ZeroDivisionError' will be raised.
6. If the inputs are valid, the program will perform the chosen operation and display the result.
7. The user will be asked if they want to perform another calculation:
  * If the user enters "yes," the program will start again from step 3.
  * If the user enters "no," the program will display a goodbye message and exit.
  * If the user enters an invalid option, a ValueError will be raised.

Note: Make sure to have Python installed on your system before running the program.
