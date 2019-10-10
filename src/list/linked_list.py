from list.node import Node

class LinkedList:
    head = None
    _length = 0

    def append(self,val):
        if not self.head:
            self.head = Node(val)
            pass
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
        self._length += 1

    def insert(self, val, index = 0):
        if not self.head:
            self.head = Node(val)
        elif index == 0:
            """ Insertion at beginning """
            temp = Node(val)
            temp.next = self.head
            self.head = temp
        else:
            """ Insertion at specified index """
            temp = self.head
            while index > -1:
                prev = temp
                temp = temp.next
                index -= 1
            prev.next = Node(val)
            prev = prev.next
            prev.next = temp
        self._length += 1

    def delete(self,index):
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        temp = temp.next
        self._length -= 1

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        print("-----------------------")

    def reverse(self):
        prev = self.head
        curr = prev.next if prev else None
        nxt = curr.next if curr else None
        if not prev or not curr:
            return self.head
        elif not nxt:
            prev.next = None
            curr.next = prev
        else:
            prev.next = None
            while curr:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = nxt.next if nxt else None
            self.head = prev

    def size(self):
        return self._length