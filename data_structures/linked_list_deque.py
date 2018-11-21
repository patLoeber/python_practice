from doubly_linked_base import DoublyLinkedBase, Empty

class LinkedDeque(DoublyLinkedBase):
    # double ended queue implementation based on a doubly linked list
    def first(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise('deque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('deque is empty')
        self._delete_node(self._header._next)

    def delete_last(self):
        if self.is_empty():
            raise Empty('deque is empty')
        self._delete_node(self._trailer._prev)

d = LinkedDeque()
d.insert_first(1)
d.insert_first(2)
print(d)
d.insert_last(3)
print(d)
d.delete_first()
print(d)
d.delete_last()
print(d)