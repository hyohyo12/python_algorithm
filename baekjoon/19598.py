import sys
input = sys.stdin.readline
import heapq



if __name__ == "__main__":
    n = int(input())
    meeting_seq = []
    for _ in range(n):
        heapq.heappush(meeting_seq,tuple(map(int,input().split())))
    
    room = 1
    seq = []
    s,e = heapq.heappop(meeting_seq)
    heapq.heappush(seq,e)
    while meeting_seq:
        s,e = heapq.heappop(meeting_seq)
        tmp = heapq.heappop(seq)
        if s < tmp:
            room += 1
            heapq.heappush(seq,e)
            heapq.heappush(seq,tmp)
        else:
            heapq.heappush(seq,e)
    print(room)