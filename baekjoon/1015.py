def sequenceP(N,A):
    # sort_A = sorted(A)
    # result = []
    # for i in A:
    #     result.append(sort_A.index(i))
    # for j in result:
    #     print(j,end=" ")
    sort_A = sorted(A)
    result = []
    for i in range(N):
        for j in range(N):
            if A[i] == sort_A[j]:
                result.append(j)
                sort_A[j] = -1
                break
    for j in result:
        print(j,end=" ")
if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    sequenceP(n,a)