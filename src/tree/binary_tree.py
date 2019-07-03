from tree import node
from tree.node import Node

class BinaryTree:

    """DLR"""
    def preOrder(self, head):
        stack = []
        stack.append(head)
        while stack:
            curr = stack.pop()
            print(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    """LDR"""
    def inOrder(self,head):
        stack = []
        curr = head
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                print(curr.val)
                curr = curr.right
            else:
                break

    """LRD"""
    def postOrder(self,head):
        stack = []
        visited = None
        curr = head
        while True:
            if curr:
                if visited :
                    if curr.left == visited:
                        if curr.right:
                            curr = curr.right
                            visited = None
                        else:
                            curr = None
                    elif curr.right == visited:
                        curr = None
                else :
                    stack.append(curr)
                    curr = curr.left
            elif stack:
                top = self.peek(stack)
                if top.right and top.right != visited:
                    curr = top.right
                else:
                    visited = stack.pop()
                    print(visited.val)
                    curr = self.peek(stack)
            else:
                break


    def peek(self,stack) -> node:
        length = len(stack)
        if length > 0:
            return stack[len(stack)-1]
        else:
            return None

    def levelOrder(self,head):
        queue = []
        queue.append(head)
        while queue:
            curr = queue.pop(0)
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


    def zigZagOrder(self,head):
        stack1 = []
        stack2 = []
        stack1.append(head)
        while stack1 or stack2:
            while stack1:
                temp = stack1.pop()
                print(temp.val)
                if temp.left:
                    stack2.append(temp.left)
                if temp.right:
                    stack2.append(temp.right)

            while stack2:
                temp = stack2.pop()
                print(temp.val)
                if temp.right:
                    stack1.append(temp.right)
                if temp.left:
                    stack1.append(temp.left)