from utils import Item

# item = Item('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)

# item.name = 'СуперСмартфон'

Item.instantiate_from_csv()  # создание объектов из данных файла
print(len(Item.all))  # в файле 5 записей с данными по товарам
5
item1 = Item.all[0]
print(item1.name)

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))