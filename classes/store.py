from classes.storage import Storage


class Store(Storage):
    """
    The Store class inherits properties and methods from the base Storage class
    and is a model of a warehouse for storing goods.
    """
    def __init__(self, items: dict, capacity=100):
        """
        The __init__ function represents a method for initializing an instance of a class, defines
        the initial properties of the instance inherited from the base class, takes as arguments
        the instance itself, the name and quantity of goods stored in the form of a dictionary {product: quantity}
        and the storage capacity with the support of a value by omission equal to 100 as an integer.
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
        if self.get_free_space() >= quantity:
            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity
            return True
        else:
            print('Вместимость скада не позволяет принять товар. \nСклад не резиновый.')
            return False


