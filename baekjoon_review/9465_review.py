def score_max(seq: list[list[int]],n:int)->int:
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = seq[0][0]
    dp[1][0] = seq[1][0]
    if n == 1:
        return max(dp[0][0],dp[1][0])
    dp[0][1] = seq[1][0] + seq[0][1]
    dp[1][1] = seq[0][0] + seq[1][1]
    
    if n == 2:
        return max(dp[0][1],dp[1][1])
    
    for i in range(2,n):
        dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + seq[0][i]
        dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + seq[1][i]
    return max(dp[0][-1],dp[1][-1])






if __name__ == "__main__":
    import sys
    input =sys.stdin.readline
    
    for __ in range(int(input())):
        n = int(input())
        seq = [list(map(int,input().split())) for _ in range(2)]
        print(score_max(seq,n))