import heapq
def minimum_class(seq:list[list[int]],n:int)->int:
    seq.sort()
    room = []
    heapq.heappush(room,seq[0][1])
    for i in range(1,n):
        if seq[i][0] < room[0]:
            heapq.heappush(room,seq[i][1])
        else:
            heapq.heappop(room)
            heapq.heappush(room,seq[i][1])
    return len(room)
            
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    seq = []
    for i in range(n):
        seq.append(list(map(int,input().split())))
    print(minimum_class(seq,n))
