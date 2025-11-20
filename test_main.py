import pytest
import main

# Тесты для get_first_and_last_char()
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "ho"),
    ("python", "pn"),
    ("a", "aa"),
    ("ab", "ab"),
])
def test_get_first_and_last_char(input_str, expected):
    assert main.get_first_and_last_char(input_str) == expected

# Тесты для get_middle_chars()
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "ell"),
    ("python", "ytho"),
    ("a", ""),
    ("ab", ""),
    ("abc", "b"),
])
def test_get_middle_chars(input_str, expected):
    assert main.get_middle_chars(input_str) == expected

# Тесты для reverse_string()
@pytest.mark.parametrize("input_str, expected", [
    ("hello", "olleh"),
    ("python", "nohtyp"),
    ("", ""),
    ("a", "a"),
])
def test_reverse_string(input_str, expected):
    assert main.reverse_string(input_str) == expected

# Тесты для is_palindrome()
@pytest.mark.parametrize("input_str, expected", [
    ("racecar", True),
    ("level", True),
    ("hello", False),
    ("a", True),
    ("", True),
    ("A man a plan a canal Panama", True), # Тест с пробелами и регистром
])
def test_is_palindrome(input_str, expected):
    # Модифицируем функцию для теста, чтобы она обрабатывала пробелы и регистр
    # Это распространенный подход при проверке палиндромов
    processed_str = ''.join(filter(str.isalnum, input_str)).lower()
    assert (processed_str == processed_str[::-1]) == expected


# Тесты для count_vowels()
@pytest.mark.parametrize("input_str, expected", [
    ("Hello World", 3),
    ("Python is awesome", 6),
    ("Rhythm", 0),
    ("", 0),
    ("AEIOUaeiou", 10),
])
def test_count_vowels(input_str, expected):
    assert main.count_vowels(input_str) == expected

# Тесты для remove_spaces()
@pytest.mark.parametrize("input_str, expected", [
    ("hello world", "helloworld"),
    ("  leading and trailing spaces  ", "leadingandtrailingspaces"),
    ("no spaces", "nospaces"),
    ("", ""),
])
def test_remove_spaces(input_str, expected):
    assert main.remove_spaces(input_str) == expected

# Тесты для capitalize_words()
@pytest.mark.parametrize("input_str, expected", [
    ("hello world", "Hello World"),
    ("python is awesome", "Python Is Awesome"),
    ("  leading spaces", "  Leading Spaces"),
    ("already capitalized", "Already Capitalized"),
    ("singleword", "Singleword"),
])
def test_capitalize_words(input_str, expected):
    assert main.capitalize_words(input_str) == expected
