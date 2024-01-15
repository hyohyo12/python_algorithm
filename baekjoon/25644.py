# def find_max_profit(seq,n):
#     dp = [0 for _ in range(n)]
#     for i,j in enumerate(seq):
#         for k in range(i+1,n):
#             if dp[k] < seq[k]-j:
#                 dp[k] = seq[k]-j
#     return dp[n-1]



def find_max_profit(seq,n):
    benefit,ans = 0,0
    for i in range(n-1,-1,-1):
        benefit = max(benefit,seq[i])
        ans = max(benefit-seq[i],ans)
    return ans

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    seq = list(map(int,input().split()))
    
    print(find_max_profit(seq,n))