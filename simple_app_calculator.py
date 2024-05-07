# 1. Define the calculator function
def calculator():
    # 2. Define the addition, subtraction, multiplication, division function
    def add_numbers(first_number, second_number):
        return int(first_number + second_number) \
            if first_number.is_integer() and second_number.is_integer() \
            else first_number + second_number
    def subtract_numbers(first_number, second_number):
        return first_number - second_number
    def multiply_numbers(first_number, second_number):
        return first_number * second_number
    def divide_numbers(first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError()
        return first_number / second_number
    # 3. Making the main loop and display the operations
# 4. Get the user's choice
# 5. Get the numbers
# 6. Perform the operation
# 7. Ensure proper handling of any mistakes
# 8. Display the result and the exception
# 9. Inquire if they want to do more math
# 10. If they're finished, say "Thank you!" and end
# 11. Call the main function to run the calculator