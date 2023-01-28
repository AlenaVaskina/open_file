# Задание №1

from pprint import pprint

with open("recipes.txt", "r", encoding='utf-8') as f:
    cook_book = {}
    while True:
        dish = f.readline().rstrip()
        if not dish:
            break
        count = int(f.readline())
        cook_book[dish] = []
        for _ in range(count):
            line = f.readline().rstrip().split(' | ')
            cook_book[dish].append({
                'ingredient_name': line[0],
                'quantity': int(line[1]),
                'measure': line[2]
            })
        f.readline()


# Задание №2
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in ingredients:
                ingredients[ingredient['ingredient_name']]['quantity'] = \
                    ingredients[ingredient['ingredient_name']]['quantity'] \
                    + ingredient['quantity'] * person_count
            else:
                ingredients[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
    return ingredients

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))


# Задание №3
import os

sort_name, name_text = {}, {}

for filename in os.listdir("sorted"):
    with open(os.path.join("sorted", filename), 'r', encoding='utf-8') as f:
        text = f.readlines()
        sort_name[filename] = len(text)
        name_text[filename] = text

sort_name = dict(sorted(sort_name.items(), key=lambda x: x[1]))

with open('sorted_file.txt', 'w') as f:
    for key, value in sort_name.items():
        f.write(f"{key}\n")
        f.write(f"{value}\n")
        for line in name_text[key]:
            f.write(f"{line.rstrip()}\n")