import sys
input = sys.stdin.readline

def main():
    n,k = map(int,input().split())
    value = [int(input()) for _ in range(n)]
    
    dp = [10001 for _ in range(k+1)]
    dp[0] = 0
    for v in value:
        #i -> 현재 가치 i원을 만들기 위한 최적해(제일 적은 수의 동전)
        for i in range(v,k+1):
            dp[i] = min(dp[i],dp[i-v] + 1)
    if dp[k] == 10001:
        print(-1)
    else:
        print(dp[k])

if __name__ == "__main__":
    main()