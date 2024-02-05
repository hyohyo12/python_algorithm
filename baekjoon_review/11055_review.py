def biggest_seq(seq:list[int],n:int)->int:
    dp = seq[:]
    for i in range(1,n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i],dp[j]+seq[i])
    return max(dp)

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    print(biggest_seq(seq,n))