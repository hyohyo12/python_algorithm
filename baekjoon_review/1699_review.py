def sol(n:int)->int:
    dp = [i for i in range(0,n+1)]
    for i in range(2,n+1):
        for j in range(1,i+1):
            if j**2 > i:
                break
            dp[i] = min(dp[i],dp[i-j*j] + 1)
    return dp[n]
if __name__ == "__main__":
    n = int(input())
    print(sol(n))