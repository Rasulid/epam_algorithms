# def binary_serch(list_s, item):
#     low = 0
#     high = len(list_s) - 1
#
#     while low <= high:
#         mid = (low + high)
#         guess = list_s[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid
#         else:
#             low = mid + 1
#     return None


def binary_search(list_s, item):
    low = 0
    high = len(list_s) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_s[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(my_list, 9))
