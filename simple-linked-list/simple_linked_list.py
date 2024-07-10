class Node:
    def __init__(self, value, next = None):
        self._next = next
        self._value = value

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._head = None
        self._count = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self._count

    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        else:
            return self._head

    def push(self, value):
        self._head = Node(value, self._head)
        self._count += 1

    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")
        else:
            actual_node = self.head()
            self._count -= 1
            self._head = actual_node.next()
            return actual_node.value()

    def reversed(self):
        return LinkedList(self)

    def __iter__(self):
        node = self._head
        while node is not None:
            yield node.value()
            node = node.next()


class EmptyListException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
