class SimpleCalculator:
    # Consolidate operations into a dictionary of functions
    def operation(self, op, x, y):
        operations = {
            1: lambda x, y: x + y,  # Addition
            2: lambda x, y: x - y,  # Subtraction
            3: lambda x, y: x * y   # Multiplication
        }
        return operations.get(op, lambda x, y: "Invalid operation")(x, y)


def main():
    calculator = SimpleCalculator()

    while True:
        x = int(input("Enter a number for x: "))
        y = int(input("Enter a number for y: "))

        # Prompt user to select an operation
        op = int(input("Pick an operation to perform: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Off\n"))

        if op == 4:  # Exit if the user selects the "Off" option
            print("power off...")
            break

        # Call the operation method with the selected operation and numbers
        result = calculator.operation(op, x, y)
        print(f"Result: {result}")

if __name__ == '__main__':
    main()
