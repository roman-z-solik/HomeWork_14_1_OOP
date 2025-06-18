from src.product import Product

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
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


    @property
    def products(self) -> None:
        products_str = ''
        for output_product in self.__products:
            products_str += (f'{output_product.name}, {output_product.price} руб. Остаток:'
                             f' {output_product.quantity} шт.\n')
        return products_str


    @products.setter
    def products(self, new_product: Product):
        pass
    #     for product1 in self.__products:
    #         if new_product == product1:
    #             print('Есть такой')
    #             if new_product.price < product1.price:
    #                 product1.quantity += new_product.quantity
    #             else:
    #                 product1.quantity += new_product.quantity
    #                 product1.price = new_product.price
    #         else:
    #             print('Нет такого')
    #             self.__products.append(product1)
    #     Category.product_count += 1


    def add_product(self, adding_product: Product):
        self.__products.append(adding_product)



# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     # print(product1.name)
#     # print(product1.description)
#     # print(product1.price)
#     # print(product1.quantity)
#     #
#     # print(product2.name)
#     # print(product2.description)
#     # print(product2.price)
#     # print(product2.quantity)
#     #
#     # print(product3.name)
#     # print(product3.description)
#     # print(product3.price)
#     # print(product3.quantity)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     # print(category1.name == "Смартфоны")
#     # print(category1.description)
#     # print(category1.products)
#     # print(category1.category_count)
#     # print(category1.product_count)
#
#     category1.products = Product.new_product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера",
#                             180000, 5)
#     print(category1.products)
#     # print(category1.category_count)
#     # print(category1.product_count)