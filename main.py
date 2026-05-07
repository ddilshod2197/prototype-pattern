class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.new_product()
        self.builder.add_parts()
        self.builder.pack_product()
        self.builder.product_price()


class Builder:
    def new_product(self):
        pass

    def add_parts(self):
        pass

    def pack_product(self):
        pass

    def product_price(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def new_product(self):
        self.product = Product()

    def add_parts(self):
        self.product.add_part("Part 1")
        self.product.add_part("Part 2")

    def pack_product(self):
        self.product.pack()

    def product_price(self):
        self.product.set_price(100)


class Product:
    def __init__(self):
        self.parts = []
        self.packed = False
        self.price = 0

    def add_part(self, part):
        self.parts.append(part)

    def pack(self):
        self.packed = True

    def set_price(self, price):
        self.price = price


# Builder pattern nima?
director = Director()
builder = ConcreteBuilder()
director.set_builder(builder)
director.construct()

print("Product parts:", builder.product.parts)
print("Product packed:", builder.product.packed)
print("Product price:", builder.product.price)
```

Kodda Builder patterni quyidagicha ishlatiladi:

1. `Director` klassi direktor rolini o'ynaydi. U builder klassini tanlaydi va construct metodini chaqiradi.
2. `Builder` klassi builder rolini o'ynaydi. U yangi mahsulot yaratish, qismlarni qo'shish, mahsulotni paketlash va mahsulot narxini belgilash uchun metodlarni taqdim etadi.
3. `ConcreteBuilder` klassi konkret builder klassidir. U yangi mahsulot yaratish, qismlarni qo'shish, mahsulotni paketlash va mahsulot narxini belgilash uchun metodlarni implement etadi.
4. `Product` klassi mahsulot rolini o'ynaydi. U qismlarni qo'shish, mahsulotni paketlash va mahsulot narxini belgilash uchun metodlarni taqdim etadi.

Builder pattern direktor klassi orqali builder klassini tanlaydi va construct metodini chaqiradi. Builder klassi yangi mahsulot yaratish, qismlarni qo'shish, mahsulotni paketlash va mahsulot narxini belgilash uchun metodlarni taqdim etadi. Konkret builder klassi konkret mahsulot yaratish, qismlarni qo'shish, mahsulotni paketlash va mahsulot narxini belgilash uchun metodlarni implement etadi.
