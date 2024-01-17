def longest_seq(n:int,seq:list[int])->int:
    dp = [1] * (n)
    for i in range(1,n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int,input().split()))
    print(longest_seq(n,seq))