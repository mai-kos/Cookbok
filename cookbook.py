from pprint import pprint

with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        meal = line.strip()
        ingredient_count = int(file.readline())
        ingredients_list = []
        for i in range(ingredient_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients_list.append({'ingredient_name': ingredient_name, 
            'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book.update({meal: ingredients_list})

pprint(f'cook_book = {cook_book}')
print()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for el in dishes:
        ingr_list = cook_book.get(el)
        for ingr in ingr_list:
            key = ingr.get('ingredient_name')
            values = {'measure': ingr.get('measure'), 
            'quantity': int(ingr.get('quantity')) * person_count}
            shop_list.update({key: values})
    return shop_list




pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
