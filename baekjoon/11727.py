#11727 / 2xn 타일링 2
def sol(n):
    dp=[0]*1001
    dp[1] = 1
    dp[2] = 3
    dp[3] = 5
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2]*2
    print(dp[n] % 10007)
    
if __name__ == "__main__":
    n = int(input())
    sol(n)