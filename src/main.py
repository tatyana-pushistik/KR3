import json
from utils import get_load_data, get_EXECUTED_data, get_top_row, result_transactions
import os
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')
top_rows = 5

def main():
    content_data= get_load_data(file_path)
    filtered_data = get_EXECUTED_data(content_data)
    sorted_slice_data = get_top_row(filtered_data, top_rows)
    result = result_transactions(sorted_slice_data)
    print (result)
    #print(json.dumps(sorted_slice_data, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    main()
