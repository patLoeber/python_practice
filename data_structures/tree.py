from linked_list_queue import LinkedListQueue

class Tree:
    """Abstract base class representing a tree structure"""

    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            raise NotImplementedError('must be implemented by subclass')

    def root(self):
        """Return Position representing the root"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root. O(n) at worst"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Return the height of the subtree rooted at Position p. O(n)"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p. O(n)
        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.preorder()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p"""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            q = LinkedListQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                p = q.dequeue()
                yield p
                for c in self.children(p):
                    q.enqueue(c)

