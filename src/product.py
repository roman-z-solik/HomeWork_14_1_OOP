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
        self.__price = price
        self.quantity = quantity


    # @classmethod
    # def new_product(cls, name, description, price, quantity):
    #     new_product = cls(name, description, price, quantity)
    #     products = Category.products
    #     for item in products:
    #         return new_product
    #
    # @property
    # def price(self):
    #     return self.__price
    #
    #
    # @price.setter
    # def price(self, new_price) -> property | None:
    #     if new_price <= 0:
    #         print(f'Цена не должна быть нулевая или отрицательная')
    #     else:
    #         Product.price = new_price


if __name__ == '__main__':
        product1 = Product('Xiaomi Redmi Note 12', '1024GB, Черный', '29000', 15)
        product2 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                            180000, 5)

        print(product1.name)
        print(product1.description)
        print(product1.price)
        print(product1.quantity)

        product3 = Product.new_product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
                            180000, 5)

        print(product2.name)
        print(product2.description)
        print(product2.price)
        print(product2.quantity)

        product2.price = 150000

        print(product2.name)
        print(product2.description)
        print(product2.price)
        print(product2.quantity)
