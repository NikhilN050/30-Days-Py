# Task 1 – Print numbers 1 to 10
'''
for i in range(1,11):
    print(i)
'''
# Task 2 – Print even numbers (1–20)
'''
i = 1
while i <= 20:
    if i % 2 ==0:
        print(i)
    i+=1
'''
# Task 3 – Multiplication Table
"""
n = int(input("Enter a number :"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
"""
# Task 4 – Sum of Numbers (1 to n)
'''
n = int(input("Enter a numbe :"))
i = 1
sum = 0
while i <= n:
    sum +=i
    i += 1
print(sum)
'''
# Task 5 – Factorial using Loop
'''
n = int(input("Enter a numbe :"))
i = 1
fact = 1
while i <= n:
    fact *=i
    i += 1
print(fact)
'''
# Task 6 – Break Statement
"""
for i in range(1,11):
    if i == 5:
        break
    print(i)
"""
# Task 7 – Continue Statement
"""
for i in range(1,11):
    if i == 3:
        continue
    print(i)
"""
# Task 8 – Pattern Printing
'''
n = int(input("Enter a num :"))
for i in range(1,n+1):
    print("*"*i,end=" ")
    print(" ")
'''
# Task 9 – Add Two Numbers
'''
def total(a,b):
    add = a+b
    print(add)
a = 10
b = 20
total(a,b)
'''
# Task 10 – Prime Checker
"""
def prime(n):
    if n <= 1:
         return False
    for i in range(2,n):
         if n % i == 0:
              return False
    return True
print(prime(9))
"""
# Task 11 – Factorial Function
"""
def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)
factorial(3)
"""
# Task 12 – Default Arguments
"""
def greet(name="user"):
    if name == name:
        print(name)
    else:
        print("non")
    return greet
greet("nikhil")
"""
# Task 13 – Reverse String
"""
def reverse(s):
    return s[::-1]
print(reverse("python is best"))
"""
# Task 14 – Sum & Average of List
"""
def sum_avg (numbers):
    total = sum(numbers)
    avg = total/len(numbers)
    return total,avg

nums = [4, 10, 6, 8]
total,avg = sum_avg(nums)
print("sum",total)
print("average",avg)
"""
# Task 15 – Local vs Global
"""
x = 50 #global

def show():
    x = 100
    print("local ",x)

show()
print("global",x)
"""