def sub_seq_sum(seq:list[int],n:int) -> list[int]:
    cur = seq[0]
    for i in range(1,n):
        cur += seq[i]
        seq[i] = cur
    return seq
    
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n,m = map(int,input().split())
    seq = list(map(int,input().split()))
    
    seq = sub_seq_sum(seq,n)
    for i in range(m):
        start,end = map(int,input().split())
        if start == 1:
            print(seq[end-1])
        else:
            print(seq[end-1]-seq[start-2])
    