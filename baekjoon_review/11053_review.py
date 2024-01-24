def longest_seq(seq:list[int],n:int)-> int:
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)



if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    print(longest_seq(seq,n))