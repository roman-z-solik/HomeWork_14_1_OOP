class Category:
    """
    Класс Category обладает следующими свойствами:
        название (name),
        описание (description),
        список товаров категории (products).
    """

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0