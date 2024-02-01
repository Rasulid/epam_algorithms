# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# def has_cycle(node):
#     slow = node
#     fast = node
#     while fast is not None and fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next
#
#         if slow == fast:
#             return True
#     return False
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node2
#
# result = has_cycle(node1)
# print("Есть цикл" if result else "Нет цикла"

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, pointer_to_next_lem=None):
        self.val = val
        self.next = pointer_to_next_lem


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head

    while cur:
        next_elem = cur.next

        cur.next = prev

        prev = cur
        cur = next_elem

    return prev


class Solution:
    pass

#     None < - 1 < - 2 - 3 - 4
# prev |
# cur  |
# next |


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Создание связанного списка
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

# Вывод на экран диаграммы связанного списка
llist.display()
