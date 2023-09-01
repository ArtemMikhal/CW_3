import pytest
import json
import os
from datetime import datetime

from src import functions


def filter_operations():
    assert functions.filter_operations([
        {"state": "EXECUTED", "data": "Operation 1"},
        {"state": "PENDING", "data": "Operation 2"},
        {"state": "EXECUTED", "data": "Operation 3"}
    ]) == [
        {"state": "EXECUTED", "data": "Operation 1"},
        {"state": "EXECUTED", "data": "Operation 3"}
    ]

def test_sorts_filtered_operations():
    input_operations = [
        {"date": "2018-04-22T17:01:46.885252"},
        {"date": "2019-02-12T00:08:07.524972"}
    ]
    expected_result = [
        {"date": "2019-02-12T00:08:07.524972"},
        {"date": "2018-04-22T17:01:46.885252"}
    ]
    assert functions.sorts_filtered_operations(input_operations) == expected_result
    assert functions.sorts_filtered_operations([]) == []
    assert functions.sorts_filtered_operations([{'date': '2023-08-28T10:30:00'}]) == [{'date': '2023-08-28T10:30:00'}]

def test_receives_five_operations():
    assert functions.receives_five_operations([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert functions.receives_five_operations([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5]
    assert functions.receives_five_operations(['a','s', 'd', 'f', 'g', 'h', 'j', 'k']) == ['a','s', 'd', 'f', 'g']
    assert functions.receives_five_operations([1, 2, 3]) == [1, 2, 3]
    assert functions.receives_five_operations([]) == []
    assert functions.receives_five_operations([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == [-5, -4, -3, -2, -1]
    assert functions.receives_five_operations([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]) == [1.1, 2.2, 3.3, 4.4, 5.5]
    assert functions.receives_five_operations([1, "two", 3.0, [4], (5,)]) == [1, "two", 3.0, [4], (5,)]













