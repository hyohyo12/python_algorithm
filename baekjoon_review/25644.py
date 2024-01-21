def max_profit(n:int,seq:list[int])->int:
    dp = [0 for _ in range(n)]
    tmp = seq[0]
    for i in range(1,n):
        dp[i] = max(seq[i]-tmp,dp[i])
        tmp = min(seq[i],tmp)
    return max(dp)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    seq = list(map(int,input().split()))
    print(max_profit(n,seq))