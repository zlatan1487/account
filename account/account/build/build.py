import json
from datetime import datetime
from colorama import Fore


def last_five_executed_operations(filename):
    """
    запуск программы, функция возвращает пять последних успешных операций
    :param filename:
    :return: last_five_operations
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        executed_operations = []
        for i, operation in enumerate(data):
            if operation.get('state') == 'EXECUTED':
                executed_operations.append(operation)

        sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)
        last_five_operations = sorted_operations[:5]

        return last_five_operations


def print_info(operations):
    """
    функция выводит в консоль результат программы в нужном формате, нечего не возвращает
    :param operations:
    :return:
    """
    for item in operations:
        operation = f'''{Fore.RED}{print_date(item['date'])} {Fore.RESET}{item['description']}''''\n' \
               f'''{encrypt_card_from(check_key(item, 'from')).strip()} -> {Fore.YELLOW}{encrypt_card_to(item['to']).strip()}''''\n' \
               f'''{Fore.GREEN}{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}''' '\n'\

        print(operation)


def print_date(data):
    """
    функция принимает дату и преобразовывает в нужный формат
    :param data:
    :return:
    """
    date_time_obj = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%f')
    new_date_string = date_time_obj.strftime('%m.%d.%Y %H:%M:%S')
    return new_date_string


def encrypt_card_from(card_number):
    """
    функция принимае счет отправителя и шифрует его в нужном формате
    :param card_number:
    :return:
    """
    alpha = ''.join(filter(str.isalpha, card_number))
    alpha_strip = ''.join([' ' + i if i.isupper() else i for i in alpha]).lstrip()

    number = ''.join(filter(str.isdigit, card_number))
    temp = len(number) - 12
    masked = temp * '*'
    mask_result = ' '.join([masked[i:i + 4] for i in range(0, len(masked), 4)])
    return f'''{alpha_strip} {number[:4]} {number[4:6]}{len(number[6:8]) * '*'} {mask_result} {number[-4:]}'''


def encrypt_card_to(card_number):
    """
    функция принимае счет получателя и шифрует его в нужном формате
    :param card_number:
    :return:
    """
    alpha = ''.join(filter(str.isalpha, card_number))
    number = ''.join(filter(str.isdigit, card_number))
    groups = ' '.join([number[i:i + 4] for i in range(0, len(number), 4)])
    mask = ''.join([" " if char == " " else "*" for char in groups])
    masked_str = f"{alpha} {groups[:4]}{mask[len(groups[:4]):-len(groups[-4:])]}{groups[-4:]}"

    return masked_str


def check_key(dict_, key):
    """
    функция проверяет словарь на наличия ключа - 'from', в случае его отсутствия возвращает дефолтное значение
    :param dict_:
    :param key:
    :return:
    """
    return dict_[key] if key in dict_ else 'Unknown Sender Account'
