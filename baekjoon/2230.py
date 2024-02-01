import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int,input().split())
    seq = [int(input()) for _ in range(n)]
    seq.sort()
    start,end = 0,0
    
    result = sys.maxsize
    while start <= end and end < n:
        if seq[end]-seq[start] < m:
            end += 1
        else:
            result = min(result,seq[end]-seq[start])
            start += 1
    print(result)
