"""
interest = .05
balance = 1000.00
for i in range(0,5):
    balance += balance * interest
    print(f'After {i} years you will have {balance}')



balance = 1000.00 #8
# print(balance * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)


balance *= 1.05 #9
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)


obj = 'ABcd' #reassigns the variable
obj.upper() #does neither
obj = obj.lower() #mutates the variable | reassign
print(len(obj)) #does neither
obj = list(obj) #reassigns the variable
obj.pop() #mutates the variable
obj[2] = 'X' #mutates the variable
obj.sort() #mutates the variable
set(obj) #reassigns the variable | neither
obj = tuple(obj) #reassigns the variable

"""

# Functions and methods challenges
"""
def multiply(a,b): #3
    product = a*b
    return product

a = (float(input("Enter the first number: ")))
b = (float(input("Enter the second number: ")))
print(f'{a} * {b} = {multiply(a,b)}')
"""

#function definition
# multiply_numbers num1 num2 num3 result product

#6 returns nothing since return terminates the function before it prints

#7 missing positional argument
#8 too many positional arguments

#14 multiply left right get_num prompt float input first_number second_number product print

#15
#global:first_num second_num product multiply get_num
#local: left right prompt
#built-in: print float input

#16
# multiply 1 9
# get_num 4 7 8 
# left right 1 2
# prompt 4 5

# incorrect forgot float input and print as function names

#17
# function names: say 
# method names: upper lower
# built-in functions: print input max
"""
#18
def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []
print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))
"""
"""
def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))
"""

#Flow Control
""""
# 1.
False
True
True #3
True #3
False
True
False
False
True #False
True
"""

#2.
"""
def even_or_odd(num):
    if (num % 2 == 0):
        print('even')
    else:
        print('odd')

def even_odd(num):
    print('even' if num % 2 == 0 else 'odd')
"""

#3
# Product2 & Product not found!

#4
"""
if foo():
    return 'bar'
else:
    return qux()
"""

#5 The code outputs 'Empty' since the empty set is evaluated as falsy

#6
"""
def upper_case(str):
    if len(str) > 10: #use len
        print(str.upper())
    else:
        print(str)

upper_case('hello world')
upper_case('goodbye')
"""
"""
#7
def number_range(value):
    if (value <= 50 and value >= 0):
        print(value ,'is between 0 and 50 (inclusive)')
    elif (value >= 50 and value <= 100):
        print(value ,'is between 51 and 100 (inclusive)')
    elif (value > 100):
        print(value ,'is greater than 100')
    else:
        print(value ,'is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
"""

# Intro to collections

#1. len(people)
"""
#2 You can't change the value of bye because tuples are immutable
# however you can make a new tuple and reassign it
stuff = ('hello', 'world', 'bye', 'now')
stuff = list(stuff)
stuff[2] = 'goodbye'
stuff = tuple(stuff)
print(stuff)
"""

#3. List and tuple
# Similarity: Sequences, heterogenous,
# Differences: Mutability, [] vs ()

#4.
"""we can treat strings as sequences because they have enough similarities such as being ordered, 
heterogenous, and can be accessed through indices to be considered one"""

#5.
"""Sets mainly differ from sequence types because they are unordered and don't support indexing"""

#6.
#pi = 3.141592
#str_pi = str(pi)

#7.
"""
0 - 6
1 - 5
3, 7, 11
[]
8, 7, 6, 5, 4
"""

#8.
#print(range(3,17,4)) incorrect revisit
#

#9.
"""
1. yes 2. no 3. yes 4. yes
"""

#10. You can tell it will not because the names are in a set and sets are unordered 

#11.
"""
name_list = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
    }
print(name_list['Alice'])
"""

# Using Collections
#1.
#set_range = range(0,25,3)
#print(set_range[6])

#2.
"""
string = 'Launch School'
first_c = string.find('c')
print(string[first_c:first_c + 6])
"""

#3.
"""
old_tup = (1, 2, 3, 4, 5)
print(old_tup[3:0:-1])

#alt answer to 3
old_tup = list(old_tup)
old_tup.reverse()
print(tuple(old_tup[1:4]))
"""

#4.
"""
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets.get('Dog'))
print(pets.get('Lizard'))
print(pets.get('Lizard','<silence>'))
"""

#5. you can't use ['a','b'] or {1, 4, 9, 16, 25} or {'a' : 1, 'b': 2} because they are mutable
# keys must be immutable

