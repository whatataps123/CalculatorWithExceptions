# Joshua Lemuel Z. Centina BSCPE 1-4
# 20 Integers Odd Even Text Files

# The application will ask the user to choose one of the four math operations(addition, subtraction, multiplication and division). 
# The application will ask for two numbers and perform the chosen operation using then it will display the result.

# pseudocode
# ask the user to choose an operation (1-4)
def calculator():
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
            num_1 = float(input("\nEnter the first number: "))
            break  # If no exception occurs, exit the loop
        except ValueError:
            print("Invalid input for the first number. Try again.")

    while True:
        try:
            num_2 = float(input("Enter the second number: "))
            if calc_operation == 4 and num_2 == 0:
                raise ZeroDivisionError("Cannot divide by zero. Please choose another number.")
            break
        except ValueError:
            print("Invalid input for the second number. Try again.")
        except ZeroDivisionError as error:
            print(error)
# perform operation and display result
    if calc_operation == 1:
        print(num_1, "+", num_2)
        sum_num = num_1 + num_2
        print("The sum:", sum_num)

    elif calc_operation == 2: 
        print(num_1, "-", num_2)
        diff_num = num_1 - num_2
        print("The difference:", diff_num)
    
    elif calc_operation == 3:
        print(num_1, "*", num_2)
        mult_num = num_1 * num_2
        print("The product:", mult_num)

    elif calc_operation == 4:
        print(num_1, "/", num_2)
        div_num = num_1 / num_2
        print("The quotient:", div_num)
calculator()

# ask user to try again or not
while True:
    try:
        user_retry = input("\nDo you want to perform another calculation? (yes/no): ")
        # if yes, back to step 1
        if user_retry.lower() == "yes":
            calculator()
        # if no, thank you and exit program
        elif user_retry.lower() == "no":
            print("Thank you for using Joshua Lemuel Z. Centina's Calculator.")
            break
        else:
            raise ValueError("Invalid input")
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")