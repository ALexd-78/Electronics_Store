class Item:
    pay_rate = 1 #уровень цены на товар
    all = []


    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls)


    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.all += (self, name, price, count)

    def calculate_total_price(self):
        self.total_price = self.price * self.count * self.pay_rate
        return self.total_price


    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)

print(Item.all)