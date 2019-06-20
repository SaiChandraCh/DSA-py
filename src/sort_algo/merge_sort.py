def merge_sort(A,start,end):
    if end-start > 1:
        mid = start + (end-start)//2
        merge_sort(A,start,mid)
        merge_sort(A,mid,end)
        print("Before : ",A)
        merge(A,start,mid,end)
        print("After : ",A)
        return A

def merge(A,start,mid ,end):
    i = start
    j = mid
    temp = []
    while i < mid and j < end:
        if A[i] > A[j]:
            temp.append(A[j])
            j += 1
        else:
            temp.append(A[i])
            i += 1
    if i != mid:
        while i < mid:
            temp.append(A[i])
            i += 1
    elif j != end:
        while j < end:
            temp.append(A[j])
            j += 1
    i = start
    for num in temp:
        A[i] = num
        i += 1
    return A

if __name__ == '__main__':
    # A = [14, 7, 3, 12, 9, -1, 11, 6, 2, 8, -3, 10]
    A = [8, 5, 9, 1, 6, 7, 0, 3]
    A = merge_sort(A,0,len(A))
    print(A)