import sys
from collections import deque
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    dp = [1 for _ in range(n)]
    sub_seq = deque()
    for i in range(n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[j]+1,dp[i])
    tmp = max(dp)
    print(tmp)
    for i in range(n-1,-1,-1):
        if dp[i] == tmp:
            sub_seq.appendleft(seq[i])
            tmp -= 1
    print(*sub_seq)