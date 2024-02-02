import sys
input = sys.stdin.readline

def dfs(x,y,graph):
    global count
    if x == 0: #x가 0이라는 건 이웃 빵집에 도달했다는 뜻이므로
        count += 1 #정답 변수 + 1
        return True #True 리턴
    for dx,dy in [(-1,-1),(-1,0),(-1,1)]: #왼쪽 아래 대각선, 왼쪽, 왼쪽 위 대각선 순회
        nx,ny= x+dx, y+dy
        if 0 <= nx < c and 0 <= ny < r: #인덱스 에러 방지
            if graph[ny][nx] == '.': #건물이 아니라면
                graph[ny][nx] = 'x'#방문 처리 후
                if dfs(nx,ny,graph): #재귀 호출 도달했다면 True 리턴 
                    return True
    return False

if __name__ == "__main__":
    r,c = map(int,input().split())
    
    graph = [list(input().strip()) for _ in range(r)]
    
    count = 0
    
    for y in range(r): #모든 y축에 대해 dfs 순회
        dfs(c - 1, y,graph)
    print(count)