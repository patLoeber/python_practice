class Empty(Exception):
    pass


class LinkedListStack:
    # LIFO stack implementation using a singly linked list for storage
	# Top of the stack is the head of the list

    class _Node:
        #__slots__ = 'element', 'next'
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
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

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        first = self._head._element
        self._head = self._head._next
        self._size -= 1
        return first


l = LinkedListStack()
l.push(1)
l.push(2)
l.push(3)
print(l)
a = l.pop()
print(a)