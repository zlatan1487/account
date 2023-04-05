from account.account.build import build


def test_last_five_executed_operations():
    pass
    assert build.last_five_executed_operations('tests/test_json/test_file.json') == [
        {"id": 594226721, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации", "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"},
        {"id": 594226722, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации", "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"},
        {"id": 594226723, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации", "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"},
        {"id": 594226724, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации", "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"},
        {"id": 594226725, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод организации", "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}}, "from": "Visa Platinum 1246377376343588",  "to": "Счет 14211924144426031657"},
    ]


def test_print_date():
    assert build.print_date('2022-01-15T18:30:00.000000') == '01.15.2022 18:30:00'
    assert build.print_date('2022-02-20T12:45:00.000000') == '02.20.2022 12:45:00'


def test_card_number_from():
    assert build.encrypt_card_from("Visa Classic 2842878893689012").strip() == "Visa Classic 2842 87** **** 9012"
    assert build.encrypt_card_from("Maestro 7810846596785568").strip() == "Maestro 7810 84** **** 5568"
    assert build.encrypt_card_from("Счет 38611439522855669794").strip() == "Счет 3861 14** **** **** 9794"
    assert build.encrypt_card_from("Счет 196288543832159541471488").strip() == "Счет 1962 88** **** **** **** 1488"
    assert build.encrypt_card_from("19628854383215954147").strip() == "1962 88** **** **** 4147"
    assert build.encrypt_card_from("1962885438321595414722").strip() == "1962 88** **** **** ** 4722"
    assert build.encrypt_card_from("").strip() == ""


def test_card_number_to():
    assert build.encrypt_card_to("Visa Classic 2842878893689012").strip() == "VisaClassic 2842 **** **** 9012"
    assert build.encrypt_card_to("Maestro 7810846596785568").strip() == "Maestro 7810 **** **** 5568"
    assert build.encrypt_card_to("Счет 38611439522855669794").strip() == "Счет 3861 **** **** **** 9794"
    assert build.encrypt_card_to("19628854383215954147").strip() == "1962 **** **** **** 4147"
    assert build.encrypt_card_to("").strip() == ""


def test_check_key():
    test_dict1 = {'sender': 'John Doe', 'amount': 100}
    assert build.check_key(test_dict1, 'sender') == 'John Doe'

    test_dict2 = {'amount': 200}
    assert build.check_key(test_dict2, 'sender') == 'Unknown Sender Account'

    test_dict3 = {}
    assert build.check_key(test_dict3, 'sender') == 'Unknown Sender Account'
