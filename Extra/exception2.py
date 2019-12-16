try:
   with open("test.txt",'r') as my_file:
        content= my_file.read()
        print(content)
except FileNotFoundError:
    print("The File Does Not Exist.")

finally:
    print("To be or not to be that is the question")
