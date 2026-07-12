class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock

    def get_stock(self):
        return self.__stock
    
    def reduct_stock(self, amount):
        if amount > self.__stock:
            return False
        self.__stock -= amount
        return True
    
    def __str__(self):
        return f"[{self.product_id}] {self.name} | قیمت: {self.price} تومان | موجودی: {self.__stock} عدد"
    
class Store:
    def __init__(self, name):
        self.name = name
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)
        print(f"✅ '{product.name}' به فروشگاه اضافه شد!")

    def show_products(self):
        if len(self.__products) == 0:
            print("⚠️ هیچ محصولی ثبت نشده!")
            return
        print(f"\n--- موجودی فروشگاه {self.name} ---")
        for product in self.__products:
            print(product)

    def find_product(self, product_id):
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def buy_product(self, product_id, amount):
        product = self.find_product(product_id)
        if not product:
            print("❌ محصول پیدا نشد!")
            return
        if product.reduct_stock(amount):
            total = product.price * amount
            print(f"✅ {amount} عدد '{product.name}' خریداری شد!")
            print(f"💰 مبلغ کل: {total} تومان")
        else:
            print(f"❌ موجودی کافی نیست! موجودی فعلی: {product.get_stock()} عدد")

    def __str__(self):
        return f"🏪 فروشگاه {self.name} | تعداد محصولات: {len(self.__products)}"

Store = Store("مبلمان Pouya")
print(Store)


Store.add_product(Product(1, "مبل راحتی", 5000000, 10))
Store.add_product(Product(2, "میز ناهارخوری", 3000000, 5))
Store.add_product(Product(3, "تخت خواب", 8000000, 3))
Store.add_product(Product(4, "صندلی اداری", 2000000, 15))


Store.show_products()


print("\n--- خرید ---")
Store.buy_product(1, 3)   # خرید ۳ مبل
Store.buy_product(3, 5)   # موجودی کافی نیست
Store.buy_product(9, 1)   # محصول پیدا نشد


Store.show_products()