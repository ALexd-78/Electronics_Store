#импорты
import pytest
from utils import Item

@pytest.fixture()
def item():
    return Item("Смартфон", 10000, 5)


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