from config import ROOT_DIR
import json
import os
file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')

def get_load_data(file_path):
    """Загружаем данные"""
    with open(file_path, 'r', encoding='utf-8') as file:
        file_r = file.read()
        json_data = json.loads (file_r)
        return json_data

