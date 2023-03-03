#импорты
import pytest
from utils import Item

@pytest.fixture()
def item():
    return Item("Смартфон", 10000, 5)

# @pytest.fixture()
# def item1():
#     return Item("СуперСмартфон", 10000, 5)












