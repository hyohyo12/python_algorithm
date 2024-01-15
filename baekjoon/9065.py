def plus(n):
    dp = [0] * (n+1)
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]
if __name__ == "__main__":
    for i in range(int(input())):
        print(plus(int(input())))