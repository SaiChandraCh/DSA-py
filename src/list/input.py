from src.list import LinkedList


def input():
    obj = LinkedList()
    obj.insert(5)
    obj.insert(9)
    obj.insert(1)
    obj.insert(6)
    obj.insert(7)
    obj.insert(0)
    obj.insert(3)

    obj.print()
    obj.delete(0)
    obj.print()

    obj.size()
