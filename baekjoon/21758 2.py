import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    
    sum_seq = [seq[0]]
    for i in range(1,n):
        sum_seq.append(sum_seq[i-1]+seq[i])
    
    res = 0
    for i in range(1,n-1):
        res = max(sum_seq[n-2] + sum_seq[i-1] - seq[i],res)
    for i in range(1,n-1):
        res = max(sum_seq[n-1] - seq[0] - seq[i] + sum_seq[n-1]- sum_seq[i],res)
    for i in range(1,n-1):
        res = max(sum_seq[n-2] - seq[0] + seq[i],res)
    
    print(res)