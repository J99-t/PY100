"Basic: Write a function that takes a string and returns the string with all vowels removed." #revisit

def remove_vowels(string):
    vowels = ('a','e','i','o','u')
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

#print(remove_vowels('hello world'))

# Example:
   # remove_vowels("hello world") should return "hll wrld"

"Create a program that asks the user for a number n and prints the sum of all numbers from 1 to n."

#x = int(input("Enter a number:"))
#total = 0
#for i in range(1,x+1):
#    total += i
#print(total)

"""
Write a function that determines if a given string is a palindrome 
(reads the same forward and backward, ignoring spaces, punctuation, and capitalization).
""" #revisit

def is_palindrome(string):
    for char in range(len(string)//2):
        if string[char] != string[(len(string)-1 -char)]:
            return False
    return True

#print(is_palindrome('racecar'))

"""
Create a function that takes a list of numbers and returns a new list containing only the even numbers.
"""

def even_list(numbers):
    even_num_list = []
    for element in numbers:
        if element % 2 == 0:
            even_num_list.append(element)
    return even_num_list

#print(even_list([1,2,3,4,5,6]))

"Write a function that converts temperature from Celsius to Fahrenheit (formula: F = C * 9/5 + 32)."

def celsius_to_fahrenheit(celsius_temp):
    fahrenheit_temp = ((celsius_temp * 9/5) + 32)
    return fahrenheit_temp

#print(celsius_to_fahrenheit(0))
#print(celsius_to_fahrenheit(100))

# Example:
   # celsius_to_fahrenheit(0) should return 32
   # celsius_to_fahrenheit(100) should return 212

"Create a function that takes a list of strings and returns a new list with all strings converted to uppercase."

def to_uppercase(small):
    new_list = []
    for element in small:
        if isinstance(element,str): #preferred over == type(str) because You're trying to check if element is a string, not if it's the str class itself.
            new_list.append(element.upper())
    return new_list

#print(to_uppercase(["hello", "world"]))

   # Example:
   # to_uppercase(["hello", "world"]) should return ["HELLO", "WORLD"]

'Intermediate: Write a function that counts the frequency of each character in a string and returns a dictionary with the results.'     

def char_frequency(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#print(char_frequency("hello"))


   # Example:
   # char_frequency("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}

'Intermediate: Create a function that finds the largest number in a list without using the built-in max() function.'

def find_max(numbers):
    biggest = 0
    for i in numbers:
        if i > biggest:
            biggest = i
    return biggest

#print(find_max([1, 5, 8, 3, 2]))
# Example:
   # find_max([1, 5, 8, 3, 2]) should return 8

'Write a function that takes a list of numbers and returns the average (mean) value.'

def calculate_average(numbers):
    total = 0
    divisible = 0
    for i in numbers:
        total += i
        divisible += 1
    return (total / divisible)

#print(calculate_average([1, 2, 3, 4, 5]))

    # Example:
   # calculate_average([1, 2, 3, 4, 5]) should return 3.0

"Create a program that asks the user for their name and age, then prints a message stating how old they will be in 10 years."

#name = input('Whats your name?')
#age = int(input('How old are you? '))
#print(f'{name} will be {age + 10} in 10 years')

'Write a function that takes a string and returns a dictionary '
'where keys are words and values are the number of times each word appears in the string.'

def count_words(string):
    word_count = {}
    split_string = string.split()
    for i in split_string:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count
        

#print(count_words('hello world hello'))

    # Example:
   # count_words("hello world hello") should return {'hello': 2, 'world': 1}

"Create a function that takes a list of integers and returns a new list where each element is the product of all other elements "
"in the original list except the element at that position."

def product_except_self(numbers):
    new_list=[]
    for i in range(len(numbers)):
        product = 1
        for j in range(len(numbers)):
            if i != j:
                product *= numbers[j]
        new_list.append(product)
    return new_list

#print(product_except_self([1,2,3,4]))

# Example:
   # product_except_self([1, 2, 3, 4]) should return [24, 12, 8, 6]
   # Explanation: [2*3*4, 1*3*4, 1*2*4, 1*2*3]

"Write a function that accepts a string and returns the longest word in the string."
"If there are multiple words with the same maximum length, return the first one."

def longest_word(words):
    word_list = words.split()
    longest = ''
    for word in word_list:
        if len(word) > len(longest):
            longest = word
    return longest

#print(longest_word("The quick brown fox jumps over the lazy dog"))

"Create a function that takes a dictionary containing names and ages as input and returns a "
"new dictionary with only the names of people who are 18 or older."

def filter_adults(dict):
    new_dict = {}
    for key in dict:
        if dict[key] <= 18:
            pass
        

    # Example:
   # filter_adults({"Alice": 20, "Bob": 17, "Charlie": 19, "David": 16}) 
   # should return {"Alice": 20, "Charlie": 19}

'Write a function that takes a list of numbers and returns a new list containing only the even numbers.'

def filter_even(numbers):
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return new_list

#print(filter_even([1,2,3,4,5]))

   # Example:
   # filter_even([1, 2, 3, 4, 5]) should return [2, 4]

'Create a function that merges two lists into a single list, alternating elements from each list. revisit'


   # Example:
   # merge_lists([1, 3, 5], [2, 4, 6]) should return [1, 2, 3, 4, 5, 6]
   # merge_lists([1, 3], [2, 4, 6, 8]) should return [1, 2, 3, 4, 6, 8]

'Write a function that takes a dictionary and returns a list of its keys sorted alphabetically.'
def sorted_keys(dict):
    alphabetical = sorted(dict)
    return alphabetical

#print(sorted_keys({"c": 3, "a": 1, "b": 2}))

   # Example:
   # sorted_keys({"c": 3, "a": 1, "b": 2}) should return ["a", "b", "c"]

"Create a function that adds a new key-value pair to a dictionary if the key doesn't already exist."

def add_if_missing(dict, key, value):
    if key not in dict:
        dict[key] = value
    return dict

#print(add_if_missing({"a": 1, "b": 2}, "c", 3))
      # Example:
   # add_if_missing({"a": 1, "b": 2}, "c", 3) should return {"a": 1, "b": 2, "c": 3}
   # add_if_missing({"a": 1, "b": 2}, "a", 3) should return {"a": 1, "b": 2}    

'Create a function that takes a dictionary and returns a list of all the keys that have values greater than 10.'
def greater_than_ten(dict):
    new_list = []
    for key in dict:
        if dict[key] > 10:
            new_list.append(key)
    return new_list

#print(greater_than_ten({"a": 5, "b": 15, "c": 3, "d": 12}))

   # Example:
   # Input: {"a": 5, "b": 15, "c": 3, "d": 12}
   # Output: ["b", "d"]


'Write a function that merges two lists into a dictionary, where the elements of the first list are the keys and '
'the elements of the second list are the values. If the lists are of different lengths, ignore the extra elements.'

def merge_two_list(keys, values):
    my_dict = {}
    for key in keys:
        for value in values:
            my_dict[key] = value
    return my_dict

#merge_two_list(["a", "b", "c"], [1, 2, 3])

   # Example:
   # Input: ["a", "b", "c"], [1, 2, 3]
   # Output: {"a": 1, "b": 2, "c": 3}

'Create a function that takes a string and returns a dictionary with each character as a key and its frequency as the value.'

def letter_count(string):
    my_dict = {}
    for i in string:
        if i not in my_dict.keys():
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    return my_dict
    
#print(letter_count('hello'))
    
    # Example:
# Input: "hello"
# Output: {"h": 1, "e": 1, "l": 2, "o": 1}

'Create a nested list that represents a small library, where each inner list'
'contains a book title and its author. Then write code that prints each book and its author on one line.'
"""
small_library = [
    ['"The Hobbit" by J.R.R. Tolkien'],
    ['"Dune" by Frank Herbert']
]

for book in small_library:
    print(book)
"""
"""
small_library = [
    {'"The Hobbit"': 'J.R.R. Tolkien'},
    {'"Dune"': 'Frank Herbert'}
]

for book in small_library:
    for title, author in book.items():
        print(f'{title} by {author}')
"""
   # Example output:
   # "The Hobbit" by J.R.R. Tolkien
   # "Dune" by Frank Herbert

'Given two dictionaries containing student grades, write a function that compares them and returns a list of students whose grades improved.'
first_quarter = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
second_quarter = {"Alice": 89, "Bob": 86, "Charlie": 90, "Diana": 95}

def compare_grades(first,second):
    improved_grades_list = []
    for name1,grade1 in first.items():
        for name2,grade2 in second.items():
            if grade2 > grade1 and name1 == name2:
                improved_grades_list.append(name2)
    return improved_grades_list

#print(compare_grades(first_quarter,second_quarter))
"""
def compare_grades(first, second): #improved version
    improved_grades_list = []
    for name in first: #goes through first quarter
        if name in second and second[name] > first[name]: # condition checks for same and accesses values using keys to check grade
            improved_grades_list.append(name)
    return improved_grades_list
"""

# Example:
   # first_quarter = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 95}
   # second_quarter = {"Alice": 89, "Bob": 86, "Charlie": 90, "Diana": 95}
   # Output should be: ["Alice", "Charlie"]

"""
Write a function that takes a list of strings and returns a new list containing only the strings that have more than 5 characters.
   """

   # Example:
   # Input: ["hello", "hi", "goodbye", "hey", "python", "code"]
   # Output: ["goodbye", "python"]

"""
Create a function that takes a dictionary of student names and scores, and returns the name of the student with the highest score.
"""
def highest_score(score_sheet):
    highest = 0
    for name,grade in score_sheet.items():
        if grade > highest:
            highest = grade
            best_student = name
    return best_student

#print(highest_score({"Alice": 92, "Bob": 84, "Charlie": 96, "Diana": 88}))

 # Example:
   # Input: {"Alice": 92, "Bob": 84, "Charlie": 96, "Diana": 88}
   # Output: "Charlie"

#Create a nested function example where an inner function has access to a variable defined in the outer function. 
# Explain how this demonstrates the concept of closures in Python.

def greet():
    greeting = 'Hello'
    def find_name():
        nonlocal greeting
        name = input("What is your name ")
        return name
    name = find_name()
    return f'{greeting} {name}'
    
#print(greet())

#Write a function called sum_to_n that takes a positive integer n as an argument and returns the sum of all integers from 1 to n.
"""
def sum_to_n(pos_int):
    total = 0
    for num in range(1,pos_int+1):
        total += num
    return total

print(sum_to_n(5))
"""

#Create a function called count_vowels that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. 
# Make your function case-insensitive.

def count_vowels(string):
    vowels = ('a','e','i','o','u')
    number_of_vowels = 0
    for letter in string:
        if letter.lower() in vowels:
            number_of_vowels += 1
    return number_of_vowels

#print(count_vowels('HELLO WORLD'))

#Write a function called fizz_buzz that prints numbers from 1 to n (where n is a parameter). 
# For multiples of 3, print "Fizz" instead of the number. 
# For multiples of 5, print "Buzz". 
# For numbers that are multiples of both 3 and 5, print "FizzBuzz"

def fizz_buzz(n):
    for nums in range(0,n+1):
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz")
        elif nums % 3 == 0:
            print("Fizz")
        elif nums % 5 == 0:
            print("Buzz")
        else:
            print(nums)

#fizz_buzz(15)

   # Example:
   # fizz_buzz(15) should print:
   # 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

#Create a function called pattern_printer that takes a positive integer n and prints a pattern of asterisks. 
# The pattern should have n rows, where row i contains i asterisks.

def pattern_printer(n):
    for i in range(0,n+1):
        print('*' * i)
    
#pattern_printer(5)

   # Example:
   # pattern_printer(5) should print:
   # *
   # **
   # ***
   # ****
   # *****

# Write a function called skip_multiples that takes two positive integers: n and skip. 
# The function should print all numbers from 1 to n, except for multiples of skip.
def skip_multiples(n,skip):
    for i in range(0,n+1):
        if i % skip == 0:
            continue
        print(i)

#skip_multiples(15,3)

   # Example:
   # skip_multiples(15, 3) should print:
   # 1, 2, 4, 5, 7, 8, 10, 11, 13, 14

#Create a function called nested_numbers that uses nested loops to create and return a list of lists, 
# where each inner list contains numbers from 1 to the outer loop's current value.

def nested_numbers(loops):
    new_list = []
    for number in range(1,loops+1):
        add_num = []
        for element in range(1,number+1):
            add_num.append(element)
        new_list.append(add_num)
    return new_list

#print(nested_numbers(3))

   # Example:
   # nested_numbers(3) should return:
   # [[1], [1, 2], [1, 2, 3]]

#Write a function that accepts a list of numbers and returns the sum of all positive numbers in the list until a negative number is encountered. 
# Use a while loop with a break statement to stop the summation once a negative number is found.

def sum_of_pos(num_list):
    total = 0
    index = 0
    while index < len(num_list):  # Loop through the list
        if num_list[index] < 0:  # Checks for negative and breaks if true
            break
        total += num_list[index]
        index += 1  # Increment the index to move to the next element
    return total

#print(sum_of_pos([1, 2, 3, -5, 4]))

# Write a function that accepts a positive integer n and prints all even numbers from 1 to n, skipping any number that is divisible by 10. 
# Use a while loop with continue statements to skip numbers divisible by 10.

def all_evens(n):
    counter = 0
    while counter < n:
        if counter % 2 == 0:
            print(counter)
        counter +=1

#all_evens(6)

#Write a while loop that counts from 1 to 10, printing each number. 
# Once it reaches 10, print "Countdown complete!"
"""
i = 1
while i <= 10:
    print(i)
    if i == 10:
        print("Countdown Complete!")
    i += 1
"""
#Write a program that asks the user to enter numbers one at a time. The program should continue asking for numbers until the user enters 0. 
# Then print the sum of all numbers entered (excluding the final 0).
"""
total = 0
num = int(input("Enter a number: "))
while num != 0:
    total += num
    num = int(input("Enter a number: "))
    if num == 0:
        print(total)
"""

#Write a program that asks the user to create a password. The password must be at least 8 characters long. 
# Use a while loop to continue asking for a password until the user enters a valid one.

"""
while True:
    password = input("Enter an 8 character password: ")
    if len(password) >= 8:
        print("Password created successfully!")
        break
    else:
        print("Your password is too short. Try again.")
"""
#Write a list comprehension that creates a list of the squares of numbers from 1 to 10, but only includes squares that are even numbers.

squares = [i * i for i in range(1,11) if i % 2 == 0]
# print(squares)

#You have two lists: names = ['Alice', 'Bob', 'Charlie'] and ages = [24, 32, 19].
#Write code using zip and a comprehension to create a list of strings in the format "Name is age years old".
"""
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 32, 19]

zipped = zip(names,ages)
name_to_age = [f'{name} is {ages} years old' for name,ages in zipped]
print(name_to_age)
"""

#Given three lists:
"""
subjects = ['Math', 'Science', 'History']
scores = [88, 92, 78]
is_passed = [True, True, False]

# Write a dictionary comprehension using zip that creates a dictionary where:
#•   The keys are the subject names
#•   The values are dictionaries containing 'score' and 'passed' key-value pairs

zipped = zip(subjects,scores,is_passed)
dict_comp = {subject: {'score': scores, 'passed': is_passed} for subject, scores, is_passed in zipped}
print(dict_comp)
"""

#Write code that uses the zip function to combine two lists: names = ['Alice', 'Bob', 'Charlie'] and ages = [25, 30, 35]. 
# Then, print each name and age pair.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped = zip(names,ages)
#print(list(zipped))

#Given two lists: keys = ['name', 'age', 'job'] and values = ['Dave', 28, 'Developer'], 
#write code using zip to create a dictionary where the elements of keys are the keys and the elements of values are the values.

keys = ['name', 'age', 'job']  
values = ['Dave', 28, 'Developer']
zipped = zip(keys,values)
my_dict = {keys: values for keys, values in zipped}
#print(my_dict)

"Advanced: Processing Uneven Lists with Zip You have three lists of different lengths:"
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [True, False, True, False]
#Write code that uses zip to combine these lists, handles the fact that they have different lengths, 
#and creates a list of tuples with the elements from each list. Explain what happens to the extra elements in the longer lists.
my_list = []
zipped = zip(list1,list2,list3)
for i in zipped:
    my_list.append(tuple(i))

#print(my_list)

#Write a set comprehension that creates a set of all even numbers between 1 and 20.
my_set = {i for i in range(1,21) if i % 2 == 0}
#print(my_set)

#Create a dictionary using a dictionary comprehension where:
#•   The keys are numbers from 1 to 10
#•   The values are the squares of the keys, but only if the square is not divisible by 3

comp_dict = {key : key*key for key in range(1,11) if key*key % 3 != 0}
#print(comp_dict)

#You have a dictionary of student scores:
# python

scores = {
    'Alice': [85, 90, 78],
    'Bob': [92, 88, 95],
    'Charlie': [76, 80, 85]
}
#Use a dictionary comprehension to create a new dictionary where:
#•   The keys are the student names
#•   The values are sets containing only the scores above 85
"""
student_dict = {key : values for key, value in scores if value > 85}
print(student_dict)
"""

#Write a function called modify_counter that increments a global counter variable by a specified amount. 
# The function should take one parameter: the amount to increment by.
"""
def modify_counter(increment):
    global counter
    counter += increment

counter = 0
modify_counter(5)
print(counter)  # Should output: 5
modify_counter(3)
print(counter)  # Should output: 8
"""

"""
Create a function called process_data that takes a list of numbers. The function should:
•   Use a global variable called processed_count to keep track of how many times the function has been called
•   Calculate the sum of all numbers in the list
•   Return a string in the format: "Processed {count} times. Sum: {sum}"
"""

def process_data(num_list):
    global processed_count
    total = sum(num_list)
    processed_count += 1
    return f'Processed {processed_count} times. Sum: {total}'

# Your code should work with this:
processed_count = 0
#print(process_data([1, 2, 3]))  # Should output: "Processed 1 times. Sum: 6"
#print(process_data([4, 5]))     # Should output: "Processed 2 times. Sum: 9"

"""
Create a counter factory function that creates counters with customizable step values. Your implementation should:
•   Define a function called create_counter that takes a parameter step (default value: 1)
•   Inside create_counter, define a nested function called increment that uses nonlocal to modify a counter variable
•   The increment function should return the updated counter value
•   create_counter should return the increment function
"""

#Write a dictionary comprehension that takes a list of words and creates a dictionary where the keys are the words 
# and the values are the lengths of those words.
words = ['python', 'programming', 'dictionary', 'comprehension']
my_dict = {word: letter_len for word in words for letter_len in range(len(word))}
#print(my_dict)
   # Your dictionary comprehension here

#Given a list of numbers, 
# create a dictionary where the keys are the numbers and the values are strings indicating whether the number is 'even' or 'odd'.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {num: 'even' if num % 2 == 0 else 'odd' for num in numbers}
#print(my_dict)

#Given the following dictionary of student scores:
#Write a dictionary comprehension that creates a new dictionary where the keys are the student names and 
# the values are the average scores of each student.

student_scores = {
       'Alice': [85, 90, 78, 92],
       'Bob': [76, 88, 95, 82],
       'Charlie': [91, 84, 88, 90],
       'David': [72, 68, 75, 83]
   }

dict_scores = {student: sum(scores) / len(scores) for student,scores in student_scores.items()}
#print(dict_scores)

#Write a dictionary comprehension that creates a dictionary where the keys are numbers from 1 to 10 
# and the values are the squares of those numbers.

squared_dict = {num: num*num for num in range(1,11)}
#print(squared_dict)

#Given a string of text, create a dictionary using a dictionary comprehension where the keys are the unique words in the text 
# and the values are the number of times each word appears.

text = "the quick brown fox jumps over the lazy dog"
text_length = {word: letters for word in text.split() for letters in range (len(word)+1) }
#print(text_length)

#Given two lists of equal length (one containing product names and another containing their prices), 
# use a dictionary comprehension to create a dictionary where the keys are the product names and the values are the prices, 
# but only include products whose price is greater than 10.
products = ['apple', 'banana', 'orange', 'mango', 'laptop', 'headphones']
prices = [5, 3, 4, 7, 1200, 150]
#zipped_products = zip(products,prices)
#product_price = {product: price for product,price in zipped_products if price > 10}
product_price = {products[i]: prices[i] for i in range (len(prices)) if prices[i] > 10}
#print(product_price)

#Write a nested function that increments a counter using a nonlocal variable.

def create_counter():
    counter = 0
    def increment_counter():
        nonlocal counter
        counter += 1
        return counter
    return increment_counter()

#print(create_counter())

#Create a function that uses both global and nonlocal variables to track different levels of information.
total_calls = 0

def create_calculator():
    result = 0
    
    def add(n):
        nonlocal result
        global total_calls
        result += n
        total_calls += 1
        return result
        
    def subtract(n):
        nonlocal result
        global total_calls
        result -= n
        total_calls += 1
        return result
    
    def get_result():
        return result
    
    return {'add': add, 'subtract': subtract, 'get_result': get_result}

calc = create_calculator()
#print(calc['add'](5))
#print(calc['subtract'](7))
#print(calc['get_result'])

       # Your code here:
       # 1. Create a local variable called result with initial value 0
       # 2. Define nested functions add(n) and subtract(n) that modify result using nonlocal
       # 3. Both functions should also increment the global total_calls variable
       # 4. Return a dictionary with the add and subtract functions and a way to get the current result

#Implement a nested function structure for a simple banking system that tracks deposits, withdrawals, and 
# enforces a minimum balance using nonlocal variables.
def create_account(initial_balance=0, minimum_balance=0):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if minimum_balance < (balance - amount):
            balance -= amount
            return balance
        else:
            return 'Insufficient Balance'

    def get_balance():
        return balance

    return {'deposit' : deposit, 'withdraw' : withdraw, 'get_balance': get_balance}

       # Your code here:
       # 1. Use a nonlocal balance variable to track the account balance
       # 2. Create deposit(amount) and withdraw(amount) nested functions
       # 3. withdraw should prevent withdrawals that would bring balance below minimum_balance
       # 4. Add a get_balance() function that returns the current balance
       # 5. Return a dictionary with all three functions
   
   # Example usage:
account = create_account(100, 50)
#print(account['deposit'](25))  # balance is now 125
#print(account['withdraw'](70))  # balance is now 55
#print(account['withdraw'](10))  # balance is now 45
success = account['withdraw'](50)  # should fail and return False (would go below minimum)

#Write a function that takes a sentence as input and returns a new string where each word is reversed, 
# but the order of words in the sentence remains the same. For example, "Python is fun" should become "nohtyP si nuf".
def reverse(sentence):
    words = sentence.split()
    for word in words:
        for letter in range(len(word)-1,-1,-1):
            print(word[letter], end='')
        print(' ', end='')

#reverse("Python is fun")

#Create a function that counts the occurrences of each character in a string and returns a dictionary with characters as keys and 
# counts as values. The function should ignore case (treat 'A' and 'a' as the same character) and exclude spaces.

def count_letters(string):
    s = string.casefold().replace(' ', '')
    return {s[letter]: s.count(s[letter]) for letter in range(len(s))}

#print(count_letters('Hello WorLd'))

#Implement a function that finds the longest palindromic substring in a given string. 
# A palindrome reads the same backwards as forwards. For example, in the string "babad", 
# the longest palindromic substring is "bab" or "aba".

def longest_palindrome(substring):
    longest = ''
    for i in range(0,len(substring)):
        for j in range(len(substring)-1,-1,-1):
            if substring[j] != substring[i]:
                longest = ''
            elif substring[j] == substring[i]:
                longest += substring[i]
    return longest

#print(longest_palindrome('rbacecar'))
   # Example input: "rbacecar"
   # Expected output: "cec" (or "aceca" is also valid)