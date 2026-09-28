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