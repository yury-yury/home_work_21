from classes.request import Request
from classes.shop import Shop
from classes.store import Store


def main():
    """
    The main function is a wrapper that sets initial values, initializes instances of the necessary
    classes, receives data from the user and the relationship between the elements of the application
    in the process of functioning.
    """
    store = Store({"печеньки": 6, "собачки": 4, "коробки": 5, "елки": 8, "конфеты": 8, "апельсины": 11})
    shop = Shop({"собачки": 2, "печеньки": 2})

    while True:
        print("Введите запрос на перемещение товара или выход")
        user_input =  input()
        if user_input == 'выход':
            return

        Request([store, shop], user_input)

        for cur_store, name in [(store, 'склад'), (shop, 'магазин')]:
            print()
            print(f'В {name} хранится:')
            for name, quantity in cur_store.get_items().items():
                print(f'{quantity} {name}')


main()
