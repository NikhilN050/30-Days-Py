# Task 1 – String Basics
"""
user = input("Enter your name:")
user1 = input("Enter a name:")
up = user.upper()
tit = user.title()
low = user.lower()
print(up)
print(tit)
print(low)
"""
# Task 2 – String Slicing
"""
user = input("Enter a number : ")
print(user[:3])
print(user[-3:])
print(user[::-1])
"""
# Task 3 – Count Vowels
"""
text = input("Enter a word :")
count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count +=1
print(count)
"""
