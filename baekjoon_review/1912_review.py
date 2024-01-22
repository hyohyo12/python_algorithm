def biggest_sub_seq(n:int,seq:list[int])->int:
    dp = seq[:]
    for i in range(1,n):
        dp[i] = max(dp[i],dp[i-1]+seq[i])
    return max(dp)


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    print(biggest_sub_seq(n,seq))