class Empty(Exception):
    pass


class LinkedListQueueCircular():
    # queue implementation using a circular linked list for storage
    # use a tail pointer that points to the first element in the queue
    # implement a rotate method that rotates the front element to the back of the queue
    class _Node():
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return '[]'
        string = ''
        current = self._tail._next
        for i in range(self._size):
            string += str(current._element) + ' '
            current = current._next
        string = string[:len(string)-1]
        return '[' + string + ']'

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        new = self._Node(e, None)
        if self.is_empty():
            new._next = new
        else:
            new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1

    def rotate(self):
        # rotate front element to the back of the queue
        if self._size > 0:
            self._tail = self._tail._next


q = LinkedListQueueCircular()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
d = q.dequeue()
print('dequeue:', d)
print(q)
print('rotate...')
q.rotate()
print(q)
q.enqueue(5)
print(q)
d = q.dequeue()
print('dequeue:', d)
f = q.first()
print('first:', f)
print(q)

