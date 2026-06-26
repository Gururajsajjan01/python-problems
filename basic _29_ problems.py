# hello world
print("hello world")

# print your name
name = "Gururaj"
print(name)

#take your name as input and print a welcome message
name = int(input("ente the name"))
print("welcome",name)

# add two numbers
a = int(input("enter the number"))
b = int(input("enter the number"))
print("sum",a+b)

# subtract two number
a = int(input("enter the first number"))
b = int(input("enter the second number"))
print("subtrack",a - b)

# mutiple two number
a = int(input("enter the number"))
b = int(input("enter the number"))
print("mutiple",a * b)

# divide two number
a = int(input("enter the number"))
b = int(input("enter the number"))
print("div",a/b)

# find the remainder
a = input("enter the number")
b = input("enter the number")
print("remainder",a % b)
 
# find the square of a number
a = int(input("enter the number"))
b = int(input("enter the number"))
print("square", a ** b)

# find the cube od a number
n = input("enter the number")
print(n ** 3)

# swap two numbers using a thrid variable
a = int(input())
b = int(input())

temp = a 
a = b
b = temp

print(a,b)

# swap two number without thrid variable
a = int(input())
b = int(input())

a,b = b,a
print(a,b)

# calculate the area of a recatangle
length = int(input())
width = int(input())

rectangle= length * width

print(rectangle)

# calculate the area of a circle

r = float(input())
print(3.14 * r * r)

# find the average of three number
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
num3 = int(input("enter the number"))

average = num1+num2+num3/3
print(average)

# convert celsius to fahrenheit

c = int(input("enter the celsius"))
print(c * 9/5 + 32)

# find the simple interest
p = float(input())
r = float(input())
t = float(input())

print((p * r * t) / 100)

# calculate the perimeter of a rectangle 
l = float(input())
w = float(input())

print(2 * (l + w))

#Find the total and percentage of 5 subjects.
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total =", total)
print("Percentage =", percentage)