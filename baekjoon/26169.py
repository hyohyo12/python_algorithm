def dfs(graph,visited,r,c,apple,n):
    visited[r][c] = True
    
    if graph[r][c] == 1:
        apple+=1
    
    if apple >= 2:
        return 1
    
    if n > 2:
        visited[r][c] = False
        return 0
    
    for i in ([0,1],[0,-1],[1,0],[-1,0]):
        if 0 <= r+i[0] < 5 and 0 <= c+i[1] < 5:
            if not visited[r+i[0]][c+i[1]] and graph[r+i[0]][c+i[1]] != -1:
                if dfs(graph,visited,r+i[0],c+i[1],apple,n+1) == 1:
                    return 1
    visited[r][c] = False
    return 0


if __name__ == "__main__":
    graph = []
    for i in range(5):
        graph.append(list(map(int,input().split())))
    r,c = map(int,input().split())
    visited = [[False] * 5 for _ in range(5)]
    print(dfs(graph,visited,r,c,0,0))