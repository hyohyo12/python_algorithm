import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph:list[list[int]],v:int):
    visited = [0 for _ in range(v+1)]
    q = deque([1])
    visited[1] += 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == True:
                


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        v,e = map(int,input().split())
        graph = [[] for _ in range(v+1)]
        for __ in range(e):
            sp,ep = map(int,input().split())
            graph[sp] = ep
        