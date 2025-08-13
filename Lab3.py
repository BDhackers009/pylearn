# Lab3.py
#Task 1
print("Hello")

# Task 2

name = input("Enter Your Name: ")

print(f"Welcome, {name}")


# Task 3
nameandage = input("Enter your name and age: ")

name, age = nameandage.split()

print(f"Welcome, {name}")
print(f"You are {age} years old")

#Part B

# Task 1

number = int(input("Enter a number: "))
print("The number is: ", number)

# Task 2
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
domath = n1 + n2
print("The sum is:", domath)


# Task 3
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
add = n1 + n2
subtract = n1 - n2
multiply = n1 * n2
divide = n1 / n2
mod = n1 % n2
print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)
print("Mod:", mod)


#Task 4
char1 = input("Enter first character: ")
char2 = input("Enter second character: ")
char3 = input("Enter third character: ")
welcome_message = f"Hello {char1}{char2}{char3}! We hope you have a nice day"
print(welcome_message)


# Task 5

val1 = "Python"
val2 = 10
val3 = 98.10
print("String:", val1)
print("Integer:", val2)
print("Float:", val3)


# Task 6
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
temp = num1
num1 = num2
num2 = temp
print("Swapped num1 =", num1, "num2 =", num2)

# Task 7

sub1 = float(input("Enter Mark1: "))
sub2 = float(input("Enter Makr2: "))
sub3 = float(input("Enter Mark3: "))
sub4 = float(input("Enter Mark4: "))
sub5 = float(input("Enter Mark5: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
avg_percentage = total / 5
print("Total marks:", total)
print("Percentage:", avg_percentage, "%")

# Task 8


basic_salary = float(input("Enter the Basic salary: "))
grade_pay = 2 * basic_salary
da = 0.70 * basic_salary
ta = 200
hra = 0.20 * basic_salary
total_salary = grade_pay + da + ta + hra
print("Grade Pay:", grade_pay)
print("Dearness Allowance (DA):", da)
print("Travel Allowance (TA):", ta)
print("House Rent Allowance (HRA):", hra)
print("Total Salary:", total_salary)