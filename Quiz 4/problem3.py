import random
import itertools
random.seed(1)

card = [1, 2, 3, 4]
combinations = list(itertools.permutations(card, 4))

def naive():
    print("Naive algorithm:")
    my_map = {}
    for per in combinations:
        my_map[per] = 0
    for _ in range(1000000):
        card = [1, 2, 3, 4]
        for i in range(4):
            n = random.randint(0, 3)
            card[i], card[n] = card[n], card[i]
        my_map[tuple(card)] += 1
    for key in my_map:
        print(f"{key}: {my_map[key]} times")
def fisher():
    print("Fisher-Yates shuffle:")
    my_map = {}
    for per in combinations:
        my_map[per] = 0
    for _ in range(1000000):
        card = [1, 2, 3, 4]
        for i in range(3, 0, -1):
            n = random.randint(0, i)
            card[i], card[n] = card[n], card[i]
        my_map[tuple(card)] += 1
    for key in my_map:
        print(f"{key}: {my_map[key]} times")

if __name__ == "__main__":
    naive()
    fisher()
