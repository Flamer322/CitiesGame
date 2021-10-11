import pytest
from CitiesGame import CitiesDict


@pytest.fixture
def cities_dict():
    return CitiesDict()


def test_is_city(cities_dict):
    assert cities_dict.is_city('Архангельск') == True
    assert cities_dict.is_city('Москва') == True
    assert cities_dict.is_city('Варшава') == True
    assert cities_dict.is_city('Стол') == False
    assert cities_dict.is_city('Стул') == False


def test_is_available(cities_dict):
    assert cities_dict.select_city('Архангельск') == True
    cities_dict.select_city('Архангельск')
    assert cities_dict.select_city('архангельск') == False
    assert cities_dict.select_city('Москва') == True
    assert cities_dict.select_city('Стол') == False
    assert cities_dict.select_city('Стул') == False


def test_select_city(cities_dict):
    assert cities_dict.select_city('Архангельск') == True
    assert cities_dict.select_city('архангельск') == False
    assert cities_dict.select_city('Москва') == True
    assert cities_dict.select_city('Санкт-Петербург') == True
    assert cities_dict.select_city('Москва') == False


def test_get_next_char(cities_dict):
    assert cities_dict.get_next_char('Архангельск') == 'К'
    assert cities_dict.get_next_char('Москва') == 'А'
    assert cities_dict.get_next_char('Чаны') == 'Н'
    assert cities_dict.get_next_char('Пермь') == 'М'
    assert cities_dict.get_next_char('Калуга') == 'А'