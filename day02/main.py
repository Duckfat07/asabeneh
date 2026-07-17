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