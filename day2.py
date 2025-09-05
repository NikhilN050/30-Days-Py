# Task 1 Arithmetic Practice
'''
a = int(input("Enter any number :"))
b = int(input("Enter any number :"))

sum = a + b
print(sum)
diff = a - b
print(diff)
product = a * b
print(product)
division = a / b
print(division)
floor_division = a // b
print(floor_division)
modulus = a % b
print(modulus)
power = a ** b
print(power)
'''

# Task 2 Comparison Operators
'''
a=10
b=20

print(a == b)
print(a > b)
print(a < b)
'''

# Task 3 Logical Operators
'''
user = int(input("Enter your age :"))

if (user>=18 and user<=60):
    print("True")
else:
    print("False")
'''   

# Task 4 Type Casting
'''
a = "123"
print(int(a)+10)
b = "12.5"
print(float(b)*2)
c = 90
print(type(f"your score is {c}"))
'''

# Task 5 Even or Odd Checker
"""
num = int(input("Enter a number here :"))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
"""

# Task 6 Maximum of Two Numbers
'''
a = int(input("Enter any number : "))
b = int(input("Enter any number : "))
if a > b :
    print("a is grater")
else :
    print("b is grater")
'''

# Task 7 Positive, Negative, or Zero
"""
num = int(input("Enter any number with :"))

if num > 0:
    print("Positive")
elif num < 0:
    print("Nagative")
else:
    print("zero")
"""

# Task 8 Simple Calculator
'''
a = float(input("Enter first num :"))
b = float(input("Enter second num :"))
op = input("Enter a operator (+,-,*,/) : ")

if op == "+":
    print("result " , a + b)
elif op == "-":
    print("result ",a-b)
elif op == "*":
    print("result ",a*b)
elif op == "/":
    if b != 0:
        print("result ",a/b)
    else:
        print("Error : Division by zero")
else:
    print("Invalid operator")
'''

# Task 9 Age Category
'''
age = int(input("Enter your age :"))

if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult") 
else:
    print("senior")   
'''

# Task 10 Number Conversion
'''
num = int(input("Enter a decimal number: "))

print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
'''

#  Task 11 Absolute Difference
"""
a = int(input("Enter a num :"))
b = int(input("Enter a num :"))

diff = abs(a-b)
print("your absulate diff is ",diff)
"""