# Part A
# 1
num = int(input("Enter a number to countdown from: "))
while num >= 0:
    print(num)
    num -= 1 



# 2
for number in range(2, 51, 2):  
    print(number, end="\t")  
    if number % 10 == 8: 
        print()


# Part B



# Part B
# 1
# using for loop
for number in range(1, 21):
    print(number)
number = 1
 # using while loop
while number <= 20:
    print(number)
    number += 1


# 2

number = 7
for multiply in range(1, 11):
    print(f"{number} x {multiply} = {number * multiply}")


# 3


correct_number = 7
attempts = 5
print("Try to guess a number between 1 and 10.")
while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess < correct_number:
        print("Too low!")
    elif guess > correct_number:
        print("Too high!")
    else:
        print("you are correct")
        break
    
    attempts -= 1

if attempts == 0:
    print("Failed. Correct number was 7.")


# 4
for i in range(1, 6):
    print("*" * i) 