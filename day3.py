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
