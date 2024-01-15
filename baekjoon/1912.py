def max_con_sum(n:int,seq:int)->int:
    for i in range(1,len(seq)):
        seq[i] = max(seq[i],seq[i-1]+seq[i])
    return max(seq)
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int,input().split()))
    print(max_con_sum(n,seq))