def get_pascal(n:int,k:int)->int:
    dp = [[1]*i for i in range(1,n+1)]
    for i in range(2,n):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    return dp[n-1][k-1]
def get_pascal1(n:int,k:int)->int:
    dp = [[1 for j in range(min(i,k)+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j == 0 or j == i: continue
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n-1][k-1]
if __name__ =="__main__":
    n,k = map(int,input().split())
    print(get_pascal(n,k))
    print(get_pascal1(n,k))