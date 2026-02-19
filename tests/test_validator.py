from src.validator import is_valid_number


def test_valid_number():
    assert is_valid_number(10) == True
