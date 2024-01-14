def find_max_distance(seq,n,m):
    max_size = m//n
    dp = [[0 for _ in range(n)] for _ in range(max_size+1)]
    return dp[n-1]
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    seq = []
    for _ in range(m):
        seq.append(tuple(map(int,input().split())))
    print(find_max_distance(seq,n,m))