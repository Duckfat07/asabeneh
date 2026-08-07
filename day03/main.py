# variables in python
# assigning a certain data type to a variable is called variable declaration
first_name = 'Ethan'
last_name = 'Kim'
country = 'The United States of America'
age = 18
is_male = True
features = ['athletic','intelligent','hard worker'] # this is an example of a list, uses square brackets 
personal_information = {
    'name':'Ethan Kim',
    'country_of_origin':'Korea',
    'city':'New York City'
}

# Printing the values stored in variables
print('First name:', first_name)
print('Last name:', last_name)
print('length of first name:', len(first_name))

name_of_user = input('What is your name?')
age_of_user = input('How old are you?')

print(name_of_user)
print(age_of_user)

year = 2026
print(type(year))

years_till_2028 = 2028 - year
print(years_till_2028)


# declaring multiple variables on one line
animal, number_of_legs, is_farm = 'pig', 4, True
print(animal, number_of_legs, is_farm)

nickname = 'EJK'
net_worth = 500000000
is_married = False

# area of a circle 
# defining the radius
radius = 25 
area_of_circle = 3.14 * radius ** 2
print('Area of a circle:', area_of_circle)

# area of a rectangle
length = 20
width = 10
rect_area = length * width
print('Area of a rectangle:', rect_area)

# Calculating the wieght of an object
mass = 5
gravity = 9.81 
weight = mass * gravity
print('Weight:', weight, 'N')

# Calculating the density of a liquid 
mass = 60
volume = 0.05 # in cubic meter 
density = mass/volume
print(density, 'kg/m^3')

# booleans
print('A' in 'Asabeneh') # True, A is found in the string 
print('B' in 'Asabeneh') # false there is no uppercase B
print(5 > 3) # True 
print(77 < 3) # false
print(not True) # False 

age = 18
int_age = int(18)
print(type(age))
print(int_age)

height = 5.10
real_height = float(height)
print(type(height))
print(real_height)

complex_num = 5 + 1j
print(type(complex_num))

# area of triangle exercise 
base = int(input('Enter the base of the triangle:')) # input always returns a string
height = int(input('Enter the height of the triangle:')) # input alwas returns a string, so it is necessary to convert the input into an integer
area = 1/2 * base * height
print("This is the area of the triangle:", area)

# perimeter of a triangle
a = int(input('side 1 of triangle:'))
b = int(input('side 2 of triangle:'))
c = int(input('side 3 of triangle:'))
perimeter = a+b+c
print(a + b + c)

# rectangle exercises
length = int(input('what is the length of the rectangle?:'))
width = int(input('what is the width of the rectangle?:'))
area = length * width 
perimeter = 2*length + 2*width

radius = int(input('what is the radius of the circle?:'))
pi = 3.14
area = pi*radius**2 

