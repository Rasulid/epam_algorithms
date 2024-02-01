# import time
# from typing import List
#
#
# def dec(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         stop = time.perf_counter()
#         print(f'Function {func.__name__} took {stop - start} seconds')
#         return result
#
#     return wrapper
#
#
# @dec
# def test_func(items):
#     print(items)
#
#
# decorated_test_func = dec(test_func)
#
#
# # decorated_test_func(1)
#
# # algorithm
#
#
# def extract_integers(lst: list) -> List[int]:
#     result = []
#
#     for x in lst:
#         if isinstance(x, int):
#             result.append(x)
#         elif isinstance(x, list):
#             result.extend(extract_integers(x))
#
#     return result
#
#
# nested_list = [[1, [[[[[6, [[[4, 5, [[[[[4, [[[[[[32]]]]]]]]]]]]]]]]]]]]]
#
#
# # flattened_list = extract_integers(nested_list)
# # print(flattened_list)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):  # equal
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):  # hash the value
#         return hash((self.x, self.y))
#
#
# # Usage
# # p1 = Point(1, 2)
# # p2 = Point(1, 2)
# # p3 = Point(3, 4)
#
#
# # print(hash(p1))  # Output: <hash value>
# # print(hash(p2))  # Output: <same hash value as p1>
# # print(hash(p3))  # Output: <different hash value>
#
# # generator
# def countdown(*n):
#     while len(n) > 0:
#         yield n
#
#
# l = [1, 2, 3, 4, 5, 6]
#
#
# # Using the generator
# # for i in countdown(l):
# #     print(i)
#
#
# # iterator
#
# # someList = [1, 2, 3, 4, 5]
# # myIterator = iter(someList)
# #
# # print(next(myIterator))
# # print(next(myIterator))
# # print(next(myIterator))
# # print(next(myIterator))
# # print(next(myIterator))
# # print(next(myIterator))  # StopIteration
#
#
# def decor(func):
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         stop = time.perf_counter()
#         print(f"the decorator {func.__name__} and took {stop - start} seconds")
#
#         return result
#
#     return wrapper
#
#
# @decor
# def test_func(num):
#     print(num)
#
#
# # test_func(2)
#
#
# class Bird:
#     def fly(self):
#         pass
#
#
# class Sparrow(Bird):
#     def fly(self):
#         print("Sparrow is flying")
#
#
# class Penguin(Bird):
#     def fly(self):
#         print("Penguin can't fly")
#
#
# def make_bird_fly(bird: Bird):
#     bird.fly()
#
# 
# # Пример использования
#
# sparrow = Sparrow()
# penguin = Penguin()
#
# make_bird_fly(sparrow)  # Работает корректно, так как Sparrow - подтип Bird
# make_bird_fly(penguin)  # Тоже работает корректно, хотя Penguin не может летать
