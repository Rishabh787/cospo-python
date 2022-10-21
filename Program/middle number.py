
#  Write a program to find positive and negative number? 
# 
# z = int(input("Enter number:"))
# if (z>0):
#     print("positive", z)
# elif (z<0):
#     print("negative")
# else:
#     print("zero")


#  Write a program to find middle number between three numbers?

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if (a>b and a<c):
    print(a)
elif (b>a and b<c):
    print(b)
elif (c>a and c<b):
    print(c)