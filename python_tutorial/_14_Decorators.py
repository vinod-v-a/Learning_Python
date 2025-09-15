"""Decorator is a design pattern that allows you to dynamically alter the functionality of a
      function, method, or class by wrapping them with another function"""

"============Function Decorators using print()============="

# def decor(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("modification")
#     return wrapper
#
# @decor
# def hello():
#     print("print hello")
#
# hello()


"================= Function Decorators using return ============"

# def decor(func):
#     def wrapper():
#         bef = "Before Function call"
#         res = func()
#         aft = "Modification "
#         return bef, res, aft
#
#     return wrapper
#
#
# @decor
# def hello():
#     return "Hello Function"
#
#
# print(hello())


"===================== Check age ==============================="

# def decor(func):
#     def wrapper(wr_age):
#         if not isinstance(wr_age, int) or wr_age < 0:
#             return "Provide a valid age"
#         res = func(wr_age)
#         return res
#
#     return wrapper
#
#
#
# @decor
# def check_age(age):
#     if age > 18:
#         return "major"
#     return "minor"
#
#
# print(check_age(8))
# print(check_age(20))
# print(check_age("a"))
# print(check_age(-8))

"===================== Parameterized Decorator (also known as decorator factory) ===================="

# def outer(num):
#
#     def decor(func):
#         def wrapper(*args,**kwargs):
#             bef = "Befor call of function"
#             res = func(*args,**kwargs)
#             aft = "Modification"
#             return bef,res,aft,num
#         return wrapper
#     return decor
#
# @outer(100)
# def hello():
#     return "hello method"
#
# @outer(100)
# def bye(x):
#     return f"bye Method :{x}"
#
# print(hello())
# print(bye("python"))


"================== Class-based function decorator ========================================"
# class DecoratorClass:
#     def __init__(self,func):
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         return "from _call_",self.func()
#
#
#
# @DecoratorClass
# def hello():
#     return "Hello Method"
# print(hello())

"=============== Function-based class decorator ====================="

# def decor(classs):
#     class WrapperClass(classs):
#         def wrap_meth(self):
#             return "from Wrap_meth"
#     return WrapperClass
#
#
# @decor
# class ClassName:
#     def inst_method(self):
#         return "From ClassName ins_method"
#
# obj = ClassName()
# print(obj.inst_method())
# print(obj.wrap_meth())

# x = [i**2 for i in range(4)]
# print(sum(x))
# print(sum(x))

# def func(val,res=[]):
#     res.append(val)
#     return res
# print(func(10))
# print(func(20,[]))
# print(func(30))
# print(func(40,[]))
# print(func(40,))
# from abc import ABC,abstractmethod




"======================================"


def decor(func):
    def wrapper(self):
        res = func(self)
        out = res.upper()
        return res,out

    return wrapper

@decor
def hello(x):
    return x

print(hello("hello"))