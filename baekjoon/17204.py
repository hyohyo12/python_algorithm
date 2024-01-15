#17204 죽음의 게임
#그래프 이론
from collections import deque
def dfs(graph,k):
    m = 0
    visited = [False] * len(graph[0])
    q = deque([0])
    visited[0] = True
    while q:
        x = q.popleft()
        if x == k:
            return m
        m+=1
        for i in range(len(graph[0])):
            if not visited[i] and graph[x][i] == 1:
                q.append(i)
                visited[i] = True
    return -1

if __name__ == "__main__":
    n,k = map(int,input().split())
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        num = int(input())
        graph[i][num] = 1
    print(dfs(graph,k))