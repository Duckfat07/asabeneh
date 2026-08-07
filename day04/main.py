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
