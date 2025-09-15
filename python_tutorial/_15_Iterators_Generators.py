"===================== iterators ==========================="

"Print iterators using for loop"
# ls = [10,20,30]
#
# ls_iter = iter(ls)
# print(ls_iter,type(ls_iter))
# for each in ls_iter:
#     print(each)

"Print using __next__()"
    # ls2 = [10,40,50]
    # ls2_iter = iter(ls2)
    #
    # print(ls2_iter.__next__())
    # print(ls2_iter.__next__())
    # print(ls2_iter.__next__())
    # print(ls2_iter.__next__())      # StopIteration

" checking ID of iterators"
# ls = [10, 20, 30]

# itr_ls = iter(ls)
# print(id(itr_ls))  # 2672325824464
# itr_ls_2 = iter(itr_ls)
# print(id(itr_ls_2)) # 2672325824464

"""
class CustomIterator:

    def __iter__(self):
        return self

    def __next__(self):
        # business logic

"""


# class RangeIterator:
#     def __init__(self,start,stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         curr = self.start
#         if self.start >= self.stop:
#             raise StopIteration
#         self.start += 1
#         return curr
#
# obj = RangeIterator(5, 10)
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

# for _ in range(5):
#     print(obj.__next__())


"===================== generators ==============================="

# def check():
#     print("~" * 5)
#     yield 10
#     print("+" * 5)
#     yield 20
#     print("=" * 5)
#     yield 30
# x  = check()
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) # StopIteration


# def func(num):
#     for each in range(num):
#         yield each
#         print("*"*20)
#
#
# res = func(5)
# print(res)
# for _ in range(5):
#     print(next(res))


# def range_gen(start,stop):
#     while start<stop:
#         yield start
#         start+= 1
#
# res = range_gen(5,10)
# for _ in range(5):
#     print(next(res))