import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    visited = [False for _ in range(v+1)]
    q = deque()
    q.append((start,0))
    visited[start] = True
    tmp = [0,0]
    while q:
        dest,cost = q.popleft()
        for next_d,next_c in tree[dest]:
            if not visited[next_d]:
                q.append((next_d,next_c+cost))
                visited[next_d] = True
                if cost+next_c > tmp[1]:
                    tmp[1] = cost+next_c
                    tmp[0] = next_d
    return tmp

if __name__ == "__main__":
    v = int(input())
    tree = [[] for _ in range(v+1)]
    for _ in range(v):
        seq = list(map(int,input().split()))
        for i in range(1,len(seq)-1,2):
            tree[seq[0]].append((seq[i],seq[i+1]))
    point,temp = bfs(1)
    print(bfs(point)[1])