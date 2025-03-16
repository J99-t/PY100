#String Formatting
name = "Victor"
profession = "programmer"

message_format = "Hello, {}. You are a {}"
formatted_message = message_format.format(name,profession)
#print(formatted_message)

#print(f'Hello, {name}. You are a {profession}')

#Style Guide
ice_cream_density=10

while ice_cream_density > 0:
    #print('Drip...')
    ice_cream_density -= 1

#print('The ice cream melted.')

from datetime import datetime
current_datetime = datetime.now()
#print(current_datetime)

#Syntax error
speed_limit = 60
current_speed = 80
"""
if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    """
#TypeError
tweet = 'Woohoo! :-)'
"""
if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + str(5))
"""
#Loop and print
"""
for num in range(0, 11, 2):
    print(num) # 0 2 4 6 8 10
"""
#Countdown
"""
for i in range(10, 0, -1):
    print(i)
print('Launch!')
"""
#Triple Greeting
greeting = 'Aloha!'
x=0
"""
while x < 3:
    print(greeting)
    x += 1
"""
#Take Two
"""
for i in range(1,101):
    print(i * 2)
"""
#Looping over List Elements
lst = [1, 3, 7, 15]
index = 0
"""
while index < len(lst):
    print(lst[index])
    index += 1
"""
#Greet your friends
friends = ['Sarah', 'John', 'Hannah', 'Dave']
"""
for friend in friends:
    print(f'Hello, {friend}!')
"""
#Continue
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]
"""
for city in cities:
    if city != None:
        print(city)
    else:
        continue
"""

#And on and on and on
while True: #while true is always true and there is nothing in the body to change it
    #print("and on")
    break #break will break after the first iteration

#Finding Nemo
#Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']
"""
for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break
    """
index = 0
"""
while index < len(fish_list):
    print(fish_list[index])
    if fish_list[index] == 'Nemo':
        break
    index += 1
"""

#Loop on command
"""
while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    else:
        continue
"""

#Yes? No? Part 1
import random
random_number = random.randint(0, 1)
"""
print('Yes!' if random_number == 1 else 'No.')
value = 'Yes!' if random_number == 1 else 'No.'
# print(value)

print('Yes!') if random_number == 1 else print('No.')
"""
#Check the Weather, Part 1
#weather = input('Whats the weather looking like? ')
"""
if weather.lower() == 'sunny':
    print('Its a beautiful day!')
elif weather.lower() == 'rainy':
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")
"""
#Check the Weather, Part 2
"""
weather = input('Whats the weather looking like? ')

match weather.lower():
    case 'sunny':
        print('Its a beautiful day!')
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")
"""

#Match-Case
"""
animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse': # program will print neigh
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')
"""
"""
#Logical Conditions 1
if False or True: #output will print yest
    print('Yes!')
else:
    print('No...')

#Logical Conditions 2
if True and False:
    print('Yes!')
else:
    print('No...')

#Logical Conditions 3
sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")
"""

# Are we moving
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
#print(is_moving)

# the return output is True since the first operand is true and the second part of the second operand is true
# You do need the parentheses since and has a higher operator precedence than or

#Multiply
def multiply(a,b):
    return a * b

#print(multiply(12, 4))

#Print Quote
def bruce_eckel_quote():
    print('Python is executable pseudocode.')

#bruce_eckel_quote()

# the return value is none since the function doesnt return anything

#Cite the Author

def cite(author, quote):
    print(f'{author} said: "{quote}')

#cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

#Squared Number
def squared_number(num):
    return num*num

#print(squared_number(3))  # 9

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three # the code will never print because the parentheses was never used to invoke it

#Three-way Comparison
def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) == len(string2):
        return 0
    else:
        return 1

#print(compare_by_length('patience', 'perseverance')) # -1
#print(compare_by_length('strength', 'dignity'))      #  1
#print(compare_by_length('humor', 'grace'))           #  0

#Transformation
string = 'Captain Ruby'[0:8]
string += 'Python'
#print(string)

cap_python = 'Captain Ruby'.replace('Ruby','Python')
#print(cap_python)

#Internationalization 1
def greet(greeting):
    match greeting:
        case 'en':
            return 'Hi!'
        case 'fr':
            return'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'ar':
            return 'Haai!'
"""
print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
"""

