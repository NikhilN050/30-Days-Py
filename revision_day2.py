# Task 1
"""
user = int(input("Enter a number :"))
if user > 0:
    print("positive")
elif user < 0:
    print("negative")
else :
    print("zero")
"""
# Task 2 
"""
user = int(input("Enter a number: "))
user1 = int(input("Enter a number:"))
if user > user1 :
    print(f"max is {user}")
elif user1 > user:
    print(f"max is {user1}")
"""
# Task 3
"""
user = int(input("Enter a number: "))
user1 = int(input("Enter a number:"))
user2 = int(input("Enter a number:"))
if user < user1 < user2:
    print(f"min is {user}")
elif user1 < user < user2:
    print(f"min is {user1}")
elif user2 < user < user1 :
    print(f"min is {user2}")
"""
# Task 4
'''
user = int(input("Enter a number check is divisable or not: "))

if user // 5 :
    print("yes")
else:
    print("not")
'''
# Task 5
"""
user = int(input("Enter a number check is divisable or not: "))

if user % 2 ==0:
    print("it's even")
else:
    print("it's odd")
"""
# Task 6
"""
user = int(input("Enter a number check is divisable or not: "))

if user > 10 and user % 2 ==0:
    print("good")
else:
    print("it's not")
"""
# Task 7 
"""
I1 = int(input("Enter a numer :"))
I2 = int(input("Enter a numer :"))
op = input("Enter a oprator (+,-,*,/):")

if op == "+":
    print(I1+I2)
elif op == "-":
    print(I1-I2)
elif op == "*":
    print(I1*I2)
elif op == "/":
    if I2 != 0:
        print(I1/I2)
    else:
        print("zero error")
else:
    print("invalid error")
"""
# Task 8
"""
user = int(input("Enter age :"))

if user < 13 :
    print("child")
elif user > 13 and user <19:
    print("teen")
elif user > 20 and user <59:
    print("adult")
elif user > 60:
    print("senior")
else:
    print("don't be oversmart")
"""
# Task 9 
"""
num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))

diff = abs(num1-num2)
print(diff)
"""