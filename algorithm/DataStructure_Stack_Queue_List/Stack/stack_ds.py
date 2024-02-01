#
# class Stack:
#
#     def __init__(self):
#         self.arr = []
#
#     def is_empty(self):
#         return self.arr == []
#
#     def top(self):
#         return self.arr[-1]
#
#     def push(self, item):
#         self.arr.append(item)
#
#     def pop_(self):
#         return self.arr.pop()
#
#     def size(self):
#         return len(self.arr)
#
#
# stack = Stack()
#
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
#
#
# print("top", stack.top())
# print("pop", stack.pop_())
# print("size", stack.size())
# print("top", stack.top())
# print("is_empty", stack.is_empty())


class Stack:
    def __init__(self):
        self.arr = []

    def push(self, item):
        self.arr.append(item)

    def pop(self):
        return self.arr.pop()

    def top(self):
        return self.arr[-1]

    def isEmpty(self):
        return self.arr == []


pair_map = {'{': '}', '[': ']', '(': ')'}
open_brackets = {'{', '[', '('}


def isOpen(ch: str):
    return ch in open_brackets


def isPair(open_s: str, close: str):
    return pair_map.get(open_s) == close


def isValid(string: str) -> bool:
    stack = Stack()

    for char in string:
        if char in open_brackets:
            stack.push(char)
        else:
            if not stack.isEmpty() and isPair(stack.top(), char):
                stack.pop()
            else:
                return False

    return stack.isEmpty()


class Solution:
    pass


s = "{[]}"

sol = Solution()

print(isValid(s))
