class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def mines(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 - self.number2

output = Calculator(5, 5)

output_sum = output.sum()
output_mines = output.mines()
output_multiply = output.multiply()
output_divide = output.divide()

print("sum:", output_sum)
print("mines:", output_mines)
print("Multiplication:", output_multiply)
print("Division:", output_divide)

