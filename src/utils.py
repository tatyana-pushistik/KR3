from config import ROOT_DIR
import json
import datetime
import os
file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')

def get_load_data(file_path):
    """Загружаем данные"""
    with open(file_path, 'r', encoding= 'utf-8') as file:

        return json.load(file)


def get_EXECUTED_data(json_data):
    """отбираем операция у котрых статус EXECUTED"""
    EXECUTED_data = []
    for EXECUTED_content in json_data:
        if EXECUTED_content.get('state') == 'EXECUTED':
            EXECUTED_data.append(EXECUTED_content)
    return(EXECUTED_data)


def get_top_row(EXECUTED_data, top_row):
    """сотрируем по дате операция и забираем последние (количество передается в top_row) """
    top_row_data = sorted(EXECUTED_data, key=lambda operation: operation["date"], reverse=True)
    top_row_res = top_row_data[:top_row]
    return top_row_res


def convert_date(row):
    """форматируем дату в формат 01-01-2024 """
    date_from_str = datetime.datetime.strptime(row.get("date"), '%Y-%m-%dT%H:%M:%S.%f')
    date_format = date_from_str.strftime("%d-%m-%Y")
    return date_format


def hidden_number(row):
    """Счет 43241152692663622869"""
    if row is None:
        return "Нет данных"
    card_data = row.split(' ')
    card_number = card_data.pop(-1)
    if row.lower().startswith("счет"):
        card_number = f"**{card_number[-4:]}"
    else:
        card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    card_data.append(card_number)
    return( f'{" ".join(card_data)}')


def result_transactions(top_row_res):
    result = ""
    for row in top_row_res:
        result += f"\n{convert_date(row)} {row.get('description')}"
        result += f"\n{hidden_number(row.get('from'))} -> {hidden_number(row.get('to'))}"
        result += f"\n{row.get('operationAmount').get('amount')} {row.get('operationAmount').get('currency').get('name')}\n"
    return result

