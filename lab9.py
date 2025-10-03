#!/usr/bin/env python3

#Part D Task 1

abc = (2, 4, 5) # tuple unpacking
a, b, c = abc # assigning each value to a variable
print(a + b + c) # displaying the total

''' Output:
11
''' 

# Task 2
#part a
tuple1 = (1, "Hello")
tuple1 = tuple1 + (5,) # , is necessary to indicate it's a single element tuple and '+' not an arithmetic operation
print(tuple1)

''' Output:
(1, 'Hello', 5)
'''

#part b
#tuple1 = (1, "Hello")
#tuple1.append(5) # tuples are immutable, so they don't have an append method

''' Output:
AttributeError: 'tuple' object has no attribute 'append'
'''
#task 3
your_str = ('m', 'u', 's', 't', 'a', 'k', 'i', 'm')
join_str = "".join(your_str) # joining the characters in the tuple to form a string
print(join_str)
''' Output:
mustakim
'''
#task 4
my_list = [1, 2, 3, 4]
tup1 = tuple(my_list) # converting list to tuple
print(tup1)

''' Output:
(1, 2, 3, 4)
'''

# Task 5

t1 = (1, 2, 3, 4)
print(1 in t1)
print(100 in t1)

''' Output:
True
False
'''
# Task 6
tuple2 = (23, 45, 65, 78, 98, 9, 45, 56, 43)
print(tuple2[::-1]) # reversing the tuple using slicing 

''' Output:
(43, 56, 45, 9, 98, 78, 65, 45, 23)
'''

# Task 7

set1 = {1, 2, "Hello", "Python"} # given set
for i in set1:# iterating through the set
    print(i)
''' Output:
1
2
Hello
Python
'''


# Task 8

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
print(setA - setB) # difference between setA and setB
''' Output:
{1, 2}
'''

# Task 9
my_string = str(input("Enter a string: "))
set22 = set(my_string) # converting string to set
clist = list(set22) # converting set to list
tuple4 = tuple(set22) # converting set to tuple
print(set22, clist, tuple4)

''' Output: based on user input
Enter a string: hello
{'h', 'e', 'l', 'o'}
['h', 'e', 'l', 'o']
('h', 'e', 'l', 'o')
'''

# task 10
my_string = "Programming with Python"
vowels = {'a','e','i','o','u'}
count = 0
for sc in my_string.lower():   # using .lower() to avoid case sensitivity
    if sc in vowels:
        count += 1 # counting the vowels

print(count)

''' Output:
5
'''

# task 11
my_dict = {"name": "Amira", "age": 35}
my_dict["state"] = "Kedah" # adding a new kay and its value to the dictionary.
print(my_dict)

''' Output:
{'name': 'Amira', 'age': 35, 'state': 'Kedah'}
'''

# task 12
my_dict = {"name": "Amira", "age": 35}
my_dict["state"] = "Kedah" # adding a new kay and its value to the dictionary.
print(my_dict)
for key, value in my_dict.items():
    print(key, ":", value)

''' Output:
name : Amira
age : 35
state : Kedah
'''
# task 13
num = {145, 100, 65, 79}
print(sum(num)) # sum of all elements in the set

# task 14
myData = {1: "hello", 2: 22, 3: 33}
keys = [1, 2, 4]
for key in keys: # using for loop to check each key in the list
    if key in myData:
        print(f"{key} is present")
    else:
        print(f"{key} is missing")