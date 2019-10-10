from tree.node import Node

class BinarySearchTree:

    __root = None

    def __init__(self, val):
        self.__root = Node(val)

    def get_root(self) -> Node:
        return self.__root

    def insert(self,val) -> bool:
        curr = self.__root
        prev = None
        while curr:
            prev = curr
            if val > curr.val:
                curr = curr.right
            elif val <= curr.val:
                curr = curr.left

        if val > prev.val:
            prev.right = Node(val)
            return True
        else:
            prev.left = Node(val)
            return True

        return False

    def search(self):
        print(self.__root)

    def delete(self):
        self.__root = 5
        print("hello")


# if __name__ == '__main__':
#     BinarySearchTree.delete(BinarySearchTree)
#     BinarySearchTree.search(BinarySearchTree)