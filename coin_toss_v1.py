import random
def flip_a_coin():
    if random.random() < 0.5:
        return 'Head'
    else:
        return 'Tails'
print(flip_a_coin())
    