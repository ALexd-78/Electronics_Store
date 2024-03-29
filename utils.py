import csv
import pprint

class InstantiateCSVError(Exception):
    '''Класс исключения при обработке csv-файла'''
    pass


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
    def instantiate_from_csv(cls, filename='items.csv'):
        '''Считывает данные из csv-файла и создает экземпляры класса,
        инициализируя их данными из файла'''
        items = []
        try:
            with open(filename, 'r', encoding='windows-1251') as file:
                data = csv.DictReader(file)
                for i in data:
                    if list(i.keys()) == ["name", "price", "quantity"]:
                        name = i['name']
                        price = int(i['price'])
                        quantity = int(i['quantity'])
                        items.append(cls(name, price, quantity))
                    else:

                        raise InstantiateCSVError
        except FileNotFoundError:
            print("Отсутствует файл items.csv")
        except InstantiateCSVError:
            print("Файл items.csv поврежден")
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
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'



class KeyBoard(Item, MixinKeyboard):
# class KeyBoard(MixinKeyboard, Item):

    def __repr__(self) -> str:
        return super().__repr__().replace('Item', 'KeyBoard')



# Item.instantiate_from_csv()  # создание объектов из данных файла
Item.instantiate_from_csv('items2.csv')  # создание объектов из данных файла
print(Item.all)  # в файле 5 записей с данными по товарам

# item1 = Item.all[0]
# print(item1.name)
# print(KeyBoard.mro())
# kb = KeyBoard('Dark Project KD87A', 9600, 5)
# print(kb.__repr__())
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# kb.language = 'CH'
