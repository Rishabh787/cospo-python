'''  Control statement in python;

  1. Selection statement
      Selection statement are used to select the statements based on a condition.
  2. Looping statement
      looping statement are used to executte a single statemenet or a block of statement (Multiple statement)
      
      
      SELECTION STATEMENT ; if statement -

    Syntax:
    if condition:
        Statement 1;
    
    2nd-
    if condition:
        Statement 1;
    else:
        Statement 2;

    3re-
    if condition:
        Statement 1;
    elif condition:
        Statement 2;
    else: 
        Statement 3;
        
      '''

# a = int(input("Enter a number: "))
# if a%2==0:
#     print(a, "is a even number")
# else:
#     print(a, "is a odd number")
print("USe 1 for Addition (+)")
print("USe 2 for Addition (-)")
print("USe 3 for Addition (*)")
print("USe 4 for Addition (/)")

opr = int(input("Enter the operation: "))
val1 = int(input("Enter a number: "))
val2 = int(input("Enter a number: "))
if (opr == 1):
    print(val1+val2)
elif opr == 2:
    print(val1-val2)
elif opr == 3:
    print(val1*val2)
elif opr == 4:
    print(val1//val2)
else:
    print("Invalid operation")
