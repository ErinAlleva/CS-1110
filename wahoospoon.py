# Alex Hicks (awh4kc)
# Kevin John Dela Merced (krd5sw)


import random

restaurants = ["The Ivy Inn", "Christian's Pizza", "Jack Brown's Beer & Burger Joint", "Citizen Burger", "Boylan Heights"]
styles = ["desserts", "pizza", "burger", "burger", "burger"]
costs = ["$$$","$", "$", "$$", "$$"]

def get_random_rest():
    r = restaurants[random.randint(0,4)]
    s = styles[restaurants.index(r)]
    c = costs[restaurants.index(r)]
    return r, s, c

def get_rest_style(style):
    if style == "Burger":
        r = restaurants[random.randint(2,4)]
        s = styles[restaurants.index(r)]
        c = costs[restaurants.index(r)]
    else:
        r = restaurants[styles.index(style)]
        s = styles[restaurants.index(r)]
        c = costs[restaurants.index(r)]
    return r, s, c


def get_rest_cost(cost):
    if cost == "$":
        r = restaurants[random.randint(1,2)]
        s = styles[restaurants.index(r)]
        c = costs[restaurants.index(r)]
    elif cost == "$$":
        r = restaurants[random.randint(3,4)]
        s = styles[restaurants.index(r)]
        c = costs[restaurants.index(r)]
    else:
        r = restaurants[costs.index(cost)]
        s = styles[restaurants.index(r)]
        c = costs[restaurants.index(r)]
    return r, s, c

print("Welcome to WahooSpoon!")
print("1. Get a random restaurant")
print("2. Get a random restaurant based on style")
print("3. Get a random restaurant based on cost")
choice = int(input("Choice?: "))

if choice == 1:
    r, s, c  = get_random_rest()
elif choice ==  2:
    print(set(styles))
    style = input("What style would you like?: ").lower()
    r, s, c = get_rest_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    r, s, c = get_rest_cost(cost)
print("We're going to " + str(r) +   " today! (Style: " + str(s) + "/ Cost: " + str(c) + ")")