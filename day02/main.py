# built-in functions and variables
# built-in functions
print("hello world")
len('reservation') # prints the number of characters, len() doesn't work on integers
type({'color':'blue', 'team':'Golden State Warriors','has_steph_curry':True})
str(10) # converts 10 into '10'

x = 2500
print(str(x)) # converts 2500 into a string
int('10') # converts '10' into 10
print(float(300)) # converts 300 into 300.0
input('What is your name?:') # it takes user input

print(min(20,40,19,50)) # gives the minimum value
min([20,40,50,70]) # takes the list as an argument and returns the minimum value
max(90,1000, 400000) # gives the maximum value
print(max([500,501,499,6,200.9, 501.99])) # takes the list as an argument and returns max value

print('sincerely', ',', 'Ethan', 'Kim')

user_age = input('How old are you?')
# input always returns a STRING, make sure to convert to an integer
print(user_age)

num_user_age = int(user_age)
till_20 = 20 - num_user_age
print('You are', till_20, 'years til 20')

name = 'Ethan'
print(type(name))

num1 = 1+1j 
print(type(num1))

pi = 3.14159265
print(type(pi))

directory = {
    'mother':'Caroline',
    'High School':'Xavier',
    'College': 'University of Pennsylvania',
    'age':18
}
print(type(directory))

integer = 100
print(float(integer))

string = '200'
integer_to_string = int(200)
print(integer_to_string)

first_name = 'Zachary'
name_to_list = list(first_name)
print(name_to_list)

num2 = 30
num3 = 5
exp = num2 ** num3
print(exp)

num4, num5 = 5, 10
print(num4*num5)

name = input('what is your name?')
country = input('what country are you from?')

print('name:', name)
print('country of origin:', country)

nem = 'Ethan'
print(len(nem))
nem1 = len(nem)

nim = 'Kim'
nim1 = len(nim)
diff_tween_first_and_last_name_letters = nem1 - nim1

print(nem + ' ' + nim)

print('Your first name is', diff_tween_first_and_last_name_letters, 'letters longer than your last name')