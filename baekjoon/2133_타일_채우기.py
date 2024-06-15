import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [0,0,3]
    for i in range(3,n+1):
        if not(i % 2):
            dp.append(dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2)
        else:
            dp.append(0)
    print(dp[n])

if __name__ == "__main__":
    main()
