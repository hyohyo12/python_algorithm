def get_max_payment(n,jobs):
    dp = [0 for i in range(n+1)]
    for i in range(n):
        for j in range(i+jobs[i][0],n+1):
            if dp[j] < dp[i] + jobs[i][1]:
                dp[j] = dp[i] + jobs[i][1]
    return dp[-1]
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    jobs = []
    for i in range(n):
        t,p = map(int,input().split())
        jobs.append((t,p))
    print(get_max_payment(n,jobs))