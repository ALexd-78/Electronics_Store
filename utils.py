import csv


class Item:
    pay_rate = 1  # уровень цены на товар
    all = []

    def __init__(self, name='', price=0, quantity=0, **kwargs):

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        super().__init__(**kwargs)


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


class MixinKeyboard:
    '''Класс для хранения и изменеия раскладки клавиатуры'''
    def __init__(self, language='EN', **kwargs):
        self.__language = language
        super().__init__(**kwargs)


    '''Делает атрибут приватным'''
    @property
    def language(self):
        return self.__language


    def change_lang(self):
        '''Меняет раскладку клавиатуры'''
        self.__language = 'RU'
        return self.__language


class KeyBoard(Item, MixinKeyboard):
# class KeyBoard(MixinKeyboard, Item):

    def calc(self):
        pass




# print(KeyBoard.mro())
kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb)
print(kb.language)
kb.change_lang()
print(kb.language)
# kb.language = 'CH'
# print(kb.lang_en)