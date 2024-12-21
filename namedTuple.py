from collections import namedtuple

class Product(namedtuple('Product', ['id', 'name', 'price'])):
    def apply_discount(self, discount_percentage):
        discounted_price = self.price * (1 - discount_percentage / 100)
        return f"Discounted Price: {discounted_price:.2f}"

class User(namedtuple('User', ['id', 'username', 'email'])):
    def is_valid_email(self):
        return "@" in self.email and "." in self.email

product = Product(id=1, name="Laptop", price=1500)
user = User(id=101, username="diyorbek", email="diyorbek@example.com")

print(product.apply_discount(10))  
print(user.is_valid_email())
