def stair(n,lis):
    dp = [0] * (301)
    dp[0] = lis[0]
    dp[1] = lis[0] + lis[1]
    dp[2] = max(lis[0]+lis[2],lis[1]+lis[2])
    for i in range(3,n):
        dp[i] = max((dp[i-3]+lis[i-1]+lis[i]),(dp[i-2]+lis[i]))
    print(dp[n-1])

if __name__ == "__main__":
    n = int(input())
    lis = [0] * 301
    for i in range(n):
        lis[i] = int(input())
    stair(n,lis)