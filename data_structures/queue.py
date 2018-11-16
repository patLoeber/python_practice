class Empty(Exception):
    pass


class ArrayQueue:
    # FIFO queue implementation using a Python list as underlying storage
    # implementation with a circular array -> use read(front) and write(back) index
    # classic array with pop(0) would be inefficient, as this is O(n) because of required shifting
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0  # read index

    def __len__(self):
        return self._size

    def __str__(self):
        return repr(self._data)

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def dequeue(self):
        # update read index
        if self.is_empty():
            raise Empty('queue is empty')
        e = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        return e

    def enqueue(self, e):
        # update write index
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        write = (self._front + self._size) % len(self._data)
        self._data[write] = e
        self._size += 1

    def _resize(self, capacity):
        tmp = [None] * capacity
        walk = self._front
        for i in range(self._size):
            tmp[i] = self._data[walk]
            walk = (walk + 1) % len(self._data)
        self._data = tmp
        self._front = 0


q = ArrayQueue()
print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
for i in range(4,10):
    q.enqueue(i)
print(q)
q.dequeue()
q.dequeue()
print(q)
print(len(q))
for i in range(10, 14):
    q.enqueue(i)
print(q)
q.dequeue()
print(q)
q.enqueue(14)
q.enqueue(15)
print(q)
print(len(q))
