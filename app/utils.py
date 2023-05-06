import json
import operator
import os.path
import datetime


def load_json_sorted():
    """
    Загрузка данных из json-файла, сортировка словарей, фильтр транзакций по значению "EXECUTED"
    :return: Отсортированные данные по убывание даты
    """
    filedir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(filedir[:-3], 'operations.json'), 'r', encoding='UTF-8') as f:
        data = json.load(f)
        filtered_data = filter(None, data)
        sorted_data = sorted(filtered_data, key=operator.itemgetter('date'), reverse=True)
        executed_transactions = [d for d in sorted_data if d['state'] == 'EXECUTED']
        return executed_transactions


def hide_card_number(string):
    """
    Маскировка номера счёта или карты
    :param string: Данные из json-файла в формате str
    :return: Замаскированный номер счёта или карты в формате str
    """
    if 'Счет' in string:
        full_number = string[:-20]
        masked_number = (2 * '*' + string[-4:])[-6:]
        return full_number + masked_number
    elif len(string) == 0:
        return ""
    else:
        full_number = string[0:-16]
        masked_number = (
                string[-16:-12] + " " + string[-12:-10]
                + 2 * '*' + ' ' + 4 * '*' + ' ' + string[-4:])
        return full_number + masked_number


def display_transactions():
    """
    Вывод последних пяти транзакций
    :return: Пять последних транзакций из файла json
    """
    data = load_json_sorted()[:5]
    result = []
    for item in data:
        date = datetime.datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f').date()
        formatted_date = datetime.datetime.strftime(date, '%d.%m.%Y')

        description = item['description']

        try:
            info_from = item['from']
        except KeyError:
            info_from = ''
        masked_info_from = hide_card_number(info_from)

        info_to = item['to']
        masked_info_to = hide_card_number(info_to)

        amount = item['operationAmount']['amount']

        currency = item['operationAmount']['currency']['name']

        result_info = f"{formatted_date} {description}\n" \
                 f"{masked_info_from} -> {masked_info_to}\n" \
                 f"{amount} {currency}\n"
        result.append(result_info)
    return result