#6. 
"""
print('abc-def'.isalpha()) false
print('abc_def'.isalpha()) false
print('abc def'.isalpha()) false
print('abc def'.isalpha() and 'abc def'.isspace()) false
print('abc def'.isalpha() or 'abc def'.isspace()) false
print('abcdef'.isalpha()) true
print('31415'.isdigit()) true
print('-31415'.isdigit()) false
print('31_415'.isdigit()) false
print('3.1415'.isdigit()) false
print(''.isspace()) false
"""

#7
"""
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
remove = info.split(':')
print('+'.join(remove))
"""

"""
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
remove = info.replace(':','+')
print(remove)
"""

#8 Line 3 finds the most rightward f through the substring 21:35 
# while Line 4 finds the most rightward f through the whole string starting at 21

#9 
"""
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]
stuff[1][3] = 606
print(stuff)
"""

#10
"""
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])
"""
# 11.
"""
print('johnson' in 'Joe Johnson') #False
print('sen' not in 'Joe Johnson') #True
print('Joe J' in 'Joe Johnson') #True
print(5 in range(5)) #False
print(5 in range(6)) #True
print(5 not in range(5, 10)) #False
print(0 in range(10, 0, -1)) #False
print(4 in {6, 5, 4, 3, 2, 1}) #True
print({1, 2, 3} in {1, 2, 3}) #True incorrect because the whole set should be an element
print({3, 2} in {1, frozenset({2, 3})}) #True
"""

# 12.
"""
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)
"""

#13
"""
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')

print('Butterscotch' in cats) #True
print('Butter' in cats) #False
print('Butter' in cats[3]) #True
print('cheddar' in cats) #False
"""

#14
"""
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

my_zip = zip(my_str, my_list, my_tuple, my_range)
print(list(my_zip))
"""
# 15.
# It will print dict_keys([Cat, Bird, Snake])

# Loops and Iterating

# 1. The following code causes an infinite loop because you never increment the counter

# 2.
"""
age = int(input('How old are you? '))
print(f'You are {age} years old.')
for year in range(10,50,10):
    print(f'In {year} years, you will be {age + year} years old.')
"""

# 3.
"""
wmy_list = [6, 3, 0, 11, 20, 4, 17]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1
"""

"""
fmy_list = [6, 3, 0, 11, 20, 4, 17]
for element in fmy_list:
    print(element)
"""

# 4. revisit
"""
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

for element in my_list:
    if element % 2 != 0:
        print(element)
"""

# 5.
"""
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for element in my_list:
    for e in element:
        if e % 2 == 0:
            print(e)
"""

#6. try ternary expression or function
"""
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []
for element in my_list:
    if element % 2 == 0:
        even_el = 'even'
        new_list.append(even_el)
    else:
        odd_el = 'odd'
        new_list.append(odd_el)
print(new_list)
"""

#7.
"""
def find_integers(tuple):
    return [ element
        for element in tuple
        if type(element) is int
    ]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]
"""

#8. revisit
"""
my_set = {
   'Fluffy',
   'Butterscotch',
   'Pudding',
   'Cheddar',
   'Cocoa'
}

my_dict = {member: len(member) 
    for member in my_set
    if len(member) % 2 != 0
}
print(my_dict)
"""
#9.
"""
def factorial(num):
    for i in range(1,num):
        num *= i
    return num

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000
"""

#10. 
"""
import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)
"""
"""
x = (5, 6, 7, 8, 9)
y = x
y[2] = x[0]+x[1]
print(x[2])

"""

# Variables as pointers

#1 The difference between == and is is that == checks if the two objects are equal while is checks if their references are to the same object

#2 {42, 'Monty Python', ('a','b','c'), range(5,10)}

#3 It will print the original dictionary because dict 2 is stored in a different address

#4 It will print [1, 42, 3] because the list value in element[1] points to the same address in both dict

#5
"""
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
"""

"""
#6
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2) #False
print(dict1['a']    is dict2['a']) #True
print(dict1['a'][0] is dict2['a'][0]) #True
print(dict1['a'][1] is dict2['a'][1]) #True
print(dict1['b']    is dict2['b']) #True
print(dict1['b'][0] is dict2['b'][0]) #True
print(dict1['b'][1] is dict2['b'][1]) #True
"""

#More stuff
# 1. The function returns a sorted list with an upper case chris
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

#2.
"""
from math import sqrt
print(sqrt(37))
import math
print(math.sqrt(37))
import math as m
print(m.sqrt(37))
"""

#3. 
"""
def sum_of_squares(num1, num2):
    def square(number):
        return number * number
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
"""

#4.Write a function called increment_counter that increments a counter variable every time it is called. 
"""
counter = 0

def increment_counter():
    global counter
    counter += 1

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
"""

#5.
def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()