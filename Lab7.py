#!/usr/bin/python3
# Part A
# Task 1
my_list = [1.6, 2.7, 3.8, 4.9]
new_list = []
a_list = []

for val in my_list:
    temp = str(val)
    a_list.append(temp.split('.'))

for val in a_list:
    new_list.append(int(val[0]))
my_str = ':'.join(val)

print(my_list)
print(a_list)
print(new_list)
print(val)
print(my_str)

''' Output:
[1.6, 2.7, 3.8, 4.9]
[['1', '6'], ['2', '7'], ['3', '8'], ['4', '9']]
[1, 2, 3, 4]
['4', '9']
4:9
'''

# Task 2
family = ['hi', 'mom', 'father', ['halmeoni', 'grandpa']]
alias_family = family              
copy_family = family.copy() # Making a shallow copy

alias_family[0] = 'bye'
alias_family[1] = 'mother'
alias_family[2] = 'dad'

print(family)
print(alias_family)
print(copy_family) # only this remains unchanged because it is a shallow copy.

'''Output:
['bye', 'mother', 'dad', ['halmeoni', 'grandpa']]
['bye', 'mother', 'dad', ['halmeoni', 'grandpa']]
['hi', 'mom', 'father', ['halmeoni', 'grandpa']]
'''


numList = [1, 3, 5, 5, 2, 10]
numList.append(4) # inserting 4 at the end of the list

numList.sort() # sorting the original list

unique = []
for n in numList:
    if n not in unique:
        unique.append(n) # removing duplicates


for i, n in enumerate(unique): # inserting 6 before the first number greater than 6
    if n > 6:
        unique.insert(i, 6)
        break
else:
    unique.append(6) # if 6 is the largest number, append it to the end


print(numList)
print(unique)
''' Output:
[1, 2, 3, 4, 5, 5, 10]
[1, 2, 3, 4, 5, 6, 10]
'''
# Part B
# Task 1
valid_numbers = []

while True: # using True so that user can enter numbers until they decide to stop
    s = input("Enter a number (or 'stop'): ").strip().lower() # taking input and normalizing it. using .lower() to avoid case sensitivity.
    if s == 'stop': # using this method to exit the loop
        break
    try:
        n = int(s)
        if 0 <= n <= 100:
            valid_numbers.append(n)
        else: # checking if the number is in range
            print("Out of range, not added.")
    except ValueError:
        print("Not a number, try again.")

if valid_numbers:
    total = sum(valid_numbers)
    avg = total / len(valid_numbers)
    product = 1 
    for x in valid_numbers:
        product *= x
    print("Sum:", total)
    print("Average:", avg)
    print("Product:", product)
else:
    print("No valid numbers entered.")

# Task 2

import random
food = ["cookies", "brownies", "cake", "ice cream", "chocolate"]
random.shuffle(food)
print(food) 

'''Output:
['cake', 'cookies', 'brownies', 'chocolate', 'ice cream']
'''
# Task 3
 
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7]

diff = []
for x in list_a:
    if x not in list_b:
        diff.append(x) # append elements in list_a that are not in list_b
for x in list_b:
    if x not in list_a:
        diff.append(x) # append elements in list_b that are not in list_a

print("Difference:", diff) 

''' Output:
Difference: [1, 2, 3, 6, 7]
'''


# Task 4

chars = ['H', 'e', 'l', 'l', 'o']
s1 = "".join(chars)
print(s1)


# Output: Hello

# Task 5
orders = ["Burger", "Pizza", "Salad", "Pasta", "Soup", "Steak"]

print(orders[0])
print(orders[-1])        # to print the last item
print(orders[2:5])  # ['Salad','Pasta','Soup']

orders[1] = "Sushi" # replacing Pizza with Sushi
print(orders) 

''' Output:
['Burger', 'Sushi', 'Salad', 'Pasta', 'Soup', 'Steak']
'''


