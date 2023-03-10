import csv


class Item:
    pay_rate = 1  # уровень цены на товар
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        '''Выводит полную информацию экземпляра класса'''
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        '''Выводит информацию пользователю об экзмпляре класса '''
        return f"{self.__name}"

    @property
    def name(self) -> str:
        '''Возвращает наименование товара'''
        return self.__name

    @name.setter
    def name(self, value: str):
        '''Проверяет, чтобы длина наименования товара не была более 10 символов,
            иначе возвращает ошибку'''
        if len(value) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = value

    def calculate_total_price(self):
        '''Вычисляет общую стоимость категории товара в магазине'''
        self.total_price = self.price * self.quantity * self.pay_rate
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
                if cls.is_integer(i['price']):
                    price = int(float(i['price']))
                else:
                    price = float(i['price'])
                if cls.is_integer(i['quantity']):
                    quantity = int(float(i['quantity']))
                else:
                    quantity = float(i['quantity'])
                items.append(cls(i['name'], price, quantity))
        return items

    @staticmethod
    def is_integer(x):
        '''Возвращает True, если число целое'''
        isInt = int(x) == x
        return isInt


class Phone(Item):
    '''Класс наследует атрибуты класса Item и ещё есть атрибут
    для хранения количества сим-карт'''
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self) -> str:
        '''Выводит полную информацию экземпляра класса'''
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"


    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError ('Сложение только экземпляров классов Item и Phone')

    @property
    def number_of_sim(self) -> int:
        '''Возвращает количество сим-карт в Phone'''
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int):
        '''Проверяет, чтобы количество физических SIM-карт было
        целым числом больше нуля, иначе возвращает ошибку'''
        if value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = value


item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)
# print(phone1)
# print(repr(phone1))

# print(phone1 + item1)
#
# phone1.number_of_sim = 0
# print(phone1.number_of_sim)
# print(item1.__repr__())

# print(item1 + 1000)

# item2 = Item("Ноутбук", 20000, 5)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# Item.pay_rate = 0.8  # устанавливаем новый уровень цен
# item1.apply_discount()
# print(item1.price)
# print(item2.price)

# print(Item.all)

# item = Item('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)

# item.name = 'СуперСмартфон'

# Item.instantiate_from_csv()
# print(len(Item.all))
#
# i = Item.all[1]
# print(i.price)
#
# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))
