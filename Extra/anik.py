Numbers= set()
while True:
    Anik =int(input())
    if Anik== -1:
        break
    Numbers.add(Anik)

Numbers = list(Numbers)
Numbers.sort(reverse=True)
print(Numbers)
