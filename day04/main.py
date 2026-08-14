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


