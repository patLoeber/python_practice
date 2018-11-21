class Empty(Exception):
    pass

class DoublyLinkedBase:
    # A base class providing a doubly linked list representation
    # use sentinel nodes at the beginning and end
    class _Node:

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        if self.is_empty():
            return '[]'
        string = ''
        current = self._header._next
        while current is not self._trailer:
            string += str(current._element) + ' '
            current = current._next
        string = string[:len(string)-1]
        return '[' + string + ']'

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element = node._prev = node._next = None
        return element
