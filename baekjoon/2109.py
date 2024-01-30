import sys
import heapq
input = sys.stdin.readline
def max_pay(seq:list[tuple[int]],n:int)->int:
    q = []
    for i in seq:
        heapq.heappush(q,i[0])
        if len(q) > i[1]:
            heapq.heappop(q)
    return sum(q)


if __name__ == "__main__":
    n = int(input())
    seq = [tuple(map(int,input().split())) for _ in range(n)]
    
    seq.sort(key = lambda x:x[1])
    
    print(max_pay(seq,n))