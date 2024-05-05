from config import ROOT_DIR
import json
import os
file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')

def get_load_data(file_path):
    """Загружаем данные"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_EXECUTED_data(json_data):
    EXECUTED_data = []
    for EXECUTED_content in json_data:
        if EXECUTED_content.get('state') == 'EXECUTED':
            EXECUTED_data.append(EXECUTED_content)
    return(EXECUTED_data)


def get_top_row(EXECUTED_data, top_row):
    top_row_data = sorted(EXECUTED_data, key=lambda operation: operation["date"], reverse=True)
    return top_row_data[:top_row]
