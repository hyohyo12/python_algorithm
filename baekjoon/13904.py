import sys
import heapq
input = sys.stdin.readline

def max_score(seq:list[int]):
    schedule = []
    for d,s in seq:
        heapq.heappush(schedule,s)
        if len(schedule) > d:
            heapq.heappop(schedule)
    return sum(schedule)

if __name__ == "__main__":
    seq = []
    n = int(input())
    
    for _ in range(n):
        seq.append(tuple(map(int,input().split())))
    
    seq.sort(key = lambda x:x[0])
    print(max_score(seq))