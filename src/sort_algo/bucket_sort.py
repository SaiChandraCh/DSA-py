class Node:
    def __init__(self,val):
        self.val = val
        next = None

def bucket_sort(A):
    size = len(A)
    bucket = [0 for _ in range(size)]

if __name__ == '__main__':
    # [133,114,306,742,8,643,574,876,201,70,16,344,399,451,793,535,893,800,620,783,932,27,396,691,305,172,612,364,119,109,551]
    # [1,3,2,4,5,6,7]
    A = [14, 3, 7, 11, 12, 9, -1, 11, 6, 2, 8, -3, 10]
    bucket_sort(A)