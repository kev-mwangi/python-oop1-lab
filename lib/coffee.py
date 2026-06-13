class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def price(self):
        return self._price
    @size.setter
    def size(self, value):
        if value not in ["small", "medium", "large"]:
            print("size must be small, medium, or large.")
        else:           
            self._size = value

    def tip(self):
        print("This coffee is great! Here's a tip for you.")
        self._price += 1