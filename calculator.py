def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    while True:
        print("\nChoose operation: add, subtract, multiply, divide, or exit")
        choice = input("Operation: ").strip().lower()

        if choice == "exit":
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "add":
            print("Result:", add(num1, num2))
        elif choice == "subtract":
            print("Result:", subtract(num1, num2))
        elif choice == "multiply":
            print("Result:", multiply(num1, num2))
        elif choice == "divide":
            print("Result:", divide(num1, num2))
        else:
            print("Unknown operation.")

if __name__ == "__main__":
    main()
