import sys
import heapq as hq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    station = [tuple(map(int,input().split())) for _ in range(n+1)]
    station.sort()
    cnt = 0
    cur = 0
    fuel  =station[n][1]
    
    q = []
    for i in range(n+1):
        distance = station[i][0] - cur
        cur = station[i][0]
        if fuel < distance:
            while fuel < distance:
                if len(q):
                    cnt += 1
                    fuel += (-1 * hq.heappop(q))
                else:
                    cnt = -1
                    break
            if cnt == -1:
                print(-1)
                break
        hq.heappush(q,-1 * station[i][1])
        fuel -= distance
    else:
        print(cnt)