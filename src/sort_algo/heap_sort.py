def heap_sort(A):
    n = len(A)
    for i in range(n,-1,-1):
        heapify(A,n,i)


    for i in range(n-1,0,-1):
        A[0],A[i] = A[i],A[0]
        heapify(A,i,0)


def heapify(A,n,i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if right < n and A[right] > A[i]:
        largest = right

    if left < n and A[left] > A[largest]:
        largest = left

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A,n,largest)

if __name__ == '__main__':
    # A = [133,114,306,742,8,643,574,876,201,70,16,344,399,451,793,535,893,800,620,783,932,27,396,691,305,172,612,364,119,109,551]
    A = [14, 3, 7, 11, 12, 9, -1, 11, 6, 2, 8, -3, 10]
    # A = [1,3,2,4,5,6,7]
    # 133,114,306,742,8,6,43,574,876,201,70,16,344,399,451,793,535,893,800,620,783,932,27,396,691,305,172,612,364,119,109,551
    heap_sort(A)
    print(A)
