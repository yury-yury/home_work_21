class Storage:
    """
    The Storage class is the parent class, for all its child classes, defines common properties
    and methods that are common to all classes representing the abstraction of storage locations.
    """
    def __init__(self, items: dict, capacity: int):
        """
        The __init__ function implements the "magic" method called when initializing an instance of the class,
        takes as arguments the instance itself, the name and quantity of goods stored in the form of a dictionary
        and the total storage capacity as an integer.
        """
        self.items = items
        self.capacity = capacity


    def add(self, name: str, quantity: int):
        """
        The add function of the base class implements the method of the class used to add goods
        to the storage location after delivery, takes as arguments the instance itself, the name
        as a string and the quantity of the goods as an integer.
        In further use, it will be overridden in child classes.
        """
        if name in self.items:
            self.items[name] += quantity
        else:
            self.items[name] = quantity


    def remove(self, name: str, quantity: int):
        """
        The remove function of the base class implements the method of the class used to reduce the number
        of goods in the storage location after the goods are delivered for delivery, the method performs
        the necessary checks, takes as arguments the instance itself, the name of the goods as a string
        and the quantity of goods as an integer. In further use, it is inherited into child classes.
        """
        if name in self.items:
            if self.items[name] >= quantity:
                print('Нужное количество есть на складе')
                self.items[name] -= quantity
                if self.items[name] == 0:
                    self.items.pop(name)
                return True
            else:
                print('Не хватает на складе, попробуйте заказать меньше')
                return False
        else:
            print('На складе нет такого товара, попробуйте заказать другой')
            return False

    def get_free_space(self):
        """
        The get_free_space function of the base class implements the method of the class used
        to get the number of free spaces in the storage location, takes the instance itself
        as an argument. Returns the number of available seats as an integer.
        In further use, it is inherited into child classes.
        """
        seats_occupied = 0
        for value in self.items.values():
            seats_occupied += value
        return self.capacity - seats_occupied

    def get_items(self):
        """
        The get_items function of the base class implements the method of the class used to get
        the names and quantity of goods in the storage location, takes the instance itself as an argument.
        Returns the name and quantity of the product in the form of a dictionary {product: quantity} .
        In further use, it is inherited into child classes.
        """
        return self.items

    def get_unique_items_count(self):
        """
        The get_unique_items_count function of the base class implements the method of the class used
        to get the number of unique items in the storage location, takes the instance itself as an argument.
        Returns the number of unique product names as an integer .
        In further use, it is inherited into child classes.
        """
        keys_list = list(self.items.keys())
        keys_set = set(keys_list)
        return len(keys_set)

