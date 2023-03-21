import pytest
from utils import Item, Phone, MixinKeyboard, KeyBoard, InstantiateCSVError


@pytest.fixture
def item():
    item = Item("Смартфон", 10000, 5)
    return item


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


@pytest.fixture
def mix():
    mix = MixinKeyboard(language='EN')
    return mix


@pytest.fixture
def kb():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb


@pytest.fixture
def filename():
    filename = 'items.csv'
    return filename

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
    '''Проверяет исключение'''
    with pytest.raises(Exception):
        item.name = 'СуперСмартфон'
    item.name = 'Смартфон'


def test_is_integer():
    '''Проверяет целое ли число'''
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


def test_mixin_init(mix):
    assert mix.language == 'EN'


def test_change_lang(mix):
    assert mix.change_lang() == None
    # assert mix.change_lang() == 'EN'


def test_kb_init(kb):
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == 'EN'


def test_kb_repr(kb):
    assert kb.__repr__() == "KeyBoard('Dark Project KD87A', 9600, 5)"


def test_raise_instantiate_from_csv(filename):
    '''Проверяет исключение'''
    with pytest.raises(InstantiateCSVError):
        filename = 'item.csv'
    filename = 'items.csv'
