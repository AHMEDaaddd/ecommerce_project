"""Модуль для загрузки категорий и товаров из JSON-файла."""

import json
from typing import List

from src.models import Category, Product


def load_categories_from_json(path: str) -> List[Category]:
    """Загружает категории и продукты из JSON-файла.

    Args:
        path (str): Путь к JSON-файлу.

    Returns:
        List[Category]: Список объектов категорий.
    """
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    categories = []
    for category_data in data:
        products = [Product(**product) for product in category_data["products"]]
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products,
        )
        categories.append(category)
    return categories
