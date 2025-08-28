"============= Polymorphism =========================="


# class ParentClass:
#     def meth(self):
#         return "from ParentClass"
#
#     def an_meth(self):
#         pass
#
#
# class ChildClass(ParentClass):
#     def ch_meth(self):
#         pass
#
#     def meth(self):
#         return "from ChildClass"
#
#
# obj = ChildClass()
# print(obj.meth())
# print(obj.an_meth())


# obj2 = ParentClass()
# print(obj2.meth())


"================= method overriding ==================="
# class Animal:
#     def sound(self):
#         return "Animal makes sounds"
#     def sleep(self):
#         return "Animal sleeps"
#
# class Dog(Animal):
#     def sound(self):
#         return "dog barks"
#
# class Lion(Animal):
#     def sound(self):
#         return "Lion roars"
#
# an_obj = Animal()
# print(an_obj.sound())
# print(an_obj.sleep())
#
# dog_obj = Dog()
# print(dog_obj.sound())
# print(dog_obj.sleep())
#
# lion_obj = Lion()
# print(lion_obj.sound())
# print(lion_obj.sleep())

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# class Vehicle:
#     def wheels(self):
#         return "Vehicle wheels"
#     def fuel(self):
#         return "Vehicle fuel"
#
# class Bike(Vehicle):
#     def wheels(self):
#         return "Bike wheels"
#     def fuel(self):
#         return "Bike fuel"
#
# v_obj = Vehicle()
# print(v_obj.wheels())
# print(v_obj.fuel())
# b_obj = Bike()
# print(b_obj.wheels())
# print(b_obj.fuel())


"===================== method overloading ===================="

# class Employee:
#     def get_emp_data(self,name,*args,sal=25000,**kwargs):
#         return f"{name}{args}{sal}{kwargs}"
#
#
# e_obj = Employee()
# print(e_obj.get_emp_data("Raj"))
# print(e_obj.get_emp_data("Raj",10,20,))
# print(e_obj.get_emp_data("Raj",10,20,sal = 50000))
# print(e_obj.get_emp_data("Raj",10,20,sal = 50000,loc='Bangalore'))

"============= constructor overloading =================="

# class Employee:
#     def __init__(self, name, *args, sal=25000, **kwargs):
#         self.name = name
#         self.args = args
#         self.sal = sal
#         self.kwargs = kwargs
#
# obj = Employee("ramesh")
# obj = Employee("ramesh", 10)
# obj = Employee("ramesh", 10, sal=20000)
# obj = Employee("ramesh", 10, sal=20000, loc="Bangalore")
# print(obj)


"dunder methods, magic methods, special methods"

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age =age
    # def __str__(self):
    #     return f"Student object has been created with name = {self.name} and age = {self.age}"
    def __repr__(self):
        return f"Student(name = {self.name},age = {self.age})"

s_obj = Student("raj",35)
print(s_obj)


"__new__, __init__"

class Laptop:
    def __new__(cls, *args, **kwargs):
        print("Chair __new__")
        inst = super().__new__(cls)
        print(inst)
        return inst
    def __init__(self,name):
        print("From __init__")
        self.name = name


c_obj = Laptop("HP")
