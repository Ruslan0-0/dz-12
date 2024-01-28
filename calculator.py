class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, num1, num2):
        if self.strategy is None:
            return ValueError("No strategy set")
        return self.strategy.execute(num1, num2)


class Addition:
    def execute(self, num1, num2):
        return num1 + num2


class Subtraction:
    def execute(self, num1, num2):
        return num1 - num2


class Multiplication:
    def execute(self, num1, num2):
        return num1 * num2


class Division:
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2


calculator = Calculator()
calculator.set_strategy(Addition())
result = calculator.calculate(5, 2)
print(result)
