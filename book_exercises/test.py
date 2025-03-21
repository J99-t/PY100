"""
#1 Variables and Expressions
   Write code that calculates the area of a rectangle with length 7.5 and width 12.2, storing both dimensions and the result as variables."""

length = 7.5
width = 12.2
results = length * width
#print(results)

"""2. String manipulation
   Write a function that takes a person's first and last name as separate parameters and 
   returns a formatted greeting (e.g., "Hello, John Smith!")."""

def greeting(first,last):
    hello_name = (f"Hello, {first} {last}!")
    return hello_name

#print(greeting('John','Smith'))

"""3. Conditionals:
Write a function that takes a temperature value and a unit ('C' or 'F') and returns whether the temperature is freezing, 
based on water's freezing point in that unit."""
"""
def freezing_point(temp,unit):
    c_freezing = 0
    f_freezing = 32

    if unit == 'C':
        if temp <= c_freezing:
            print(f'Your celsius temperature is freezing')
        else:
            print(f'Your celsius temperature is not freezing')

    elif unit == 'F':
        if temp <= f_freezing:
            print(f'Your fahrenheit temperature is freezing')
        else:
            print(f'Your fahrenheit temperature is not freezing')

freezing_point(50,'C')
"""
"""Loops
Write a function that prints the first n numbers in the Fibonacci sequence."""


"""Lists:
Write a function that takes a list of numbers and returns the sum of all even numbers in the list.
"""
def total_even(numbers):
    total = 0
    for i in numbers:
        if i % 2 == 0:
            total += i
    return total

#print(total_even([1,2,3,4]))

"""
def total_even(numbers):
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return sum(new_list)
    """

"""
Dictionaries:
Create a function that takes a list of words and returns a dictionary 
where the keys are the words and the values are the number of times each word appears in the list.
"""

def convert_to_dict(words):
    my_dict = {}
    for word in words:
        if word not in my_dict:
            my_dict[word] = 1
        else:
            my_dict[word] += 1
    return my_dict

#print(convert_to_dict(['Hello', 'world', 'Goodbye', 'world']))

