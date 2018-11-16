class Empty(Exception):
    pass


class ArrayStack:
    # LIFO stack implementation using a Python list as underlying storage

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return repr(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()


a = ArrayStack()
a.push(1)
a.push(2)
print("S = ", a)
print("top: ", a.top())
print("stack size: ", len(a))
print("pop: ", a.pop())
print("stack size: ", len(a))
