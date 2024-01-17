# def stone(n):
#     dp = [-1] * 1001
#     dp[1] = 1
#     dp[2] = 0
#     dp[3] = 1
#     for i in range(4,n+1):
#         if dp[i-1] == 1 or dp[i-3]:
#             dp[i] = 0
#         else:
#             dp[i] = 1
#     if dp[n] == 0:
#         print("CY")
#     else:
#         print("SK")
# if __name__ == "__main__":
#     stone(int(input()))


def find_winner(n:int)->int:
    dp = [0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 0
    dp[3] = 1
    for i in range(4,n+1):
        if dp[i-1]+dp[i-3] == 2:
            dp[i] = 0
        else:
            dp[i] = 1
    return dp[n]
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    if find_winner(n):
        print('SK')
    else:
        print('CY')























