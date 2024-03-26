def sol(n):
    dp = [1 for i in range(10)]
    for _ in range(n-1):
        for i in range(1,10):
            dp[i] = dp[i] + dp[i-1]
    return sum(dp) % 10007



if __name__ == "__main__":
    n = int(input())
    print(sol(n))