import csv



class Item:
    pay_rate = 1 #уровень цены на товар
    all = []


    def __init__(self, name, price, count):
        self.__name = name
        self.price = price
        self.count = count
        self.all.append(self)

    @property
    def name(self) -> str:
        '''Возваращает наименование товара'''
        return self.__name

    @name.setter
    def name(self, value: str):
        '''Проверяет, чтобы длина наименования товара не была более 10 символов,
            иначе возвращает ошибку'''
        if len(value) > 10:
            print("Exception: Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value


    def calculate_total_price(self):
        '''Вычисляет общую стоимость категории товара в магазине'''
        self.total_price = self.price * self.count * self.pay_rate
        return self.total_price


    def apply_discount(self):
        '''Вычисляет актуальную стоимость товара'''
        self.price = self.price * self.pay_rate
        return self.price


    @classmethod
    def instantiate_from_csv(cls):
        '''Считывает данные из csv-файла и создает экземпляры класса,
        инициализируя их данными из файла'''
        items = []
        with open('items.csv') as file:
            data = csv.DictReader(file)
            for i in data:

                items.append(cls(i['name'], int(i['price']), int(i['quantity'])))
        return items

    @staticmethod
    def is_integer(x):
        '''Возвращает True, если число целое'''
        isInt = int(x) == x
        return isInt
        

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8  # устанавливаем новый уровень цен
item1.apply_discount()
print(item1.price)
print(item2.price)

print(Item.all)

item = Item('Телефон', 10000, 5)
item.name = 'Смартфон'
print(item.name)

item.name = 'СуперСмартфон'

Item.instantiate_from_csv()
print(len(Item.all))

i = Item.all[1]
print(i.price)

print(Item.is_integer(i.price))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))
