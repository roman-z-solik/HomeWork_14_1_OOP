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

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            user_input = input("Новая цена ниже. Заменить цену?(Y): ")
            if (
                user_input == "Y"
                or user_input == "y"
                or user_input == "Н"
                or user_input == "н"
            ):
                self.__price = new_price
            else:
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, parameters_list: dict):
        product = Product
        product.name = parameters_list["name"]
        product.description = parameters_list["description"]
        product.price = parameters_list["price"]
        product.quantity = parameters_list["quantity"]
        return product


    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))


