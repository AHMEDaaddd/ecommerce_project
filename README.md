# E-commerce Project Core

Это учебный проект — ядро e-commerce системы на основе ООП.

## Реализовано:
- Классы `Product` и `Category`
- Подсчёт количества категорий и продуктов
- Загрузка данных из JSON
- Покрытие тестами (pytest)
- Настройка линтеров: flake8, black, isort, mypy

## Запуск тестов:
```bash
poetry install
poetry run pytest --cov=src
```

## Загрузка данных:
```python
from src.loader import load_categories_from_json
cats = load_categories_from_json("products.json")
```