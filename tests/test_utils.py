import csv

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


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.name == "Смартфон"



def test_name_setter():
    item2 = Item("СуперСмартфон", 10000, 20)
    assert item2.name == "Exception: Длина наименования товара превышает 10 символов."


def test_is_integer():
    assert Item.is_integer(6.0) == True
    assert Item.is_integer(6.3) == False