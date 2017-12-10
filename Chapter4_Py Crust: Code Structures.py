#This is the Py Crust: Code Structures

#Compare with if, elif, and else
"""
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's a cat.")
    else:
        print("It's a bear")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but olny bees can see it")
else:
    print("I've never heard of the color", color)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey!, It's empty")


#Repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1
    
while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)
    if number %2 == 0:
        continue
    print(number, "squared is", number*number)

numbers = [1,3,4,5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')
"""
#Iterate with for
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents )

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

days = ['Monday','Tuesday','Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee','tea','bear']
desserts = ['tiramisu', 'ice cream','pie','pudding']

for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

print(list( zip(english,french)))

print(dict( zip(english,french)))

for x in range(0,3):
    print(x)
print(zip(english, french))


