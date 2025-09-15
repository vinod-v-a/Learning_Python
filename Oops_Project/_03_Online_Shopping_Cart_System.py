from abc import ABC, abstractmethod


class Items:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price


class Discount(ABC):
    @abstractmethod
    def apply_discount(self,total):
        pass


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage  # e.g., 10 for 10%

    def apply_discount(self, total):
        discount_amount = total * (self.percentage / 100)
        return total - discount_amount
class FixedDiscount(Discount):

    def __init__(self, amount):
        self.amount = amount  # Fixed amount to subtract

    def apply_discount(self, total):
        return max(0, total - self.amount)
