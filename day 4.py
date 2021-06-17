def calculation(a,b):
    return a*b
print(calculation(5,5))
# learning lists
coffee_order = [
    "Demi - Oat Latte",
    "Sebastian - normal Latte",
    "Bogdan - Cappuccino",
    "Karl - Black Coffee - no sugar!",
    "Jeff - Espresso",
    "Ray - Hot Chocolate with marshallows!",
    "Abbie - Hot Chocolate",
    "Will - double esspesso, con panna",
    "Godfrey - Coffee with milk no suagar",
    "Viji - Latte!",
    "T-John - Almond milk double Macchiatto",
]

print (coffee_order)

Nintendo_switch_games = [
    "Witcher 3 - Fantasy",
    "Doom - First Person Shooter",
    "Mortal Kombat 11 - Fighting Game",
]
Nintendo_switch_games[2]= "Skyrim - RPG"
Nintendo_switch_games.append("resident evil 7 - horror")
Nintendo_switch_games.pop()
Nintendo_switch_games.reverse()
Nintendo_switch_games.sort()
print (Nintendo_switch_games)

Favourite_website = [ 
    "Youtube",
    "Facebook",
    "Twitter",
]
Favourite_website.append("Linkedin")
Favourite_website.append("dailymotion")
Favourite_website.pop()

print(Favourite_website)

Favourite_colours = [ 
    "Blue",
    "Red",
    "Green",
    "yellow",
    "white",
    "black",
]
Favourite_colours.remove("Red")


print(Favourite_colours)

# doing loops
#learning for loop and while loop
#iteration in coding is the repetition of something more than once

Favourite_drinks = ["coke", "fanta", "tonic"]

for drink in Favourite_drinks:
    print(drink)
for i in Favourite_drinks:
    print(i)
for i in range(5, 11):
    print(i)
for i in range(1, 4):
    print(i)
for i in range(1, 1000):
    print(i)

for i in range(0, 100, 5):
    print(i)
#While loops

num = 0

while num < 10:
    num += 1
    print(num)

import random

rand_num = random.randint(0,50)

my_num = 50

while rand_num != my_num:
    print(rand_num)
    rand_num = random.randint(0,50)

print("You've found it {}!".format(my_num))

statement = "Hello World"

for i in range (13):
    print(statement)

# create a var for my random number
var = random.randint(1, 30)
# make it 6 times
for i in range(6):
    var = random.randint(1, 30) # updates the value to a new random number
    if var % 7 == 0:# check if its divisable by 7 or not
        print(f"This number, {var}, is divisable by seven!")
    else:
        print(f"This number, {var} is not!")

cards = ["Diamond","Spade","Club","Heart"]
my_card = random.randint(0,3)
while cards[my_card] != "Diamond":
    print(cards[my_card])
    my_card = random.randint(0,3)
    if cards[my_card] == "Diamond":
        print("You've found me!")
    else:
        print("Keep trying!")



