import heapq
import sys
input = sys.stdin.readline
def max_pay(seq: list[int],n:int)->int:
    q = []
    for i in range(n):
        heapq.heappush(q,seq[i][0])
        if len(q) > seq[i][1]:
            heapq.heappop(q)
    return sum(q)




if __name__ == "__main__":
    n = int(input())
    req_seq = [tuple(map(int,input().split())) for _ in range(n)]
    
    req_seq.sort(key=lambda x:x[1])
    print(max_pay(req_seq,n))