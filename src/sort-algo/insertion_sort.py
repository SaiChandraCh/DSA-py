def insertion_sort(A):
    j = 1
    length = len(A)
    while j < length:
        key = A[j]
        i = j-1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
        j += 1
    return A

if __name__ == '__main__':
    A = [31, 41, 59, 26, 41, 58]
    print(A)
    A = insertion_sort(A)
    print(A)
