import sys
input = sys.stdin.readline
from collections import deque

def sol(seq:list[int],n: int,s: int)-> list[int]:
    for i in range(n):
        max_num = max(seq[i:min(n,s+i+1)])
        idx = seq.index(max_num)
        for j in range(idx,i,-1):
            seq[j],seq[j-1] = seq[j-1],seq[j]
        s -= (idx-i)
        if s <= 0: break
    return seq
def main():
    n = int(input())
    seq = list(map(int,input().split()))
    s = int(input())
    seq = sol(seq,n,s)
    print(*seq)

if __name__ == "__main__":
    main()