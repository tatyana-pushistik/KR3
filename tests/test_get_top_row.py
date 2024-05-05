from src.utils import get_top_row
import pytest

@pytest.fixture
def EXECUTED_data():
    return [
        {"date": "2022-01-01", "value": 10},
        {"date": "2022-02-01", "value": 20},
        {"date": "2022-03-01", "value": 30},
        {"date": "2022-04-01", "value": 40},
        {"date": "2022-05-01", "value": 50}
    ]

def test_get_top_row(EXECUTED_data):
    top_row = 3
    expected_result = [
        {"date": "2022-05-01", "value": 50},
        {"date": "2022-04-01", "value": 40},
        {"date": "2022-03-01", "value": 30}
    ]
    assert get_top_row(EXECUTED_data, top_row) == expected_result
