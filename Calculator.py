# Joshua Lemuel Z. Centina BSCPE 1-4
# Calculator with Handling Exceptions

# The application will ask the user to choose one of the four math operations(addition, subtraction, multiplication and division). 
# The application will ask for two numbers and perform the chosen operation using then it will display the result.

# pseudocode
import time
import sys
print("=============================================================================")
def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()
typewriter("\033[1;46m" + "Welcome to Joshua Lemuel Z. Centina's Calculator" + "\033[1;m")

print("\nLoading:")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

# ask the user to choose an operation (1-4)
def calculator():
    print("Choose your desired operation:")
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")

# ask for two numbers
    while True:
        try:
            calc_operation = int(input("\nEnter the number of your desired operation (1-4): "))
            if calc_operation < 1 or calc_operation > 4:
                raise ValueError("Invalid operation")
            break  # If no exception occurs and input is valid, exit the loop
        except ValueError:
            print("\033[1;31m" + "Invalid input for the operation. Please enter a number from 1 to 4. Try again." + "\033[1;m")

    while True:
        try:
            num_1 = float(input("\nEnter the first number: "))
            break  # If no exception occurs, exit the loop
        except ValueError:
            print("\033[1;31m" + "Invalid input for the first number. Try again." + "\033[1;m")

    while True:
        try:
            num_2 = float(input("Enter the second number: "))
            if calc_operation == 4 and num_2 == 0:
                raise ZeroDivisionError("\033[1;31m" + "Cannot divide by zero. Please choose another number." + "\033[1;m")
            break
        except ValueError:
            print("\033[1;31m" + "Invalid input for the second number. Try again." + "\033[1;m")
        except ZeroDivisionError as error:
            print(error)
# perform operation and display result
    if calc_operation == 1:
        print(num_1, "+", num_2)
        sum_num = num_1 + num_2
        print("The sum:", "\033[1;43m" + str(sum_num) + "\033[1;m")

    elif calc_operation == 2: 
        print(num_1, "-", num_2)
        diff_num = num_1 - num_2
        print("The difference:", "\033[1;43m" + str(diff_num) + "\033[1;m")
    
    elif calc_operation == 3:
        print(num_1, "*", num_2)
        mult_num = num_1 * num_2
        print("The product:", "\033[1;43m" + str(mult_num) + "\033[1;m")

    elif calc_operation == 4:
        print(num_1, "/", num_2)
        div_num = num_1 / num_2
        print("The quotient:", "\033[1;43m" + str(div_num) + "\033[1;m")
calculator()

# ask user to try again or not
while True:
    try:
        user_retry = input("\nDo you want to perform another calculation? (yes/no): ")
        # if yes, back to step 1
        if user_retry.lower() == "yes":
            print("=============================================================================")
            calculator()
        # if no, thank you and exit program
        elif user_retry.lower() == "no":
            print("\033[1;32m" + "Thank you for using the calculator." + "\033[1;m")
            print("======================================================================")
            break
        else:
            raise ValueError("Invalid input")
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")