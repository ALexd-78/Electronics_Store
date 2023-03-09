import pytest
from utils import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 5)


def test_item_initialized(item):
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


def test_repr(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 5)"


def test_str(item):
    assert item.__str__() == "Смартфон"
