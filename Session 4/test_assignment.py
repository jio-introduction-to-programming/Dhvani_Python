from assignment import (create_list, find_element_in_list, generate_square_list,
                        add_element, remove_element, create_dict, get_value_from_key,
                        generate_dict, get_keys, get_values, get_last_element,
                        get_slice, count_elements, create_range, check_greater, check_in_range)

# Lists in Python
def test_create_list():
    assert create_list(5) == [0, 1, 2, 3, 4]
    assert create_list(1) == [0]

def test_find_element_in_list():
    assert find_element_in_list([1, 2, 3, 4, 5], 3) == True
    assert find_element_in_list([1, 2, 3, 4, 5], 6) == False

# List comprehensions
def test_generate_square_list():
    assert generate_square_list(5) == [0, 1, 4, 9, 16, 25]
    assert generate_square_list(2) == [0, 1, 4]

# List methods
def test_add_element():
    assert add_element([1, 2, 3], 4) == [1, 2, 3, 4]
    assert add_element([], 1) == [1]

def test_remove_element():
    assert remove_element([1, 2, 3], 2) == [1, 3]

# Dictionaries
def test_create_dict():
    assert create_dict(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}

def test_get_value_from_key():
    assert get_value_from_key({'a': 1, 'b': 2, 'c': 3}, 'b') == 2

# Dictionary comprehensions
def test_generate_dict():
    assert generate_dict(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dictionary methods
def test_get_keys():
    assert get_keys({'a': 1, 'b': 2, 'c': 3}) == ['a', 'b', 'c']

def test_get_values():
    assert get_values({'a': 1, 'b': 2, 'c': 3}) == [1, 2, 3]

# Negative indexing
def test_get_last_element():
    assert get_last_element([1, 2, 3, 4, 5]) == 5
    assert get_last_element(['a', 'b', 'c']) == 'c'

# List slicing
def test_get_slice():
    assert get_slice([1, 2, 3, 4, 5], 1, 3) == [2, 3]
    assert get_slice(['a', 'b', 'c', 'd', 'e'], 2, 4) == ['c', 'd']

# For loop
def test_count_elements():
    assert count_elements([1, 2, 3, 4, 5]) == 5
    assert count_elements([]) == 0

# Range function
def test_create_range():
    assert create_range(1, 5) == [1, 2, 3, 4]
    assert create_range(0, 3) == [0, 1, 2]

# If else
def test_check_greater():
    assert check_greater(5, 3) == True
    assert check_greater(3, 5) == False

# If else with logical operators
def test_check_in_range():
    assert check_in_range(3, 1, 5) == True
    assert check_in_range(7, 1, 5) == False
