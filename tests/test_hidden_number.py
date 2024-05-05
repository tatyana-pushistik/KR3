from src.utils import hidden_number

card_Maestro = "Maestro 1596837868705199"
bill_1 = "Счет 64686473678894779589"
card_visa_classic = "Visa Classic 6831982476737658"
empty_string = None


def test_hide_numbers():
    assert hidden_number(card_Maestro) == "Maestro 1596 83** **** 5199"
    assert hidden_number(card_visa_classic) == "Visa Classic 6831 98** **** 7658"
    assert hidden_number(bill_1) == "Счет **9589"
    assert hidden_number(empty_string) == "Нет данных"