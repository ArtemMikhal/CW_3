import pytest
from src import main
from datetime import datetime

def tests_outputs_information():
    input_operations = [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }
    ]

    expected_result = """19.08.2018
Перевод с карты на карту
Visa Classic **** **** **** 7658 -> Счет **5229
56883.54 USD"""

    assert main.outputs_information(input_operations) == expected_result