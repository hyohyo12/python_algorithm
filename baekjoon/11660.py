def all_part_sum(seq:list[list[int]],n:int)->list[list[int]]:
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + seq[i-1][j-1]
    return dp
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    
    seq = []
    for i in range(n):
        seq.append(list(map(int,input().split())))
    dp = all_part_sum(seq,n)
    for i in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        print(dp[x2][y2] - dp[x2][y1-1]-dp[x1-1][y2] +dp[x1-1][y1-1])