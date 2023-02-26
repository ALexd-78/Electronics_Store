#импорты
import csv
import pytest
from utils import Item

@pytest.fixture()
def item():
    return Item("Смартфон", 10000, 5)

@pytest.fixture()
def item1():
    return Item("СуперСмартфон", 10000, 5)

@pytest.fixture()
def test_csv():
    pass


def test_item_initialized(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 5


def test_calculate_total_price():
    assert item.calculate_total_price() == 50000


def test_apply_discount(item):
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 5000


def test_name(item):
    assert item.name == "Смартфон"


def test_name_setter(item1):
    assert item1.name == "Exception: Длина наименования товара превышает 10 символов."



def test_is_integer():
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.5) == False




