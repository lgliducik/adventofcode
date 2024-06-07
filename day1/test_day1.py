from day1.day1 import get_number
import pytest

# print(get_number("1abc2"))
# print(get_number("pqr3stu8vwx"))
# print(get_number("a1b2c3d4e5f"))
# print(get_number("treb7uchet"))


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1abc2", 12),
        ("pqr3stu8vwx", 38),
        ("a1b2c3d4e5f", 15),
        ("treb7uchet", 77),
        ("5zpjtbgpkvkxbgpsp3cgklflkhdteightwortv", 53)
    ],
)
def test_get_number(test_input, expected):
    assert get_number(test_input) == expected