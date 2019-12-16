class Calculator:
    """docstring for Calculator"""
    def addition(self, a, b):
        return a+b

    def subtraction(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Division By Zero Is Not Possible.")

my_calculator= Calculator()
print("Enter 2 Number And Give Space In Between Them.")
a, b= map(int, input().split())

temp = my_calculator.addition(a,b)
print(temp)

temp = my_calculator.subtraction(a,b)
print(temp)

temp = my_calculator.subtraction(a,b)
print(temp)

temp = my_calculator.division(a,b)
print(temp)
