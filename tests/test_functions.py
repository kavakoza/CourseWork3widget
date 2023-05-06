from app.utils import *
from app.main import *


def test_load_json_sorted():
    assert load_json_sorted()[2] == {
        'id': 154927927,
        'state': 'EXECUTED',
        'date': '2019-11-19T09:22:25.899614',
        'operationAmount': {
            'amount': '30153.72',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'
            }
        },
        'description': 'Перевод организации',
        'from': 'Maestro 7810846596785568',
        'to': 'Счет 43241152692663622869'
    }

def test_hide_card_number():
    assert hide_card_number('Visa Classic 1242877891011123') == 'Visa Classic 1242 87** **** 1123'
    assert hide_card_number('Счет 46878338893256147528') == 'Счет **7528'
    assert hide_card_number('Visa Platinum 6942697754917688') == 'Visa Platinum 6942 69** **** 7688'
    assert hide_card_number('') == ''

def test_display_transactions():
    assert isinstance(display_transactions(), list) is True
    assert display_transactions()[1] == "07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD\n"

