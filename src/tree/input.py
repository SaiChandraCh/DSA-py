from tree.BST.binary_search_tree import BinarySearchTree
from tree.binary_tree.binary_tree import BinaryTree

if __name__ == '__main__':

    tree = BinarySearchTree(15)
    tree.insert(68)
    tree.insert(30)
    tree.insert(28)
    tree.insert(188)
    tree.insert(18)
    tree.insert(25)
    tree.insert(26)
    tree.insert(1)
    tree.insert(90)
    tree.insert(108)
    tree.insert(111)
    tree.insert(19)
    tree.insert(85)
    tree.insert(91)
    tree.insert(136)

    BinaryTree.level_order(BinaryTree,tree.get_root())












