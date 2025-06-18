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