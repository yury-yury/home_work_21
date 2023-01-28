from classes.storage import Storage


class Shop(Storage):
    """
    The Shop class inherits properties and methods from the Storage base class
    and represents a store model as a place to store goods.
    """
    def __init__(self, items: dict, capacity=20):
        """
        The __init__ function represents a method for initializing an instance of a class, defines
        the initial properties of the instance inherited from the base class, takes as arguments
        the instance itself, the name and quantity of goods stored in the form of a dictionary {product: quantity}
        and the storage capacity with the support of a value by omission equal to 20 as an integer.
        """
        super().__init__(items, capacity)

    def add(self, name: str, quantity: int):
        """
        The add function represents an instance method of the class that adds the goods delivered for storage
        to the storage location. Accepts as arguments the instance itself, the name and quantity of goods
        delivered in storage in the form of a string and an integer, respectively. Contains the necessary
        logic to check the conditions for the addition. Returns True if the operation is successful,
        or False if it is impossible to perform it.
        """
        if self.get_free_space() >= quantity and ((name in self.items
                                            and self.get_unique_items_count() <= 5) or (name not in self.items
                                            and self.get_unique_items_count() <= 4)):
            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity
            return True
        else:
            print('Вместимость магазина не позволяет принять товар. \nМагазин не резиновый.')
            return False