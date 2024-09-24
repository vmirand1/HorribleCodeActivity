class AdditionCalculator:
    def addition(self, x: int, y: int):
        sum_of_the_two_values = x + y  # Perform addition and store the result
        return sum_of_the_two_values  # Return sum

class SubtractionCalculator:
    def subtraction(self, x: int, y: int):
        result_that_is_subtraction_method = x - y  # Perform subtraction and store the result
        return result_that_is_subtraction_method  # Return subtraction result

class MultiplicationCalculator:
    def multiplication(self, x: int, y: int):
        m = x * y  # Perform multiplication and store the result
        return m  # Return multiplication result

class OperationsChoice:
    def __init__(self):
        self.addition_calc = AdditionCalculator()
        self.subtraction_calc = SubtractionCalculator()
        self.multiplication_calc = MultiplicationCalculator()

    def operation(self, op, x, y):
        result = 0
        if op == 1:
            result = self.addition_calc.addition(x, y)  # Call addition method
        elif op == 2:
            result = self.subtraction_calc.subtraction(x, y)  # Call subtraction method
        elif op == 3:
            result = self.multiplication_calc.multiplication(x, y)  # Call multiplication method
        else:
            result = "Invalid operation"  # Handle invalid operation
        return result


class ViolationSimpleCalculator:
    def __init__(self):
        self.operation_handler = OperationsChoice()

    def operation(self, op, x, y):
        return self.operation_handler.operation(op, x, y)


def main():
    calculator = ViolationSimpleCalculator()  # Instantiate the ViolationSimpleCalculator object

    while True:
        x = int(input("Enter a number for x: "))  # Convert input to integer
        y = int(input("Enter a number for y: "))  # Convert input to integer

        op = int(input("Pick an operation to perform: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Off\n"))

        if op == 4:  # Check if the user has chosen to exit
            print("power off...")  # Inform the user that the program is shutting down
            break  # Exit the loop

        result = calculator.operation(op, x, y)  # Store the result of the operation
        print(f"Result: {result}")  # Output the result

        print("This loop will run again unless you choose to exit by pressing 4.")

# If the script is being run directly, start the main function
if __name__ == '__main__':
    main()




