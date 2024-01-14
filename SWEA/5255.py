T = int(input())
for task_case in range(1,T+1):
    n = int(input())
    dp = [0] *(n+1)
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 3
        elif i == 3:
            dp[i] = 6
        else:
            dp[i] = dp[i-1]+dp[i-2]*2+dp[i-3]
    print(f"#{task_case} {dp[n]}")