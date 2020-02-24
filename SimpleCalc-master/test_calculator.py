import pytest
from string_calculator import add

def test_add_empty():
    assert add("") == 0

def test_add_one():
    assert add("1") == 1

def test_add_two():
    assert add("1,10") == 11

def test_add_uknown_number():
    assert add("1,2,3,4,5") == 15

def test_add_new_line():
    assert add("1\n2,3") == 6

def test_add_new_line_error():
    assert add("1\n") == 1

def test_add_different_delimiters():
    assert add("//;\n1;2") == 3

def test_add_esisting_scenario():
    assert add("1;2;;1") == 4

def test_add_negatives():
    with pytest.raises(Exception) as error:
        assert add("-1,-1,2")
        str(error.value) == "negatives not allowed! -1, -1."

def test_add_bigger():
    assert add("2+1001") == 2   

def test_add_any_length():
    assert add("//[***]\n1***2***3") == 6  

def test_add_multiple():
    assert add("//[*][%]\n1*2%3") == 6   

def test_add_more_characters():
   assert add("//[*][%]\n1*2%+???++@aqw^^^\\^3") == 6
