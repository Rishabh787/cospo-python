
'''  Control statement in python;

  1. Selection statement
      Selection statement are used to select the statements based on a condition.
  2. Looping statement
      looping statement are used to executte a single statemenet or a block of statement (Multiple statement)
      
      
      SELECTION STATEMENT 👇 ; if statement -

    Syntax:
    1st-
    if condition:
        Statement 1;
    
    2nd-
    if condition:
        Statement 1;
    else:
        Statement 2;

    3rd-
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

# from ast import While


# print("Use 👉(1) for addition(+)")
# print("Use 👉(2) for subtraction(-)")
# print("Use 👉(3) for multiplication(*)")
# print("Use 👉(4) for division(/)")

# opr = int(input("Enter the operator ✍: "))
# value_1 = int(input("Enter First Number ✍: "))
# value_2 = int(input("Enter Second Number ✍: "))

# if (opr == 1):
#     print("Addition of first and second number ✍: ", value_1 + value_2)
# elif (opr == 2):
#     print("Subtraction of first and second number ✍: ", value_1 - value_2)
# elif (opr == 3):
#     print("Multiplication of first and second number ✍: ", value_1 * value_2)
# elif (opr == 4):
#     print("Division of first and second number ✍: ", value_1 // value_2)



    #  LOOPING STATEMENT 👇 ; While loop-  , for loop-

'''
    Every looping statement have  3 condition-
    1. Initialization
    2. Condition
    3. Increment/Decrement


    Syntax-

    initialization
    condition
        statement
        increment/decrement
'''

# i = int(input("Enter a number: "))
i = 1
while (i<= 10):
    print(i)
    i = i+1