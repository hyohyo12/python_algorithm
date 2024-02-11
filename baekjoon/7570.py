def min_count(n:int,seq:list[int])->int:
    idx = [-1 for _ in range(n+1)]
    for i,v in enumerate(seq):
        idx[v] = i
    cnt = 1
    longest = 0
    for num in range(1,n):
        if idx[num] < idx[num+1]:
            cnt += 1
        else:
            longest = max(longest,cnt)
            cnt = 1
    return n-longest if n != 1 else 0


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    seq = list(map(int,input().split()))
    
    print(min_count(n,seq))