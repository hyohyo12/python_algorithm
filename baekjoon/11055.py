def longest_sum(seq:list[int],n:int)->int:
    dp = seq[:]
    for i in range(1,n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i],dp[j]+seq[i])
    return max(dp)



if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    seq = list(map(int,input().split()))
    
    print(longest_sum(seq,n))   