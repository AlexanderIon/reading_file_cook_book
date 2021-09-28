from pprint import pprint


def get_cook_book(file_name):
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
pprint(get_cook_book('date_one.txt'))




