#Locale Part 1
"""
def extract_language(locale):
    match locale:
        case 'en_US.UTF-8':
            return 'en'
        case 'en_GB.UTF-8':
            return 'en'
        case 'ko_KR.UTF-16':
            return 'ko'
"""
def extract_language(locale):
    return locale.split('_')[0]

#Eprint(extract_language('en_US.UTF-8'))      # en
#print(extract_language('en_GB.UTF-8'))      # en
#print(extract_language('ko_KR.UTF-16'))     # ko

#Locale Part 2
def extract_region(region):
    return region.split('.')[0][3:5]

#print(extract_region('en_US.UTF-8'))    # US
#print(extract_region('en_GB.UTF-8'))    # GB
#print(extract_region('ko_KR.UTF-16'))   # KR

#Internationalization 2

def greet(greeting):
    match greeting:
        case 'en':
            return 'Hi!'
        case 'fr':
            return'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'ar':
            return 'Haai!'
        
def extract_language(locale):
    return locale.split('_')[0]
    
def extract_region(region):
    return region.split('.')[0][3:5]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    if language == 'en':
        match region:
            case 'US':
                return 'Hey!'
            case 'GB':
                return 'Hello!'
            case 'AU':
                return 'Howdy!'

#print(local_greet('en_US.UTF-8'))       # Hey!
#print(local_greet('en_GB.UTF-8'))       # Hello!
#print(local_greet('en_AU.UTF-8'))       # Howdy!

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

#print(local_greet('en_US.UTF-8'))       # Hey!
#print(local_greet('en_GB.UTF-8'))       # Hello!
#print(local_greet('en_AU.UTF-8'))       # Howdy!

#What's my value (Part 1)
if True:
    my_value = 20

#print(my_value) #it will print 20
if False:
    my_new_value = 42

#print(my_new_value) # return an error since condition is true

#What's my value (Part 2)
x = 10

def my_function():
    x = x + 5
    print(x)

#my_function() # the function will raise an error since x hasn't been initialized you cant try to add it

#What's my value (Part 3)
def my_function():
    a = 1

    if True:
        print(a)

#my_function() # It will print 1 since the condition is true and a is initialized in the function

#What's my value (Part 4)
a = 1

def my_function():
    print(a)

#my_function() # This function will also print 1 because the variable a is initialized globally so the function has access to it

#What's my value (Part 5)
a = 1 #anki

def my_function():
    print(a)
    a = 2

#my_function() #This will raise an UnboundLOcalError since print(a) is ran before a = 2 is assigned within the function

#What's my value (Part 6)
a = 1

def my_function():
    a = 2

my_function()
#print(a) # The function will still print 1 because the call to my_function only sets a = 2 locally 
#and both variables are stored as a different reference in memory so it won't have any effect on the global variable

#What's my value (Part 7)
a = 1

def my_function():
    global a
    a = 2

my_function()
#print(a) # The function will print 2 because the keyword global followed by the variable name will make every variable named a in the function
# a global variable so it will apply the changes globally

#What's my value (Part 8)
#print(greeting) # This will result in an NameError since the greeting variable hasn't been defined when you call print

greeting = 'Hello world!'

#What's my value (Part 9)
a = 7

def my_function(b):
    b += 10

my_function(a)
#print(a) # This will print 7 because although a is passed through to my_function it won't make any changes to the global variable because b
# is a separate local variable

#What's my value (Part 10)
b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
#print(b)

#in line 472 we initialize a variable called b to a list that contains the elements 1,2,3
# we invoke the function on line 477 which applies the function body changes to the original variable b in line 472
# we have a function body in line 475 that will reassign the first element in the variable b from 1 to 10
# we print the variable b that has been mutated on line 478 that will result in [10,2,3]

"""
Make each variable scope problem an anki card and rewatch videos to correct wording
"""

#Length
#print(len("These aren't the droids you're looking for."))

#ALL CAPS
#print('confetti floating everywhere'.upper())

all_caps = 'confetti floating everywhere'.upper()
#print(all_caps)

#Ignoring Case
name = 'Roger'
name2 = 'RoGeR'
name3 = 'Dave'
#print(name.lower() == name2.lower())
#print(name.casefold() == name3.casefold())

#Multiline String
rhyme_line_break = 'A pirate I was meant to be!\nTrim the sails and roam the sea!'
#print(rhyme_line_break)

#Contains Character
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print('x' in char_sequence)
print(False if char_sequence.find('z') == -1 else True)
print(True if char_sequence.index('z') else False)