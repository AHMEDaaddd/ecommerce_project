"""Тесты для функции загрузки категорий из JSON."""

import json
import tempfile
from pathlib import Path

from src.loader import load_categories_from_json
from src.models import Category


def test_load_categories_from_json() -> None:
    """Проверяет корректную загрузку категорий и продуктов из JSON."""
    data = [
        {
            "name": "Категория 1",
            "description": "Описание категории",
            "products": [
                {
                    "name": "Товар 1",
                    "description": "Описание товара",
                    "price": 123.45,
                    "quantity": 2,
                }
            ],
        }
    ]

    with tempfile.TemporaryDirectory() as tmpdir:
        json_path = Path(tmpdir) / "test_data.json"
        json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        start_cat = Category.category_count
        start_prod = Category.product_count

        categories = load_categories_from_json(str(json_path))

        assert isinstance(categories, list)
        assert len(categories) == 1

        cat = categories[0]
        assert cat.name == "Категория 1"
        assert cat.description == "Описание категории"
        assert len(cat.products) == 1

        product = cat.products[0]
        assert product.name == "Товар 1"
        assert product.price == 123.45
        assert product.quantity == 2

        assert Category.category_count == start_cat + 1
        assert Category.product_count == start_prod + 1
