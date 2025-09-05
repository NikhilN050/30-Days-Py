# Task 1
print("Nagar Nikhil")
print(20)
print("coding")
# Task 2

a = 10
b = 5.5
c = "python"
print(type(a))
print(type(b))
print(type(c))

# Task 3

x = 5
y = 2
print("before swapping: x",x,"y",y)
x, y = y, x
print("after swapping: x", x,"y:", y)

# Task 4

Name = str(input("Enter your name: "))
Age = int(input("Enter your age: "))
print(f"hello {Name}, you are {Age} years old")

# Task 5

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print("The sum Of",num1,"and",num2,"is",sum)
diff = num1 - num2
print("The difference Of",num1,"and",num2,"is",diff)
prod = num1 * num2
print("The product Of",num1,"and",num2,"is",prod)
div = num1 / num2
print("The division Of",num1,"and",num2,"is",div)
remi = num1 % num2
print("The remainder Of",num1,"and",num2,"is",remi)

# Task 6

no = int(input("Enter a number: "))
no1 = int(input("Enter another number: "))
no3 = int(input("Enter one more number: "))
avg = (no + no1 + no3)/3
print(f"The avrage is {avg}")


# Task 7

x = 10
y = 20
z = 30
print("Before swapping: x =",x,"y =",y,"z =",z)
x, y, z = y, z, x 
print("After swapping: x =",x,"y =",y,"z =",z)

# Task 8

user = int(input("Enter the number of celsius: "))
fahrenheit = (user * 9/5) + 32
print(fahrenheit)

# Task 9
 
P = int(input("Principle :"))
R = int(input("Rate :"))
T = int(input("Time :"))
interest = (P * R * T) / 100
print(interest)

# Task 10
user = int(input("give me a number for sqr:"))
user1 = int(input("give me a number for cube:"))
sqr = user ** 2
cube = user ** 3
print("Square:", sqr)
print("Cube:", cube)

# Task 11

user = input("Enter somthing : ")

try :
    val = int(user)
    print("This is an integer number")
except ValueError :
    try:
        val = float(user)
        print("This is a float number")
    except ValueError:
        print("This is a string")
