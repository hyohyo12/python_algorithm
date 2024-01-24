def binary_search(seq: list[int],n: int)-> int:
    left = 1
    right = max(seq)
    while left <= right:
        mid = (left + right) // 2
        lines = 0
        for i in seq:
            lines += (i//mid)
        if lines < n:
            right = mid - 1
        else:
            left = mid + 1
    return right

if __name__ =="__main__":
    k,n = map(int,input().split())
    seq = [int(input()) for _ in range(k)]
    print(binary_search(seq,n))