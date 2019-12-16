def gcd(a, b):
    if b>a:
        gcd(b,a)
    while b!=0:
        temp= a%b
        a=b
        b= temp
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

print("Please Enter Two Integers:")
a,b= map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))
