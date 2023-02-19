import pytest

from utils import Item

def test_calculate_total_price():
    '''Проверяет общую сумму всех товаров одной категории в магазине'''
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 160000


def test_apply_discount():
    '''Проверяет сумму товара одной категории в магазине'''
    item1 = Item("Смартфон", 10000, 20)
    assert item1.apply_discount() == 8000