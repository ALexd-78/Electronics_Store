class Item:

    def __init__(self, name="", price=0, **kwargs):
        self.name = name
        self.price = price
        super().__init__(**kwargs)


class KeyBoardMixin:

    def __init__(self, language="en", **kwargs):
        self.language = language
        super().__init__(**kwargs)


class Keyboard(KeyBoardMixin, Item):
# class Keyboard(Item, KeyBoardMixin):

    def __repr__(self):
        return f"{self.name}, {self.price}, {self.language}"

k = Keyboard(language="ru", name="My Stubid Keyboard", price=2000)

print(k)