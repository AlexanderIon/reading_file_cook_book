from pprint import pprint


def get_cook_book(file_name): # формирование menu из файла #
    with open(file_name) as file:
        cook_book = {}

        for line in file:
            name_dish = line.strip()
            count_ingrid = int(file.readline())
            list_ingrid = []

            for ingrid in range(count_ingrid):
                ingredient_name, quantity, measure = file.readline().strip().split("|")
                element = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                list_ingrid.append(element)

            cook_book[name_dish] = list_ingrid
            file.readline()
        return cook_book

def get_list_ingred_order_and_err (menu,order):  # формирование списка ингридиентов  для приготовления блюда из заказа #
    list_ingredient_order = []
    message_err = [] # если в заказе будет блюда , но его не будет в меню.
    for element in range(len(order)):

        if menu.get(order[element]) is None:
             message_err.append(order[element])
        else:
            list_ingredient_order.append(menu.get(order[element]))

    return list_ingredient_order, message_err


def get_shop_list_by_dishes(list_dict_ing_by_order, count_person):
    delta = 0
    dict_ingred = {}

    for dish_ingredient in range(len(list_dict_ing_by_order)):

        for ingredient in range(len(list_dict_ing_by_order[dish_ingredient])):
            name_element = list_dict_ing_by_order[dish_ingredient][ingredient].get('ingredient_name')
            measure_element = list_dict_ing_by_order[dish_ingredient][ingredient].get('measure')
            quantity_element = list_dict_ing_by_order[dish_ingredient][ingredient].get('quantity')

            if name_element in list(dict_ingred.keys()):
                #print(f'{name_element}  {quantity_element}')
                delta = int(quantity_element)

            dict_measure_and_quantity = {'measure': measure_element,
                                         'quantity': (int(quantity_element) + delta) * count_person}
            dict_element = {name_element: dict_measure_and_quantity}

            dict_ingred.update(dict_element)
    return dict_ingred


all_list_dish = get_cook_book('date.txt')


list_dish_order = ["МОЕ блюдо", 'Омлет', 'Запеченный картофель']

list_ingredient_by_order, err = get_list_ingred_order_and_err(all_list_dish, list_dish_order)

pprint("Вывод ингридиентов")


person = 1
res = get_shop_list_by_dishes(list_ingredient_by_order, person)
print(f'Блюдо {err} из Вашего заказа не может быть приготовлено.ЕГО нет в меню ')
pprint('СПИСОК ингридиентов для приготовления заказа ')
pprint(res)














