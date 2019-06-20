from list.Node import Node

class circular_linked_list:
    __head = None
    __tail = None
    __length = 0

    def __init__(self,val):
        self.__head = Node(val)
        self.__tail = self.__head
        self.__length = 1

    def insert(self,val,index = 0):
        if index == 0:
            temp = Node(val)
            temp.next = self.__head
            self.__head = temp
            self.__tail.next = self.__head
        else:
            temp = self.__head
            while index > 0 and temp:
                index -= 1
                prev = temp
                temp = temp.next

            prev.next = Node(val)
            prev.next.next = temp
            self.__tail.next = self.__head
        self.__length += 1

    def append(self,val):
        temp = Node(val)
        if self.__tail:
            self.__tail.next = temp
        self.__tail = temp
        self.__tail.next = self.__head
        self.__length += 1

    def size(self):
        return self.__length

    def print(self):
        temp = self.__head
        while temp:
            print(temp.val)
            temp = temp.next