# Joshua Lemuel Z. Centina BSCPE 1-4
# 20 Integers Odd Even Text Files

# The application will ask the user to choose one of the four math operations(addition, subtraction, multiplication and division). 
# The application will ask for two numbers and perform the chosen operation using then it will display the result.

# pseudocode
# ask the user to choose an operation (1-4)
print("Joshua Lemuel Z. Centina's Calculator")
print("\nChoose your desired operation:")
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
        print("Invalid input for the operation. Please enter a number from 1 to 4. Try again.")

while True:
    try:
        num_1 = int(input("\nEnter the first number: "))
        break  # If no exception occurs, exit the loop
    except ValueError:
        print("Invalid input for the first number. Try again.")

while True:
    try:
        num_2 = int(input("Enter the second number: "))
        break  # If no exception occurs, exit the loop
    except ValueError:
        print("Invalid input for the second number. Try again.")
# perform operation and display result
# ask user to try again or not
# if yes, back to step 1
# if no, thank you and exit program
