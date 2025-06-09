"""Тесты для моделей Product и Category."""

import pytest

from src.models import Category, Product


def test_product_initialization() -> None:
    """Проверяет корректную инициализацию товара."""
    p = Product("Test", "Test Desc", 999.99, 10)
    assert p.name == "Test"
    assert p.description == "Test Desc"
    assert p.price == 999.99
    assert p.quantity == 10


def test_category_initialization() -> None:
    """Проверяет корректную инициализацию категории и подсчёт количества."""
    p1 = Product("Item 1", "Desc 1", 100.0, 1)
    p2 = Product("Item 2", "Desc 2", 200.0, 2)
    start_cat_count = Category.category_count
    start_prod_count = Category.product_count

    c = Category("TestCat", "Testing", [p1, p2])
    assert c.name == "TestCat"
    assert c.description == "Testing"
    assert len(c.products) == 2
    assert Category.category_count == start_cat_count + 1
    assert Category.product_count == start_prod_count + 2
