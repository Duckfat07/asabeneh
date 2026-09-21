# a string could be a single character or a bunch of texts
# strings can be made using a single or double quote 

letter = 'E'
print(letter)

greeting = 'salutations!'
name = 'Ethan'
print(greeting, name)
print(len(greeting))
print(type(name))

sentence = 'I like to eat chocolate'
print(sentence)

# multi-line string is created using triple single or triple double quotes
multiline_string = '''I am a student who enjoys learning python. 
I desire to be an expert in software and AI. 
This is why I am learning how to code.'''
print(multiline_string)

# merging or connecting strings is called concatenation
first_name = 'Ethan'
last_name = 'Kim'
space = ' '
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(first_name) > len(last_name)) # true

# escape sequences in strings
# \n: new line
# \t: tab means (8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

print('Everyone is enjoying learning python.\nAre you') # line break
print('Python Files\tDays\tDirectories') # adding tab space or 4 spaces
print('Every programming language starts with \"Hello World\"') # to write double quotations within a string
print('This is a backslash symbol (\\)') # to write a backslash
print('Days\tTopics\tExercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35') # the ouput of this should be a grid, with Days, Topics, and Exercises as headlines

# alternate method of string formatting (% operator)
# %s - String (or any object with a string representation)
# %d - Integers 
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision

# strings only
first_name = 'Ethan'
last_name = 'Kim'
language = 'Python'
formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)

# strings and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

python_libraries = ['Django', 'Flask', 'NumPy', 'Madplotlib', 'Pandas']
formatted_string = 'The following are python libraries:%s' % (python_libraries) # the following are python libraries:['Django', 'Flask', 'NumPy','Matplotlib','Pandas']

# new style string formatting (str.format)
first_name = 'Ethan'
last_name = 'Kim'
language = 'Python'
formatted_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formatted_string)

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a+b))
print('{} - {} = {}'.format(a, b, a-b))
print('{} * {} = {}'.format(a, b, a*b))


# String interpolation/f-strings
c = 6
d = 7
print(f'{c} + {d} = {c+d}') # output is 6 + 7 = 13
print(f'{c} - {d} = {c-d}') # 6 - 7 = -1
print(f'{c} * {d} = {c*d}') 
print(f'{c} / {d} = {c /d:.2f}') # :.2f is a format specifier, show 2 digits after decimal point, format the number as a floating-point number
print(f'{c} ** {d} = {c**d}') # 6 ** 7 = 279936
print(f'{c} + {d} - {c*d} = {c+d-c*d}') 

# python strings as sequences of characters 
language = 'Python'
a, b, c, d, e, f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h 
print(e) # o
print(f) # n

# Accessing characters in strings by index, indexing always starts at 0
language = 'python'
letter_1 = language[0] # p 
letter_2 = language[1] # y
letter_3 = language[2]
letter_4 = language[3]
letter_5 = language[4]
letter_6 = language[5]

print(letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + letter_6)

lang = 'Python'
first_letter = lang[0]
print(first_letter)
last_index = len(lang) - 1
last_letter = lang[last_index]
print(last_letter)

# negative indexing
last_letter = lang[-1]
print(last_letter)
second_last = lang[-2]
print(second_last)

# Slicing python strings
first_three = lang[0:3]
print(first_three) # Pyt
all = lang[0:] 
print(all)
last_three = lang[-3:]
print(last_three) # hon

# Reversing a string
greeting = 'Hi World, what\'s up'
print(greeting[::-1]) # string should print in reverse, omitted start & stop, negative step of -1
# ::-1, ::-1, ::-1

# skipping characters while slicing with indexing
language = 'Python'
pto = language[0:6:2] # start 0 begin slicing at index 0, stop before index 6, step 2 move forward 2 indices at a time
print(pto) 

# string methods
# .capitalize(): converts the first character of a string to a capital letter
string = "bison"
print(string.capitalize()) # Bison
# .count() returns occurences of a substring within a string
sentence = "the cat sat on the mat. it was fat."
print(sentence.count('t')) # 7

# .endswith() checks if a string ends with a specified ending
word = "python"
print(word.endswith('on')) # true
print(word.endswith('tion')) # false

# .expandtabs() replaces the tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\of\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10)) 
print(challenge.expandtabs(20))
print(challenge.expandtabs(5))

# .find() returns the index of the first occurence of a substring, if not returns -1
sentence = 'thirty days of python'
print(sentence.find('y')) # 5
print(sentence.find('n')) # 20
#.rfind() returns the index of the last occurence of a substring, if not found returns -1
print(sentence.rfind('y')) # 16
print(sentence.rfind('s')) # 10 

# format(): formats string into a nicer output
name = 'ethan'
age = 20
job = 'entrepreneur'
country = 'America'
sentences = 'I am {}. I am {} years old. I aspire to be an {}. I live in {}.'.format(name, age, job, country)
print(sentences)

