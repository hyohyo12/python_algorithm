import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    seq = [tuple(map(int,input().split())) for _ in range(n)]
    seq.sort()
    
    q = []
    
    for deadline,score in seq:
        heapq.heappush(q,score)
        if len(q) > deadline:
            heapq.heappop(q)
    print(sum(q))