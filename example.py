class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "nemitavanad 0 bashad"
        return x / y

calculator = Calculator()

result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 4)
result_multiply = calculator.multiply(6, 7)
result_divide = calculator.divide(8, 2)

print("sum:", result_add)
print("sub:", result_subtract)
print("multi:", result_multiply)
print("div:", result_divide)


