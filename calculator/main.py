#make a calculator by using a class

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b == 0:
            return "Error: Cannot divide by zero"
        return self.a / self.b

    def power(self):
        return self.a ** self.b

    def modulus(self):
        return self.a % self.b


    def square_root(self):
        if self.a < 0:
            return "Error: Cannot calculate square root of negative number"
        return self.a ** 0.5
    
    def factorial(self):
        if self.a < 0:
            return "Error: Cannot calculate factorial of negative number"
        if self.a == 0:
            return 1
        result = 1
        for i in range(1, int(self.a) + 1):
            result *= i
        return result

    def log(self):
        from math import log
        if self.a <= 0:
            return "Error: Cannot calculate logarithm of non-positive number"
        return log(self.a, self.b)

    def sin(self):
        from math import sin
        return sin(self.a)

    def cos(self):
        from math import cos
        return cos(self.a)

    def tan(self):
        from math import tan
        return tan(self.a)
