class Product:
    """
    Класс Product обладает следующими свойствами:
        название (name),
        описание (description),
        цена (price),
        количество в наличии (quantity)
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # @property
    # def price(self):
    #     return self.__price

    @classmethod
    def new_product(cls, parameters_list: dict):
        product = Product
        product.name = parameters_list['name']
        product.description = parameters_list['description']
        product.price = parameters_list['price']
        product.quantity = parameters_list['quantity']
        return product


if __name__ == "__main__":
    product1 = Product("Xiaomi Redmi Note 12", "1024GB, Черный", "29000", 15)
    product2 = Product(
        "Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000, 5
    )

    # print(product1.name)
    # print(product1.description)
    # print(product1.price)
    # print(product1.quantity)

    product3 = Product.new_product(
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера',
         'price': 180000, 'quantity': 5}
    )

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # product2.price = 150000
    #
    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
