import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n,k = map(int,input().split())
    
    dia_seq = []
    for _ in range(n):
        m,v = map(int,input().split())
        heapq.heappush(dia_seq,(-v,m))
    
    bag_seq = [int(input()) for _ in range(k)]

    bag_seq.sort(reverse=True)
    bag = [[] for _ in range(len(bag_seq))]
    ans = 0
    for idx,w in enumerate(bag_seq):
        for _ in range(len(dia_seq)):
            v,m = heapq.heappop(dia_seq)
            v = abs(v)
            if len(bag[idx]) > 0 and m <= w:
                prev_v,prev_m = bag[idx].pop()
                if prev_v < v:
                    ans -= prev_v
                    bag[idx].append((v,m))
                    ans += v
                    heapq.heappush(dia_seq,(-prev_v,prev_m))
                elif prev_v == v:
                    if prev_m < m:
                        bag[idx].append((prev_v,prev_m))
                        heapq.heappush(dia_seq,(-v,m))
                    else:
                        bag[idx].append((v,m))
                        ans -= prev_v
                        ans += v
                        heapq.heappush(dia_seq,(-prev_v,prev_m))
                else:
                    bag[idx].append((prev_v,prev_m))
                    heapq.heappush(dia_seq,(-v,m))
            elif len(bag[idx]) == 0 and m <= w:
                ans += v
                bag[idx].append((v,m))
    print(ans)
