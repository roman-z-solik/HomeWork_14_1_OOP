import json
import os

from src.task import Product, Category
from tests.conftest import product


def read_json(path: str) -> dict:
    fullpath = os.path.abspath(path)
    with open(fullpath, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
    return json_data


def load_json_data(json_data):
    new_categorys = []
    for category in json_data:
        new_products = []
        for prod in category['products']:
            new_products.append(Product(**prod))
        category['products'] = new_products
        new_categorys.append(Category(**category))

    return new_categorys


if __name__ == '__main__':
    data = read_json('../data/products.json')
    cat_data = load_json_data(data)
    print(cat_data[0].name)
    print(cat_data[0].products[0].name)