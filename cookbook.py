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

# Проверяем вывод словаря.

pprint(f'cook_book = {cook_book}')
print()

# По-прежнему не совсем понимаю, как соблюдать длину строки по PEP8.
# Как можно логически разбить строку 34?

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for el in dishes:
        ingr_list = cook_book.get(el)
        for ingr in ingr_list:
            key = ingr.get('ingredient_name')
            values = {'measure': ingr.get('measure'), 
            'quantity': int(ingr.get('quantity')) * person_count}
            if key in shop_list.keys():
                shop_list[key]['quantity'] += int(ingr.get('quantity')) * person_count
            else:
                shop_list.setdefault(key, values)
    return shop_list

# Проверяем функцию.
# Ингредиенты не повторяются, а суммируются, если ингредиент уже встречался.

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
print()

def count_lines(file):
    with open(file, 'rt') as file:
        x = len(file.readlines())
        return x

# Немного усложнил задачу дополнительным условием, если мы не знаем кол-во строк в файлах.
# То есть моя функция будет работать с любым количеством строк, при условии,
# что мы знаем названия документов и их количество, как сказано в задаче.

def combine_files():
    len1, len2, len3 = count_lines('1.txt'), count_lines('2.txt'), count_lines('3.txt')
    file_dict = {}
    file_dict.update({len1: '1.txt', len2: '2.txt', len3: '3.txt'})
    keys_list = sorted(list(file_dict.keys()))
    with open('combined.txt', 'a') as document:
        for el in keys_list:
            document.write(file_dict.get(el) + '\n')
            document.write(str(el) + '\n')
            with open(file_dict.get(el), 'rt') as file:
                document.writelines(line + '\n' for line in file.readlines())
    return

# Запись работает, но почему-то добавляется лишняя пустая строка.
# А если убрать из 64 строки '\n', то в итоге все наоборот склеивается.

combine_files()