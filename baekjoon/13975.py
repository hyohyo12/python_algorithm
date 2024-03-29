import heapq
import sys
input = sys.stdin.readline




if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = list(map(int,input().split()))
        heapq.heapify(seq)
        res = 0
        while len(seq) != 1:
            x1 = heapq.heappop(seq)
            x2 = heapq.heappop(seq)
            res += (x1+x2)
            heapq.heappush(seq,x1+x2)
        print(res)