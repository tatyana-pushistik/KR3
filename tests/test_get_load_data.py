import pytest
import json
from src.utils import get_load_data
import os
from config import ROOT_DIR

file_path = os.path.join(ROOT_DIR, 'data', 'operations.json')


def test_is_file_exists():
    assert os.path.exists(file_path) is True


def test_get_load_data():
    data = get_load_data(file_path)
    assert isinstance(data, list)
