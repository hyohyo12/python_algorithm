if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,m = map(int,input().split())
    seq = list(map(int,input().split()))
    pre_sum = [0]
    tmp = 0
    for i in seq:
        tmp+=i
        pre_sum.append(tmp)    
    for _ in range(m):
        i,j = map(int,input().split())
        print(pre_sum[j]-pre_sum[i-1])