
class Queue:
    def __init__(self):
        self.arr = []

    def pop(self):
        return self.arr.pop(0)

    def top(self):
        return self.arr[0]

    def push(self, item):
        self.arr.append(item)


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.top())
print(queue.pop())
print(queue.top())
