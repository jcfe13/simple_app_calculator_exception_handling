# 1. Define the calculator function
def calculator():

    # 2. Define the addition, subtraction, multiplication, division function
    def add_numbers(first_number, second_number):
        return int(first_number + second_number)

    def subtract_numbers(first_number, second_number):
        return first_number - second_number

    def multiply_numbers(first_number, second_number):
        return first_number * second_number

    def divide_numbers(first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError()
        return first_number / second_number

    # 3. Making the main loop and display the operations
    while True:
        try:
            print("\n\033[96m------- Welcome to the Simple Calculator! -------\033[0m")
            print("\033[94m1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)\033[0m")
            
            # 4. Get the user's choice
            while True:
                try:
                    operation_choice = int(input("Enter the number of the operation you want to perform (1-4): "))
                    if operation_choice not in [1, 2, 3, 4]:
                        raise ValueError
                    break
                except ValueError:
                    print("\n\033[91mValueError: You have entered an invalid character, number, or choice. Please enter a number between 1-4.\033[0m\n")

            # 5. Get the numbers
            first_num = float(input("\n\033[93mPlease enter your first number: "))
            second_num = float(input("\033[93mPlease enter your second number: "))

            # 6. Perform the operation
            if operation_choice == 1:
                result = add_numbers(first_num, second_num)
                operation = "\033[95mAddition\033[0m"
            elif operation_choice == 2:
                result = subtract_numbers(first_num, second_num)
                operation = "\033[95mSubtraction\033[0m"
            elif operation_choice == 3:
                result = multiply_numbers(first_num, second_num)
                operation = "\033[95mMultiplication\033[0m"
            elif operation_choice == 4:
                result = divide_numbers(first_num, second_num)
                operation = "\033[95mDivision\033[0m"

            # 7. Ensure accurate handling of decimals
            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 2)

        # 8. Display the result and the exception
            print(f"\n\033[95mThe result for the {operation} \033[95mis: \033[94m{result}\033[95m\033[0m")

        except ValueError as e:
            print("\n\033[91mValueError:", e, "\033[0m")

        except ZeroDivisionError:
            print("\n\033[91mZeroDivisionError: Division by zero is not a valid operation. 033[0m")

        except Exception as exception:
            print("\n\033[91mAn error occurred. Please try again.", exception, "\033[0m")

        # 9. Inquire if they want to do more math
        while True:
            try:
                repeat_calculation = input("\n\033[93mDo you want to perform another calculation? ('y' for Yes / 'n' for No): ").strip().lower()
                if repeat_calculation not in ['y', 'n']:
                    raise ValueError("\n\033[91mValueError: Invalid input. Please enter 'y' for Yes or 'n' for No.\033[0m")
                break

            except ValueError as exception:
                print(exception)
                
        # 10. If they're finished, say "Thank you!" and end
        if repeat_calculation != 'y':
            print("\n\033[95mThank You for using this Simple App Calculator.")
            break

# 11. Call the main function to run the calculator
calculator()