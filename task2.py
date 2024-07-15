def display_menu():
    print("\nSimple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

def get_numbers():
    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def perform_operation(choice, num1, num2):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation choice."

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1/2/3/4) or 'q' to quit: ")
        if choice.lower() == 'q':
            print("Exiting the Simple Calculator. Goodbye!")
            break
        num1, num2 = get_numbers()
        result = perform_operation(choice, num1, num2)
        print(f"\nThe result is: {result}")
main()
