def quick_sort(A,start,end):
    if end - start > 1:
        pivot = A[end]
        print(A, pivot)
        i = start
        j = end
        while j >= i:
            if A[i] >= pivot:
                A[i],A[j-1] = A[j-1],A[i]
                A[j],A[j-1] = A[j-1],A[j]
                j -= 1
            else:
                i += 1
        quick_sort(A,start,j)
        quick_sort(A,j+1,end)


if __name__ == '__main__':
    A = [14, 7, 3, 12, 1, 9, 19, -1, 5, 4, 11, 6, 2, 8, -3, 10]
    quick_sort(A,0,len(A)-1)
    print(A)