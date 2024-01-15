#바이러스 2606
#그래프 이론
from collections import deque
import sys
input = sys.stdin.readline
def bfs(edge,n):
    visited = [False] * (n)
    res = 0
    q = deque([0])
    visited[0] = True
    while q:
        x = q.popleft()
        res += 1
        for i in range(len(edge[x])):
            if edge[x][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
    return res
if __name__ == "__main__":
    n = int(input())
    edge = [[0]*(n) for _ in range(n)]
    line = int(input())
    for i in range(line):
        s,e = map(int,input().split())
        edge[s-1][e-1] = 1
        edge[e-1][s-1] = 1
    print(dfs(edge,n)-1)