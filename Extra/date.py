from datetime import datetime
now = datetime.now()

year= int(input("Enter your birth year: "))
month= int(input("Enter your birth month: "))
date= int(input("Enter your birth date: "))
hour= int(input("Enter your birth hour: "))
minute= int(input("Enter your birth minute: "))
print("\n")

birth = datetime(year, month, date, hour, minute,)
age = now- birth
print("Your age is: ", age)
