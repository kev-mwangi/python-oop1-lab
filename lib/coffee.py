class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ["small", "medium", "large"]:
            raise ValueError("size must be small, medium, or large.")
        self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("price must be a number.")
        self._price = value

    def tip(self):
        print("This coffee is great! Here's a tip for you.")
        self._price += 1