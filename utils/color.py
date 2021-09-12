import random

def get_random_color():
    hexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E']
    random.shuffle(hexes)
    ans='#'
    for i in range(6):
        ans=ans+random.choice(hexes)
    return ans