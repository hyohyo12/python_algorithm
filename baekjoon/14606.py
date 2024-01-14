def get_happiness(n):
    dp = [0] * (11)
    dp[1] = 0
    dp[2] = 1
    for i in range(3,n+1):
        m = i//2
        dp[i] = m*(i-m) + dp[m] + dp[i-m] 
    return dp[n]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    print(get_happiness(n))