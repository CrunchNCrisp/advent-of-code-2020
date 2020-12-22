from collections import Counter
from itertools import chain

with open('./21/input.txt') as file:
    ingredients = [ x[:-1].split(" (contains ") for x in file.read().splitlines()]

    all_ingredients = set()
    count = Counter()
    possible = {}

    for food in ingredients:
        ingredients = set(food[0].split())
        allergens = set(food[1].split(", "))
        all_ingredients |= ingredients
        count.update(ingredients)

        for alg in allergens:
            if alg not in possible:
                possible[alg] = ingredients.copy()
            else:
                possible[alg] &= ingredients
    
    # Part One
    bad = set(chain.from_iterable(possible.values()))
    print(sum ([ count[ingredient] for ingredient in (all_ingredients - bad)]) )
    
    # Part Two
    taken = set()
    items = []
    while True:
        for alg, ingredients in possible.items():
            if len(ingredients - taken) == 1:
                left = min(ingredients-taken)
                items.append((alg,left))
                taken.add(left)
                break
        else:
            break

    print(",".join(x[1] for x in sorted(items)))
