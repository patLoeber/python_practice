class Empty(Exception):
    pass


class LinkedListQueue:
    # FIFO queue implementation using a singly linked list (with head and tail pointer) for storage
    # Front of queue = head of list, back of queue = tail of list
    class _Node():
        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return '[]'
        string = ''
        current = self._head
        while current is not None:
            string += str(current._element) + ' '
            current = current._next
        string = string[:len(string)-1]
        return '[' + string + ']'


    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('queue is empty')
        first = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return first

    def enqueue(self, e):
        new_tail = self._Node(e, None)
        if self.is_empty():
            self._head = new_tail
        else:
            self._tail._next = new_tail
        self._tail = new_tail
        self._size += 1


q = LinkedListQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
print(len(q))

