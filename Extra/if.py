print("Enter a Character", end=" ")
character= input()

if character>='a' and character<='z' or character>='A' and character<='Z':
    if character in "aeiouAEIOU":
        print("It is a Vowel")
    else:
        print("It is a Consonent")

else:
    print("it is not a character")

