def side():
    dp = [0 for _ in range(101)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3,101):
        dp[i] = dp[i-2] + dp[i-3]
    return dp
if __name__ == "__main__":
    nums = side()
    for i in range(int(input())):
        print(nums[int(input())])
    