import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    seq = []
    for _ in range(n):
        seq.append(list(map(int,input().split())))
    seq.sort(key=lambda x:x[1])
    
    room = 1
    q = []
    heapq.heappush(q,seq[0][2])
    for i in range(1,n):
        end = heapq.heappop(q)
        if seq[i][1] >= end:
            heapq.heappush(q,seq[i][2])
        else:
            room += 1
            heapq.heappush(q,seq[i][2])
            heapq.heappush(q,end)
    print(room)
    