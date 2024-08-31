import pytest
from string_calculator import StringCalculator

calculator = StringCalculator()

def run_all_tests():
    try:
        test_add_empty_string()
        test_add_single_number()
        test_add_two_numbers()
        test_add_multiple_numbers()
        test_add_with_newlines()
        test_add_with_custom_delimiter()
        test_add_with_custom_delimiter_and_newlines()
        test_add_with_different_custom_delimiter()
        test_add_with_long_custom_delimiter()
        test_add_negative_numbers()
        test_add_with_custom_delimiter_and_negative_numbers()
        test_add_with_large_numbers()
        test_add_with_custom_delimiter_and_large_numbers()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed: {e}")

def test_add_empty_string():
    assert calculator.add("") == 0


def test_add_single_number():
    assert calculator.add("1") == 1


def test_add_two_numbers():
    assert calculator.add("1,2") == 3


def test_add_multiple_numbers():
    assert calculator.add("1,2,3,4") == 10


def test_add_with_newlines():
    assert calculator.add("1\n2,3") == 6


def test_add_with_custom_delimiter():
    assert calculator.add("//;\n1;2") == 3


def test_add_with_custom_delimiter_and_newlines():
    assert calculator.add("//;\n1;2\n3") == 6


def test_add_with_different_custom_delimiter():
    assert calculator.add("//|\n1|2|3") == 6


def test_add_with_long_custom_delimiter():
    assert calculator.add("//***\n1***2***3") == 6


def test_add_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -1,-3"):
        calculator.add("1,-1,2,-3")


def test_add_with_custom_delimiter_and_negative_numbers():
    with pytest.raises(ValueError, match="negative numbers not allowed: -2,-4"):
        calculator.add("//;\n1;2;-2;4;-4")


def test_add_with_large_numbers():
    assert calculator.add("1000,1001,2") == 1002


def test_add_with_custom_delimiter_and_large_numbers():
    assert calculator.add("//;\n1000;1001;2") == 1002

if __name__ == "__main":
    run_all_tests()