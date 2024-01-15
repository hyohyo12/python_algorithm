#26170 / 사과 빨리 먹기
import sys
input = sys.stdin.readline
def dfs(graph,cur_x,cur_y,count,dist):
    global ans
    global success
    if count == 3:
        if ans > dist:
            ans = dist
            success = True
    for i in possible:
        if ((cur_y+i[0]) >= 0 and (cur_x + i[1]) >= 0) and ((cur_y + i[0]) < 5 and (cur_x + i[1]) < 5):
            if graph[cur_y+i[0]][cur_x+i[1]] != -1:
                if graph[cur_y+i[0]][cur_x+i[1]] == 1:
                    graph[cur_y+i[0]][cur_x+i[1]] = -1
                    dfs(graph,cur_x+i[1],cur_y+i[0],count+1,dist+1)
                    graph[cur_y+i[0]][cur_x+i[1]] = 1
                else:
                    graph[cur_y+i[0]][cur_x+i[1]] = -1
                    dfs(graph,cur_x+i[1],cur_y+i[0],count,dist+1)
                    graph[cur_y+i[0]][cur_x+i[1]] = 0
        else:
            continue     
if __name__ == "__main__":
    graph = []
    success = False
    for i in range(5):
        graph.append(list(map(int,input().split())))
    y,x = map(int,input().split())
    possible = [[1,0],[-1,0],[0,1],[0,-1]]
    ans = float("inf")
    
    if graph[y][x] == 1:
        graph[y][x] = -1
        dfs(graph,x,y,1,0)
        
    else:
        graph[y][x] = -1
        dfs(graph,x,y,0,0)
    if success:
        print(ans)
    else:
        print(-1)