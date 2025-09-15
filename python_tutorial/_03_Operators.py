# "Arithmetic operators"
# "+ - * / // % **"


# a = 10
# b = 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)      # Float (True division)
# print(a//b)     # int (floor division)
# print(a % b)
# print(a**b)


# a = 10
# b = "Python"
# print(a+b)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# a = "Python"
# b = "Hello "
# print(b+a)

# a = "Raj"
# b = True
# print(a + b) #TypeError: can only concatenate str (not "bool") to str


# a = [1, 3, 4]
# b = [7, 8, 9]
# print(a + b)  # Concatenation of list (only +)


# a = (1, 3, 4)
# b = (7, 8, 9)
# print(a + b)  # Concatenation of tuple

# a = {1, 3, 4}
# b = {4, 8, 9}
# print(a + b)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'


# a = {"a": 10, "b": 20}
# b = {1: "Python", 2:"Hello"}
# print(a+b) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'



# "Comparison Operator"
# "== != > < >= <="


# n1 = 5
# n2 = 10
# res = n1 < n2
# print(res)

# n1 = 7.0
# n2 = 10
# res = n1 < n2
# print(res)

# n1 = "Apple"
# n2 = "Python"
# res = n1 > n2
# print(res)
#
# n1 = [1, 2, 3]
# n2 = [10, 20, 30]
# res = n1 < n2
# print(res)

# n1 = (1, 2, 3)
# n2 = (10, 20, 30)
# res = n1 < n2
# print(res)


# n1 = {1, 2, 3}
# n2 = {10, 20, 30}
# res = n1 > n2
# print(res)  # Always False


# n1 = {"a": 1, "b": 2, "c": 3}
# n2 = {"a": 10, "y": 20, "z": 30}
# res = n1 > n2
# print(res)     # TypeError: '>' not supported between instances of 'dict' and 'dict'


# x1 = "Python"
# x2 = [50]
# res = x1 > x2
# print(res)    # TypeError: '>' not supported between instances of 'str' and 'list'

# "Logical Operators"
# "and or not - DM"

"""
p       q       p and q         p or q
-       -       -------         -------
T       T           T               T
T       F           F               T
F       T           F               T
F       F           F               F

"""

# AND

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
# print(10 and 5)
# print(5 and 10)
# print("a" and "b")
# print("b" and 100)
# print(1 and 0)
# print(0 and 1)
# print(" " and 10)
# print(10 and [])
# print(( ) and [])
# print([] and 10)

# OR
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# print(5 or 10)
# print(10 or 5)
# print("a" or "b")
# print("a" or 10)
# print(1 or 0)
# print(0 or 1)
# print("" or 10)
# print("a" or [])
# print([] or 10)
# print(() or [])


# s = "A"
# s = None
# s = 0
# s = ""
# s = []
# s = ()
# s = set()
# s = {}

# if not s:
#     print("there is no data")
# else:
#     print("data is present")


# Membership Operators ("in" / "not in")
# l1 = [10, 20, 30]
# print(10 in l1)  # True
# l2 = [10, ["python", "Welcome"], {"a", "b"}]
# print("python" in l2)    # False
# print("a" not in l2)   # True


# Assignment Operators
# x = 10
# x += 5
# x -= 5
# x *= 5
# x /= 5
# x //= 5
# x %= 5
# x **= 5
# print(x)


# Identity Operators

# immutable
# x = 10
# y = 10
# print(x == y)   # True
# print(x is y)   # True
# print(x is not y)   # False

# mutable
# x = [20, 30]
# y = [20, 30]
# print(x == y)  # True => check only values
# print(x is y)  # False => check the id of the object
# print(x is not y)   # True

# Bitwise Operators
p = 25
q = 10
print("Binary Value of p: ", bin(p))
print("Binary Value of q: ", bin(q))
# z = p & q
# z = p | q
# z = p ^ q
z = ~q
print("Binary Value of z: ", bin(z))
print("Value of z: ", z)





