def extend_fibo(n:int)->int:
    dp = [0,1,1]
    for i in range(3,abs(n)+1):
        dp.append((dp[i-1] + dp[i-2])%1000000000)
    if n < 0:
        if n % 2 == 0:
            print(-1)
            return dp[abs(n)]
        else:
            print(1)
            return dp[abs(n)]
    else:
        print(0 if n == 0 else 1)
        return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(extend_fibo(n))