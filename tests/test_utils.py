import pytest
from utils import Item, Phone


@pytest.fixture
def item():
    item = Item("Смартфон", 10000, 5)
    return item


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test_item_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 5


def test_calculate_total_price(item):
    '''Проверяет общую сумму всех товаров одной категории в магазине'''
    assert item.calculate_total_price() == 50000


def test_apply_discount(item):
    '''Проверяет сумму товара одной категории в магазине'''
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000


def test_name(item):
    assert item.name == "Смартфон"


def test_name_setter(item):
    with pytest.raises(Exception):
        item.name = 'СуперСмартфон'
    item.name = 'Смартфон'


def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_item_repr(item):
    '''Проверяет вывод всей информации об экземпляре класса Item'''
    assert item.__repr__() == "Item('Смартфон', 10000, 5)"


def test_item_str(item):
    '''Проверяет вывод информации пользователю об экземпляре класса Item'''
    assert item.__str__() == "Смартфон"


def test_phone_init(phone):
    '''Проверяет инициализацию класса Phone'''
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5


def test_phone_repr(phone):
    '''Проверяет вывод всей информации об экземпляре класса Phone'''
    assert phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(item, phone):
    '''Проверяет сложение экземпляров классов Item и Phone по количеству quantity,
    иначе выводит ошибку'''
    with pytest.raises(ValueError):
        phone + 200
    assert phone + item == 10


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2


def test_number_of_sim_setter(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    assert phone.number_of_sim == 2