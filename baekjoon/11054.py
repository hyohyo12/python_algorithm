import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    res = 0
    
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        tmp = 0
        for j in range(i-1,-1,-1):
            if seq[i] > seq[j]:
                tmp = max(tmp,dp[j])
        dp[i] += tmp
    reverse_dp = [1 for _ in range(n)]
    for i in range(n-2,-1,-1):
        tmp = 0
        for j in range(i+1,n):
            if seq[i] > seq[j]:
                tmp = max(tmp,reverse_dp[j])
        reverse_dp[i] += tmp
        dp[i] +=tmp
        res = max(res,dp[i])
    res = max(res,dp[-1])
    print(res)