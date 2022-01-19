class Product:
    name: str
    article: int
    price: int
    productURL: str
    count: int

    def __init__(self, name: str, article: int, price: int, productURL: str, count: int):
        self.productURL = productURL
        self.count = count
        self.name = name
        self.article = article
        self.price = price

    def get_name(self): return self.name
    def set_name(self, name: str): self.name = name

    def get_article(self): return self.article
    def set_article(self, article: int): self.article = article

    def get_price(self): return self.price
    def set_price(self, price: int): self.price = price

    def get_product_url(self): return self.productURL
    def set_product_url(self, productURL: str): self.productURL = productURL

    def get_count(self): return self.count
    def set_count(self, count: int): self.count = count
