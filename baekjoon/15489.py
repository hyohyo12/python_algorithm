import sys
input = sys.stdin.readline

def bino_coef(r,c,w):
    dp = [[1]*i for i in range(1,r+w)]
    
    for i in range(2,r+w-1):
        for j in range(1,len(dp[i])-1):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    cnt = -1
    ans = 0
    for i in range(r-1,r+w-1):
        cnt+=1
        for j in range(c-1,c+cnt):
            ans+=dp[i][j]
    print(ans)


if __name__ == "__main__":
    r,c,w = map(int,input().split())
    bino_coef(r,c,w)