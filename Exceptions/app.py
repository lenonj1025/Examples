from operation_error import OperationError

print("Welcome to the calculator app: ")
allows_operations = {'+', '-', '*', '/'}
while True:
    try:
        print("Enter the operation that you would like to perform (+, -, *, /): ")
        choice = input()
        if choice not in allows_operations:  # 0(1) because we are using a set
            raise OperationError("You must enter a valid operation (+, -, *, /")

        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())

        if choice == '+':
            print("The result " + str(num1 + num2))
        elif choice == '-':
            print("The result " + str(num1 - num2))
        elif choice == '*':
            print("The result " + str(num1 * num2))
        elif choice == '/':
            print("The result " + str(num1 / num2))

    except ValueError as e:
        print("Please enter a valid number!")
    except OperationError as e:
        print(e)

    print("Enter (y or Y) if you would like to continue, otherwise the program will end")
    exit_choice = input()
    if not (exit_choice == 'y' or exit_choice == 'Y'):
        break
