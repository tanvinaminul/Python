def factorial(number):
    if number==0:
        return 1
    else:
        return number * factorial(number-1)
print("Enter a number")
number= int(input())
print(number)
print(factorial(number))
