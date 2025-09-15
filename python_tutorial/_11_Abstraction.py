"""
abstraction:
hiding the implementation details
focusing on what needs to be implemented rather than how it is implemented

from abc import ABC, abstractmethod
"""

from abc import ABC , abstractmethod
#
class Login(ABC):
    @abstractmethod
    def login_meth(self):
        return "login "
class Order(Login):
    def order_meth(self):
        return "Order Class order_meth "
    def login_meth(self):
        return "login_meth from order class"

class Payment(Login):
    def payment_meth(self):
        return "payment_meth from Payment Class"
    def login_meth(self):
        return "login_meth from payment Class"

o_obj = Order()
print(o_obj.order_meth())
print(o_obj.login_meth())

p_obj = Payment()
print(p_obj.payment_meth())
print(p_obj.login_meth())


"==============  Singleton Pattern ==========================="


# class ControlTower:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             print("Initialize Control Tower!")
#         return cls._instance
#
#     # def __init__(self):
#     #     print("Initialize Control Tower!")
#
#
# tower1 = ControlTower()
# tower2 = ControlTower()
# print(tower1)
# print(tower2)
# tower3 = ControlTower()
# print(tower1 is tower2)
# print(tower2 is tower3)

