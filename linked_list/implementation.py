from .interface import AbstractLinkedList
from. node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        if elements:
            for e in elements:
                self.append(e)

    def __str__(self):
        elem_list = []
        if self.start is None:
            return '[]'
        else:
            pseudo_start = self.start
            while pseudo_start is not None:
                elem_list.append(pseudo_start.elem)
                pseudo_start = pseudo_start.next
            str_list = str(elem_list)
            return str_list

    def __len__(self):
        return self.count()

    def __iter__(self):
        pass

    def __getitem__(self, index):
        if self.start is None or index < 0 or index > self.count() - 1:
            raise IndexError
        c = 0
        pseudo_start = self.start
        while c != index:
            pseudo_start = pseudo_start.next
            c = c + 1
        return pseudo_start.elem

    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        if self.count() == other.count():
            pseudo_start1 = self.start
            pseudo_start2 = other.start
            while pseudo_start1 is not None:
                if pseudo_start1.elem != pseudo_start2.elem:
                    return False
                pseudo_start1 = pseudo_start1.next
                pseudo_start2 = pseudo_start2.next

            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def append(self, elem):
        node_added = Node(elem)
        if self.start is None:
            self.start = node_added
            self.end = node_added
        else:
            self.end.next = node_added
            self.end = node_added

    def count(self):
        pseudo_start = self.start
        pseudo_end = self.end
        if pseudo_start is None:
            return 0

        nodes_counted = 1
        while (pseudo_start != pseudo_end):
            pseudo_start = pseudo_start.next
            nodes_counted += 1
        return nodes_counted

    def pop(self, index=None):
        c = self.count()
        if c == 0 or index is not None and (index < 0 or index > c - 1):
            raise IndexError
        if c == 1:
            del_node = self.start
            self.start = None
            self.end = None
            return del_node.elem

        if index is None or index == c - 1:
            del_node = self.end
            pseudo_start = self.start
            while pseudo_start.next != self.end:
                pseudo_start = pseudo_start.next
            pseudo_start.next = None
            self.end = pseudo_start
            return del_node.elem
        if index == 0:
            del_node = self.start
            self.start = self.start.next
            del_node.next = None
            return del_node.elem
        else:
            c = 0
            pseudo_start = self.start
            pseudo_prev = self.start
            while c != index:
                pseudo_prev = pseudo_start
                pseudo_start = pseudo_start.next
                c += 1
            del_node = pseudo_start
            pseudo_prev.next = pseudo_start.next
            del_node.next = None
            return del_node.elem
