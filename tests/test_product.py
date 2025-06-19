from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_create():
    test_product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    test_product.name = "Iphone 15"
    test_product.description = "512GB, Gray space"
    test_product.price = 210000.0
    test_product.quantity = 8


def test_product_update(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
