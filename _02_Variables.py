# Variable
# name = "Raj"
# age = 25
# sal = 35000.00
#
# print(name, type(name))
# print(age, type(age))
# print(sal, type(sal))
#
# import keyword
# print(keyword.kwlist)


# immutable - int float complex bool None str tuple - CRD

# x = 10
# y = 10
# x = 20
# print(id(x))
# print(id(y))



# x = 15.00
# y = 15.00
# x = 20.00
# print(id(x))
# print(id(y))

# x = 5j
# y = 5j
# x = 15j
# print(id(x))
# print(id(y))

# x = True
# y = True
# x = False
# print(id(x))
# print(id(y))

# x = "Raj"
# y = "Raj"
# x = "Sam"
# print(id(x))
# print(id(y))


# x = (1,2,3,4)
# y = (1,2,3,4)
# x = (5,6,7)
# print(id(x))
# print(id(y))


# mutable   - list set dict- CRUD
# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# # l1 = [4,5,6]
# print(id(l1))
# print(id(l2))

# s1 = {1,2,3}
# s2 ={1,2,3}
# print(id(s1))
# print(id(s2))


# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'a': 1, 'b': 2, 'c': 3}
# print(id(d1))
# print(id(d2))

# non-iterable -int, float, complex, bool, None

# a, b, c = 123
# print(a,b,c) # TypeError: cannot unpack non-iterable int object

# a,b = 50.00
# print(a,b) #TypeError: cannot unpack non-iterable float object

# a, b = 4j
# print(a, b) #TypeError: cannot unpack non-iterable float object

# a, b, c = True
# print(a, b, c) #TypeError: cannot unpack non-iterable bool object



# iterable - str, list, tuple, set. dict
# set - unordered

# a,b,c ="Raj"
# print(a,b,c)
# x, y, z = "Rahul"
# print(x, y, z) #ValueError: too many values to unpack (expected 3)

# a, b, c = [10, 20, 30]
# print(a, b, c)

# a, b, c = {1,2,3}
# print(a,b,c)

# x, y, z = {1: "raj", 2: "sam", 3: "pam"}
# print(x,  y, z)

# a = b = c = 100
# print(id(a))
# print(id(b))
# print(id(c))
#
# x= 10,20,30
# print(x, type(x))


#   "LEGB"

from math import pi

print(pi)
pi = "GLOBAL SCOPE"
# print(pi)
def outer():
    pi = "ENCLOSED SPACE"
    # print(pi)
    def inner ():
        # pi = "LOCAL SPACE"
        print(pi)
    return inner()
outer()


