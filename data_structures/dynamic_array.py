import ctypes

class DynamicArray:
    # a dynamic array without the build-in list class
    # support raw data with ctypes module

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._n

    def __str__(self):
        if self.is_empty():
            return '[]'
        return '[' + ' '.join(str(self._A[k]) for k in range(self._n)) + ']'

    def __getitem__(self, index):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        return self._A[index]

    def is_empty(self):
        return self._n == 0

    def append(self, item):
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        self._A[self._n] = item
        self._n += 1

    def insert(self, index, item):
        if not 0 <= index <= self._n:
            raise IndexError('invalid index')
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for k in range(self._n, index, -1):
            self._A[k] = self._A[k-1]
        self._A[index] = item
        self._n += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError('nothing to pop')
        last_item = self._A[self._n - 1]
        self._A[self._n - 1] = None  # help garbage collection
        self._n -= 1
        if self._n <= self._capacity/2:
            self._resize(int(self._capacity/2))
        return last_item

    def delete(self, index):
        if not 0 <= index < self._n:
            raise IndexError('invalid index')
        for k in range(index, self._n - 1):
            self._A[k] = self._A[k + 1]
        self._A[self._n-1] = None
        self._n -= 1
        if self._n < self._capacity/4:
            self._resize(int(self._capacity/2))

    def remove(self, item):
        for k in range(self._n):
            if item == self._A[k]:
                for i in range(k, self._n-1):
                    self._A[i] = self._A[i+1]
                self._A[self._n-1] = None
                self._n -= 1
                if self._n < self._capacity/4:
                    self._resize(int(self._capacity/2))
                return
        raise ValueError('item not found')

    def find(self, item):
        for k in range(self._n):
            if item == self._A[k]:
                return k
        return -1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

a = DynamicArray()
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

print('\nappend 4 items...')
a.append(1)
a.append(3)
a.append(5)
a.append(4)

print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

element2 = a[2]
print('\nitem at index 2 is: ', element2)

print('\ninsert item 6 at index 1...')
a.insert(1, 6)
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

popped_item = a.pop()
print('\npopped item...: ', popped_item)
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

a.delete(2)
print('\ndelete item at index 2...')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

print('\nappend 3 items...')
a.append(1)
a.append(6)
a.append(2)

print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

a.remove(1)
print('\nremove item 1')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

a.remove(1)
print('\nremove item 1')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))


a.remove(6)
print('\nremove item 6')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

a.remove(6)
print('\nremove item 6')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))

a.remove(5)
print('\nremove item 5')
print('A = ', a)
print('length: {0}, capacity: {1}'.format(len(a), a.capacity()))
