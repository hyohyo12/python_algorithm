import sys
input = sys.stdin.readline
def get_round(n:int):
    dp = [0,1]
    if n == 1:
        return 4
    for i in range(2,n+1):
        dp.append(dp[i-1]+dp[i-2])
    ans = dp[n]*2 +(dp[n-1]+dp[n])*2
    return ans
if __name__ == "__main__":
    n = int(input())
    print(get_round(n))