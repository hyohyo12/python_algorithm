def sub_seq_sum(s,n,start,seq,cur):
    global cnt
    if sum(cur) == s and len(cur) > 0:
        cnt += 1
    for i in range(start,n):
        cur.append(seq[i])
        sub_seq_sum(s,n,i+1,seq,cur)
        cur.pop()

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n,s = map(int,input().split())
    seq = list(map(int,input().split()))
    cnt = 0
    visited = [False for _ in range(n)]
    sub_seq_sum(s,n,0,seq,[])
    print(cnt)
