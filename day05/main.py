# four collection data types in python
#list: ordered and mutable (able to be changed), allows duplicates. uses square brackets []
# tuple: ordered and immutable, allows duplicates. uses parentheses and commas
# set: unordered, unindexed, immutable, but can add new items to the set. duplicates not allowed. curly brackets and commas. 
# dictionary: unordered, mutable, and indexed. No duplicate members. curly brackets and colons

# lists
lst = list()

empty_list = list() # this list contains absolutely nothing
print(len(empty_list)) #0 

# two ways to create lists. 
# first one is by using the built-in list() constructor
# second one is by using square brackets []
lst = []

fruits = ['grapes', 'oranges', 'strawberries', 'mangoes']
print(len(fruits))
print(fruits)

countries = ['Finland', 'Sweden', 'United States']
print(len(countries))
print(countries)

lst = ['Ethan', 18, {'country': 'America', 'city':'New York'}] # lists can contain other data types. 
# lists are square brackets, dictionaries and sets utilize curly brackets

# access items using postive indexing
teams = ['Tottenham', 'Man City', 'Everton', 'Liverpool']
print(teams[0])
print(teams[1] + ' ' + 'and' + ' ' + teams[2])

last_index = len(teams) - 1
last_team = teams[last_index] 

# accessing list items using negative indexing 
players = ['Jasper', 'Mario', 'Ethan', 'Ian']
first_player = players[-4]
last_player = players[-1]
second_last = players[-2]
print(last_player, second_last, first_player)

# unpacking list items
lst = ['one', 'two', 'three', 'four', 'five', 'six']
a, b, c, *rest = lst # order matters, lst should be on the right
print(a)
print(b)
print(c)
print(rest)

first, second, third, *rest, tenth = [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)

countries = ['Korea', 'USA', 'Japan', 'Germany', 'France', 'Canada', 'Albania', 'Bosnia', 'Bulgaria', 'Croatia']
kor, usa, jpn, ger, fr, can, *balkans = countries 
print(kor)
print("the balkans:", balkans)
print(usa)
print(fr)
print(ger)

# slicing items from a list 
# positive indexing: we can specify a range of positive indexes by specifying the start, end, and step. the return value will be a new list. 
cities = ['New York', 'Toronto', 'Philadelphia', 'Boston']
print(cities)
all_cities = cities[0:4]
print(all_cities)
all_cities = cities[0:]
print(all_cities)
first_three = cities[0:3] # this should print the first three
print(first_three)
# negative indexing 
all_cities = cities[-4:]
print(all_cities)
middle_two = cities[-3:-1] 
print(middle_two)
reverse_cities = cities[::-1]
print(reverse_cities)
last_three = cities[-3:] # this should print Toronto, Philadelphia, and Boston
print(last_three)

# modifying lists, lists are mutable
teams = ['Chelsea', 'Tottenham', 'Wolves','Liverpool']
teams[0] = 'Manchester United'
print(teams) # ManU should replace Chelsea

teams[1] = 'Hull City'
print(teams)
last_index = len(teams) - 1
teams[last_index] = 'Barcelona'

# checking items in a list, check if it is a member of a list using in operator
carbs = ['bread', 'oatmeal', 'pasta', 'potatoes']
does_exist = 'bread' in carbs
print(does_exist)
does_exist = 'grits' in carbs
print(does_exist)

# adding items to a list
# lst = list()
# lst.append(item)
sweets = ['brownies', 'chocolate', 'ice cream', 'sundae']
sweets.append('cake')
print(sweets)
sweets.append('candy')
print(sweets)

