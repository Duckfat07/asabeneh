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
