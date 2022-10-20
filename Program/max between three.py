#  Write a program to find max number between three numbers?

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if (a>b and a>c):
    print("max number:", a)
elif (b>c and b>a):
    print("max number:", b)
else:
    print("max number:", c)
