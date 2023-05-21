from src.utils import *


def test_get_data():
    expected_result = [
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        },
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265"
        },
        {
            "id": 957763565,
            "state": "EXECUTED",
            "date": "2019-01-05T00:52:30.108534",
            "operationAmount": {
                "amount": "87941.37",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 46363668439560358409",
            "to": "Счет 18889008294666828266"
        },
        {
            "id": 667307132,
            "state": "EXECUTED",
            "date": "2019-07-13T18:51:29.313309",
            "operationAmount": {
                "amount": "97853.86",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 1308795367077170",
            "to": "Счет 96527012349577388612"
        }
    ]

    assert get_data('test_file.json') == expected_result


def test_sorted_oprations():
    expected_result = [{'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
                        'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
                        'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'},
                       {'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
                        'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170',
                        'to': 'Счет 96527012349577388612'},
                       {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
                        'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
                        'to': 'Счет 18889008294666828266'},
                       {'id': 27192367, 'state': 'CANCELED', 'date': '2018-12-24T20:16:18.819037',
                        'operationAmount': {'amount': '991.49', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 71687416928274675290',
                        'to': 'Счет 87448526688763159781'},
                       {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412',
                        'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Счет 26406253703545413262',
                        'to': 'Счет 20735820461482021315'}]

    operations = get_data('test_file.json')
    assert sorted_oprations(operations) == expected_result


def test_five_last_operations():
    expected_result = [{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
                        'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170',
                        'to': 'Счет 96527012349577388612'},
                       {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
                        'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 46363668439560358409',
                        'to': 'Счет 18889008294666828266'},
                       {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412',
                        'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Счет 26406253703545413262',
                        'to': 'Счет 20735820461482021315'}]

    operations = get_data('test_file.json')
    operations = sorted_oprations(operations)
    operations = five_last_operations(operations)
    assert operations == expected_result


def test_get_card_number():
    expected_result = [{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
                        'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод с карты на счет', 'from': 'Maestro 1308 79** **** 7170',
                        'to': 'Счет 96527012349577388612'},
                       {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
                        'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 4636 36** **** **** 8409',
                        'to': 'Счет 18889008294666828266'},
                       {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412',
                        'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Счет 2640 62** **** **** 3262',
                        'to': 'Счет 20735820461482021315'}]

    operations = get_data('test_file.json')
    operations = sorted_oprations(operations)
    operations = five_last_operations(operations)
    operations = get_card_number(operations)
    assert operations == expected_result


def test_get_sent_number():
    expected_result = [{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
                        'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод с карты на счет', 'from': 'Maestro 1308 79** **** 7170',
                        'to': 'Счет **8612'},
                       {'id': 957763565, 'state': 'EXECUTED', 'date': '2019-01-05T00:52:30.108534',
                        'operationAmount': {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод со счета на счет', 'from': 'Счет 4636 36** **** **** 8409',
                        'to': 'Счет **8266'},
                       {'id': 921286598, 'state': 'EXECUTED', 'date': '2018-03-09T23:57:37.537412',
                        'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Счет 2640 62** **** **** 3262',
                        'to': 'Счет **1315'}]

    operations = get_data('test_file.json')
    operations = sorted_oprations(operations)
    operations = five_last_operations(operations)
    operations = get_card_number(operations)
    operations = get_sent_number(operations)
    assert operations == expected_result


def test_get_date():
    expected_result = [{'id': 667307132, 'state': 'EXECUTED', 'date': '13.07.2019',
                        'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод с карты на счет', 'from': 'Maestro 1308 79** **** 7170',
                        'to': 'Счет **8612'}, {'id': 957763565, 'state': 'EXECUTED', 'date': '05.01.2019',
                                               'operationAmount': {'amount': '87941.37',
                                                                   'currency': {'name': 'руб.', 'code': 'RUB'}},
                                               'description': 'Перевод со счета на счет',
                                               'from': 'Счет 4636 36** **** **** 8409', 'to': 'Счет **8266'},
                       {'id': 921286598, 'state': 'EXECUTED', 'date': '09.03.2018',
                        'operationAmount': {'amount': '25780.71', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                        'description': 'Перевод организации', 'from': 'Счет 2640 62** **** **** 3262',
                        'to': 'Счет **1315'}]

    operations = get_data('test_file.json')
    operations = sorted_oprations(operations)
    operations = five_last_operations(operations)
    operations = get_card_number(operations)
    operations = get_sent_number(operations)
    operations = get_date(operations)
    assert operations == expected_result