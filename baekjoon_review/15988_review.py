def all_case()->list[int]:
    dp = [0,1,2,4]
    for i in range(4,1000001):
        dp.append((dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009)
    return dp


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    dp = all_case()
    for i in range(int(input())):
        print(dp[int(input())])