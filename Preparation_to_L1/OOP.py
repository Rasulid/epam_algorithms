# class Class:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         pass
#
#     def see(self):
#         return "something"
#
#     def find(self):
#         return "find old person"
#
#     def stend_up(self):
#         return "stend up"
#
#     def get_info(self):
#         return self.name, self.age
#
#
# obj = Class("Johon", 16)
# print(obj.see())
# print(obj.find())
# print(obj.get_info())


def star_triangle(r):
    for x in range(r):
        print(' ' * (r - x - 1) + '*' * (2 * x + 1))


star_triangle(7)
