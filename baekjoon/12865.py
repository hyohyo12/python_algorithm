import sys
input = sys.stdin.readline
def knapsack(n,W,wt,val):
    dp = [[0 for _ in range(W+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                valWith = val[i-1]+dp[i-1][w-wt[i-1]]
                valWithout = dp[i-1][w]
                dp[i][w] = max(valWith,valWithout)
    print(dp[i][w])
if __name__ == "__main__":
    n,k = map(int,input().split())
    val = []
    weight = []
    for i in range(n):
        w,v = map(int,input().split())
        val.append(v)
        weight.append(w)
    knapsack(n,k,weight,val)