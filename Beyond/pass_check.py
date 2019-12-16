correct_password = ["aminul","islam"]
password = input("Enter password: ")
while password != correct_password:
    password = input("Wrong password! Enter again\n")

print("You logged in")
