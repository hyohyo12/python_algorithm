def fibo(n):
    dp = [0] * 51
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = (dp[i-1] + dp[i-2] + 1)
    print(dp[n] % 1000000007)
if __name__ =="__main__":
    n = int(input())
    fibo(n)