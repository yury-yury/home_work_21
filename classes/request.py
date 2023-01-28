class Request:
    """
    The Request class is an independent class that contains the basic logic for receiving, processing,
    verifying and executing a request to move goods between storage locations.
    """
    def __init__(self, store_list: list, request: str):
        """
        The __init__ function represents an instance method of the class called when initializing a new instance.
        Takes as arguments the instance itself, the list of available storage locations in the form of instances
        of the corresponding classes and the timing of the request received from the user for the transportation
        of goods from one storage location to another. It contains all the necessary logic to check the conditions
        for conducting and performing operations.
        """
        request = request.split()
        for i in range(len(request)):
            if request[i].isdigit():
                self._amount = int(request[i])
                self._product = request[i+1]
                self._from_ = request[i + 3]
                try:
                    self._to = request[i+5]
                except:
                    self._to = "магазин"
                break

        if self._from_ == "склад":
            self.donor = store_list[0]
        else:
            self.donor = store_list[1]

        if self._to == "магазин":
            self.accepter = store_list[1]
        else:
            self.accepter = store_list[0]

        res = self.donor.remove(self._product, self._amount)
        if res:
            print(f'Курьер забрал {self._amount} {self._product} из {self._from_}')
            print(f'Курьер везет {self._amount} {self._product} из {self._from_} в {self._to}')
            res = self.accepter.add(self._product, self._amount)
            if res:
                print(f'Курьер доставил {self._amount} {self._product} в {self._to}')
            else:
                print(f'Курьер возвращает {self._amount} {self._product} на {self._from_}')
                self.donor.add(self._product, self._amount)



