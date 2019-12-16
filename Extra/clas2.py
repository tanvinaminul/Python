class Calculator(object):
    """docstring for Calculator"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a/self.b
        except:
            raise ZeroDivisionError("Can't Devide By Zero.")

print("Enter Two Number with space In Between Them.")
a,b = map(int, input().split())

my_calculator = Calculator(a, b)

temp = my_calculator.addition()
print(temp)

temp = my_calculator.subtraction()
print(temp)

temp = my_calculator.multiplication()
print(temp)

temp = my_calculator.division()
print(temp)
