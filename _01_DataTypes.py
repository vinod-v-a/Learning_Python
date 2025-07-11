# Data Types
x = 10
y = 28.0
z = "King"
print(x,    type(x))
print(y,    type(y))
print(z,    type(z))

# List
a = [1, 2, 3, "Abc"]
print(a,    type(a))
# Create List using constructor
b = list([9, 8, 7, 6])
print(b,    type(b))

# Adding Elements into List
# append(): Adds an element at the end of the list
a.append("Raj")
print(a)
# insert( insert index ,inset value): Adds an element at a specific position.
a.insert(0,"king")
print(a)
# extend(): Adds multiple elements to the end of the list.
a.extend([2, 3, 4])
print(a)
# Updating Elements into List
a[0] = 0
print(a)

# Removing Elements from List
# remove(): Removes the first occurrence of an element.
a.remove(2)
print(a)


# pop(): Removes the element at a specific index or the last element if no index is specified.
a. pop(4)
print(a)
a.pop()
print(a)

# del statement: Deletes an element at a specified index.
del a[3]
print(a)

# Iterating Over Lists

for i in a:
    print(i)

# Get list as input Using for loop
c = []

# n = int(input("Enter no of  Elements :"))
#
# for i in range(n):
#     element = input(f"Enter the element {i+1}:")
#     c.append(element)
# print("List : ", c)


# Get list as input Using map()
# user_input = list(map(int, input("Enter number :").split()))
# print("list :", user_input)

# Create List using range()
r1 = 0
r2 = 10
l1 = list(range(r1, r2))
print(l1)