import sys
input = sys.stdin.readline

def LCS(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s2[i-1] == s1[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return reverseTracking(dp,n,m)

def reverseTracking(dp:list[list[int]],n:int,m:int):
    cnt = 0
    while n > 0 and m > 0:
        if dp[m-1][n] == dp[m][n]:
            m -= 1
        elif dp[m][n-1] == dp[m][n]:
            n -= 1
        else:
            cnt += 1
            m -= 1; n -= 1
    return cnt


if __name__ == "__main__":
    string1 = input().strip()
    string2 = input().strip()
    
    print(LCS(string1,string2))