import random

def tilfeldigeTall():

    tilfeldig = random.sample(range(1,9), 3)
    tilfeldig.sort()
    print(tilfeldig)

tilfeldigeTall()