# Part A
# Task 1
n1 = int(input("Enter a number: "))

if n1 % 2 == 0:
    print(f"{n1} is Even.")
else:
    print(f"{n1} is Odd.")


# Task 2

score = int(input("Type your total score: "))

if score < 50:
    print("You FAILED MAN!")
else:
    print("You PASSED")



# Task 3

x = float(input("Number 1: "))
y = float(input("Number 2: "))
z = float(input("Number 3: "))
largest = x

if y > largest:
    largest = y
if z > largest:
    largest = z

print(f"Largest number is {largest}")

# Task 4

selling_price = float(input("Enter selling price: "))
buying_price = float(input("Enter buying price: "))

if selling_price > buying_price:
    print("PROFIT")
elif selling_price < buying_price:
    print("LOSS")
else:
    print("NO PROFIT NO LOSS")


#Part B

# Task 1
while True:
    print("\n--- PRO CALC ---")
    print("1. Calculate area of a rectangle")
    print("2. Find smallest of three numbers")
    print("3. Find the sum of two numbers")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        l = float(input("Enter length of rectangle: "))
        w = float(input("Enter width of rectangle: "))
        ar = l * w
        print(f"Area of rectangle: {ar}")

    elif choice == '2':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        z = float(input("Enter third number: "))
        s = x
        if y < s:
            s = y
        if z < s:
            s = z
        print(f"Smallest number is: {s}")

    elif choice == '3':
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        total = x + y
        print(f"Sum is: {total}")

    elif choice == '4':
        print("Exiting the program.")
        break # I used exit() before but it was causing issues

    else:
        print("Try Again.")



# Task 2
x = int(input("Enter a year: "))

if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0): # Formula is from chatgpt
    print(f"{x} is a leap year.")
else:
    print(f"{x} is not a leap year.")



# Task 3

marital_status = input("married or unmarried? : ")
gender = input("male or female? : ")
age = int(input("Enter age: "))

if marital_status == "married":
    print("Driver is insured.")
elif marital_status == "unmarried":
    if gender == "male" and age > 30:
        print("Driver is insured.")
    elif gender == "female" and age > 25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")
else:
    print("Invalid input.")