radius = 10
pi = 3.14
area = pi*radius**2
print('The area of a circle is {} with radius {}'.format(area, radius))

# index(): returns the lowest index of a substring
# syntax: string.index(substring, start, end)
person = 'Abraham Lincoln'
substring = 'ham'
print(person.index(substring))
# rindex(): returns the highes index of a substring
print(person.rindex(substring, 3)) # will return a valueError if substring is not found

# isalnum() checks alphanumeric character checks if all the characters in a string are alphanumeric (letters and numbers)
phrase = '8675-309Jenny'
print(phrase.isalnum()) # false
line = 'he he'
print(line.isalnum()) # false, because of the space
text = 'powerade2224'
print(text.isalnum()) # true

# isalpha() checks if the string elements are alphabet characters
object = 'boomerangfrisbee'
print(object.isalpha())
text1 = 'bomboclat soccer ball'
print(text1.isalpha())

# isdecimal() checks if all the characters in a string are decimal (0-9)
numbers = '123456'
print(numbers.isdecimal()) # should return true
num = '1 2'
print(num.isdecimal()) # false, spaces are characters

# isdigit() checks if all characters in a string are numbers, more broad than isdecimal()
text = '\u00B2' # the backslash is important
print(text.isdigit()) # True, 
text = '545434'
print(text.isdigit()) #true

num = '123' # 123 without quotes wont work; these are all string methods, won't work for integers
print(num.isdigit())

# isnumeric() checks if all characters are numbers or number-related (accepts more symbols like 1/2)
num = '10'
print(num.isnumeric()) # True
fraction = '\u00B2'
print(fraction.isnumeric()) # true

# isidentifier() checks if a string is a valid variable name
phrase = 'Michael Jordan'
print(phrase.isidentifier()) # false 

# islower() checks if all the characters in a string are lowercase
sentence = 'i like to eat burgers'
print(sentence.islower()) # true

# isupper() checks if all the alphabet characters in the string are uppercase
sentence = 'I like to eat pasta'
print(sentence.isupper()) # false
phrase = 'I LIKE TO EAT PASTA'
print(phrase.isupper()) #true

# join(): returns a concatenated string, joining two or more text strings end-to-end to create a single new string
soccer_players = ['Messi', 'Ronaldo', 'Sonny', 'Salah']
result = ' '.join(soccer_players)
print(result) 
output = ' > '.join(soccer_players)

# strip() removes all given characters starting from the beginning and end of the string
sentence = 'Kanye West more like Kanye East'
print(sentence.strip('stKa')) # only takes one argument

# replace() replaces substring with a given string
sentence = 'I love hiking'
revision = sentence.replace('hiking','cooking')
print(revision)

# split() splits the string, using given string or space as a separator
sentence = 'Cause Girls Like You Run Around With Guys Like Me'
print(sentence.split())
text = 'cocoa, mango, oboe, tango'
print(text.split(', '))

# title() returns a title cased string
saying = 'to thine own self be true'
print(saying.title())

# swapcase() converts all uppercase to lowercase and all lowercase letters to uppercase
building = 'hollenback'
print(building.swapcase())
course = 'FRENCH'
print(course.swapcase())

# startswith() checks if string stars with the specified string
title = '500 Days of Summer'
print(title.startswith('500')) # true
bomba = 500
print(title.startswith(str(bomba)))# true

# String exercises let's fucking go! String methods
string = ['Thirty', 'Days', 'of','Python']
result = ' '.join(string)
print(result)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper()) # .upper() converts all letters to uppercase
print(company.lower()) # .lower() method converts all characters to lowercase

string = 'coding for all'
formatted_string = string.capitalize()
title_string = string.title()
string1 = 'cODING fOR aLL'
swapped = string1.swapcase()
print(formatted_string)
print(title_string)
print(swapped)

text = 'Coding for All'
first_word = text.split()[0]
print(first_word) # to keep the first word

last_word = text.split()[-1]
print(last_word) # to keep only the last word

no_first_word = text.split(' ', 1)[1] 
print(no_first_word) 

word2 = text.split()[1]
word2_1 = word2.capitalize()
word3 = text.split()[2]
two_last_words = str(word2_1 + ' ' + word3)
print(two_last_words)

string1 = '30DaysOfPython'
string2 = 'thirty_days_of_python'
print(string1.isidentifier())
print(string2.isidentifier())

sentence = 'You cannot end a sentence with because because because is a conjunction'
word = 'because'
print(sentence.index(word))
print(sentence.rindex(word))

phrase = 'Coding for All'
substring = 'Coding'
print('Does \'Coding for All \' start with a substring \'Coding\'?')
x = phrase.startswith(substring)
if x == True:
    print('Yes, it does')
else:
    print('no, it does not')

print('Does \'Coding for All \' end with the substring \'Coding\'?')
substring2 = substring.lower()
y = phrase.endswith(substring2)
if y == True:
    print('the phrase ends with substring2')
else: 
    print('the phrase does not end with substring2')