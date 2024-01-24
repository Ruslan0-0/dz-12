from abc import ABC, abstractmethod
def fibonachi():
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = int(input(" = "))

for num in fibonachi():
    print(num)


def cycl():
    numbers = [1, 2, 3]
    i = 0
    while i < n:
        yield numbers [i % len(numbers)]
        i += 1

n = int(input(" = "))

for num in cycl():
    print(num)


class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza: size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, size):
        return self.builder \
            .set_size(size) \
            .add_cheese() \
            .add_pepperoni() \
            .add_mushrooms() \
            .add_onions() \
            .add_bacon() \
            .build()


builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza(size="Large")

print(pizza)


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return ("Meow")

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid")

factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())


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


