
def peek(self, stack):
    length = len(stack)
    if length > 0:
        return stack[len(stack) - 1]
    else:
        return None