""" Function design
Write a function called is_palindrome that checks if a string reads the same forward and backward (ignoring spaces and case).
"""
def is_palindrome(string):
    for char in range(len(string)//2):
        if string[char] != string[(len(string) -1 - char)]:
            return False
    return True

#print(is_palindrome('racecar'))

"""Default parameters
Write a function that greets a user by name, with a default greeting of "Hello" if no specific greeting is provided."""

def greeting(greet='Hello'):
    name = input("What's your name?: ")
    return f'{greet} {name}'

#print(greeting('Salutations'))

"""Nested Collections
Given a list of dictionaries representing students (with 'name' and 'grades' keys, where grades is a list), 
write a function to find the student with the highest average grade."""

def find_highest_avg(students):
    highest_avg = 0
    best_student = ''
    for student in students:
        average = sum(student['grades']) / 4
        if average > highest_avg:
            highest_avg = average
            best_student = student['name']
    return best_student
            
students = [
    {'name': 'Emma', 'grades': [85, 90, 92, 88]},
    {'name': 'Michael', 'grades': [78, 82, 80, 75]},
    {'name': 'Sophia', 'grades': [95, 93, 91, 98]},
    {'name': 'James', 'grades': [88, 86, 90, 92]},
    {'name': 'Olivia', 'grades': [91, 89, 93, 87]}
]

#print(find_highest_avg(students))

"""
Write a function that safely converts a string to an integer, returning None if the conversion fails.
"""

test_inputs = [
    "42",           # Valid integer
    "-17",          # Valid negative integer
    "3.14",         # Not an integer (float)
    "hello",        # Not a number at all
    "123abc",       # Starts with digits but isn't fully an integer
    "",             # Empty string
    "9999999999999" # Very large number (may cause overflow in some languages)
]

"""
Write a function called format_phone_numbers that takes a list of phone numbers in various formats 
(e.g., "1234567890", "123-456-7890", "(123) 456-7890") and returns a dictionary where:
•   Keys are the original phone numbers
•   Values are formatted consistently as "(XXX) XXX-XXXX"
Your function should strip any non-digit characters from the input before formatting. 
If a number doesn't have exactly 10 digits after cleaning, mark it as "Invalid number" instead of formatting it.
"""

def format_phone_numbers(list_of_numbers):
    phone_dict = {}
    for elements in list_of_numbers:
        new_nums = ''
        for i in elements:
            if i.isdigit():
                new_nums += i
        if len(new_nums) == 10:
            phone_dict[elements] = f'({new_nums[0:3]}) {new_nums[3:6]}-{new_nums[6:10]}'
        else:
            phone_dict[elements] = 'Invalid number'
    return phone_dict

#print(format_phone_numbers(["1234567890", "123-456-7890", "(123) 456-7890", "12345", "123456789012"]))

# Example:
# Input: ["1234567890", "123-456-7890", "(123) 456-7890", "12345", "123456789012"]
# Output: {
#    "1234567890": "(123) 456-7890", 
#    "123-456-7890": "(123) 456-7890", 
#    "(123) 456-7890": "(123) 456-7890", 
#    "12345": "Invalid number", 
#    "123456789012": "Invalid number"
# }
"""
import copy
a = [[1,2,3], [4,5,6], 1]

#Creating a shallow copy of the nested list 'original'
b = copy.copy(a)

#Modifying an element in the shallow-copied list
b[0][0] = 99
b[2] = 10

#Printing the original and shallow-copied lists
print(a) #[[99,2,3], [4,5,6], 1]
print(b) #[[99,2,3], [4,5,6], 10]

a = [1, 2, 3]  
b = a  
a.append(4)
"""

# Write a function that uses the global keyword to modify a counter 
# variable that tracks how many times the function has been called.
counter = 0

def count_counter():
    global counter
    counter += 1

#Create a function create_counter() that returns another function. 
# The inner function should increment a counter variable each time it's called and return the current count. 
# Use the nonlocal keyword to make this work.

def create_counter():
    counter = 0
    def increment_counter():
        nonlocal counter
        counter += 1
        return counter
    return increment_counter

#Write a function that takes a number and adds it to a global list only if the number is even. 
# If the number is odd, it should print the current contents of the list.
"""
even = []

def take_num(lst_of_nums):
    global even
    for i in lst_of_nums:
        if i % 2 == 0:
            even.append(i)
        else:
            print(i)
"""
#Create a nested function structure with three levels: outer, middle, and inner. The outer function should define a variable. 
# The middle function should use nonlocal to modify that variable, and the inner function should print its value. 
# Demonstrate how the variable's value changes through this nested structure.

def outer_func():
    var = 0

    def mid_func():
        nonlocal var
        var += 1
        return var
    
    def inner_func():
        nonlocal var
        print(var)

    mid_func()

    inner_func()

#outer_func()

#Create a nested counter system with three levels of functions that uses both global and nonlocal statements to track different types of counts. 
# The outer function should maintain a global counter, 
# the middle function should maintain its own counter using nonlocal, 
# and the innermost function should increment both counters.
global_counter = 0 # defined a global variable

def outer_function():
    global global_counter

    def mid_func():
        middle_counter = 0

        def inner_function():
            nonlocal middle_counter
            global global_counter
            middle_counter += 1
            global_counter += 1
            print(f'Global counter: {global_counter}, Middle counter: {middle_counter}')
        return inner_function
    return mid_func()
    
#counter_func = outer_function()
#counter_func()  # Global counter: 1, Middle counter: 1
#counter_func()  # Global counter: 2, Middle counter: 2
#counter_func()  # Global counter: 3, Middle counter: 3
#print(f"Function was called {global_counter} times globally")

"""
output
Global counter: 1, Middle counter: 1
Global counter: 2, Middle counter: 2
Global counter: 3, Middle counter: 3
Function was called 3 times globally
"""

#Write a function create_account() that creates a bank account with methods to deposit, withdraw, and check the balance. Use nonlocal to maintain the account balance. 
# Include validation that prevents withdrawals exceeding the balance. The function should also track all transactions globally.
transaction_hist = []

def create_account():
    account_balance = 0

    def deposit(amount):
        nonlocal account_balance
        account_balance += amount
        transaction_hist.append('deposit,' + str(amount))

    def withdraw(amount):
        nonlocal account_balance
        account_balance -= amount
        if amount > account_balance:
            print(f'Insufficient funds. Balance: {account_balance}')
        else:
            transaction_hist.append('withdraw' + str(amount))

    def check_balance():
        nonlocal account_balance
        return account_balance
    
    def transaction_history():
        return transaction_hist
    
    return deposit, withdraw, check_balance, transaction_history

deposit, withdraw, check_balance, transaction_history = create_account()
deposit(500)

#print(check_balance())
#print(transaction_history())
"""
Balance: 500
Balance: 800
Insufficient funds. Balance: 800
Balance: 650
Transaction history: [('deposit', 500), ('deposit', 300), ('withdraw', 150)]
"""

#Write a function that takes a string and returns a new string with all vowels removed.

def remove_vowels(word):
    vowels = ('a','e','i','o','u')
    new_word = ''
    for letter in word:
        if letter not in vowels:
            new_word += letter
    return new_word

#print(remove_vowels("hello world")) #should return "hll wrld"

#Create a function that calculates the sum of all even numbers in a list.
def sum_even_numbers(lst):
    new_list = []
    for number in lst:
        if number % 2 == 0:
            new_list.append(number)
    return sum(new_list)

#print(sum_even_numbers([1, 2, 3, 4, 5, 6])) #should return 12 (2 + 4 + 6)

#Create a function that takes a dictionary with string keys and integer values, and returns a new dictionary where the keys 
# with even values are kept and keys with odd values are removed.
"""
def filter_even_values(dict):
    new_dict = {}
    for key,value in dict.items():
        if value % 2 == 0:
            new_dict[key] = value
    return new_dict
"""
def filter_even_values(dict):
    new_dict = {key: value for key, value in dict.items() if value % 2 == 0}
    return new_dict

#print(filter_even_values({"a": 1, "b": 2, "c": 3, "d": 4})) #should return {"b": 2, "d": 4}

#Write a function that takes a string and returns it with the first and last characters swapped.
def swap_first_last(word):
    if len(word) < 2:
        print(word)
    else:
        new_word = word[-1] + word[1:-1] + word[0]
        print(new_word)

swap_first_last("Python") #should return "nythoP"
swap_first_last("a") #should return "a"

#Create a function that takes a list of numbers and returns a new list containing only the numbers that are divisible by 3.

def divisible_by_three(lst):
    new_list = []
    for number in lst:
        if number % 3 == 0:
            new_list.append(number)
    return new_list

#print(divisible_by_three([1, 2, 3, 4, 5, 6, 9, 10])) #should return [3, 6, 9]

#Write a program that generates a dictionary where the keys are numbers from 1 to 10 and the values are the squares of the keys.
