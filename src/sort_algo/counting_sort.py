def counting_sort(A):
    mini = min(A)
    maxi = max(A)
    n = len(A)
    ranz = maxi - mini +1
    result = [0 for _ in range(len(A))]
    count = [0 for _ in range(ranz)]
    for i in A:
        count[i-mini] += 1

    for i in range(1,ranz):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        count[A[i]-mini] -= 1
        result[count[A[i]-mini]] = A[i]


if __name__ == '__main__':
    # A = [14, 3, 7, 11, 12, 9, -1, 11, 6, 2, 8, -3, 10]
    # [1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 2, 1, 0, 1]
    # [-3, -1, 2, 3, 6, 7, 8, 9, 10, 11, 11, 12, 14]
    A = [133,114,306,742,8,643,574,876,201,70,16,344,399,451,793,535,893,800,620,783,932,27,396,691,305,172,612,364,119,109,551]
    print(A)
    counting_sort(A)


