class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
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


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
                         [product1, product2, product3])
    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(category1.category_count)
    print(category1.product_count)