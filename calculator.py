#Creating a basic calculator using Python10
import os

def calculation():
    num1 = float(input("Enter the First Number: "))

    continue_flag = True
    while continue_flag:
        operation = input("Choose the operation ('+','-','*','/','%','^') : ")

        if operation not in ['+','-','*','/','%','^']:
                is_true = True
                while is_true:
                    operation = input("Choose valid operation : ")
                    if operation in ['+','-','*','/','%','^']:
                        is_true = False

        

        num2 = float(input("Enter the Second Number: "))

        try:
            if operation == "+":
                output = num1 + num2 
            elif operation == "-":
                output = num1 - num2
            elif operation == "*":
                output = num1 * num2
            elif operation == "/":
                output = num1 / num2 
            elif operation == "%":
                output = num1 % num2 
            elif operation == "^":
                output = num1 ** num2
            else:
                output = f"Invalid operation {output} selected -> CHOOSE VALID OPERATION"

        except ZeroDivisionError:
            output = "ZeroDivisionError: Cannot divide by 0"

        print(f"The result is \t {num1} {operation} {num2} = {output}")


        should_continue = input(f"Click 'c' to CONTINUE the calculation with previous output '{output}' or \nClick 'n' to START a new calculation or \nClick 'x' to EXIT : ").lower()

        if should_continue == "c":
            num1 = output
            
        elif should_continue == "n":
            continue_flag = False
            os.system('cls')
            calculation()

        else:
            continue_flag = False 
            print("Thanks for visiting")

calculation()