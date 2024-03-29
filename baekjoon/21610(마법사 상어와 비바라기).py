import sys
input = sys.stdin.readline
#방향 리스트
dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

#구름을 방향대로 움직히는 함수
def move_cloud(cloud:list[list[int]],dir:int,s:int,n:int):
    #다음 이동한 구름의 위치를 반환할 리스트
    new_cloud = [[False for _ in range(n)] for _ in range(n)]
    #거리에 따라 가중치가 부여된 이동 거리
    weight_x,weight_y = dx[dir]*s,dy[dir]*s
    #cloud 를 순회
    for i in range(n):
        for j in range(n):
            #구름이 있는 곳이면
            if cloud[i][j]:
                #새로운 위치 인덱스 에러를 방지하기 위해 그리고 board의 양 옆, 위 아래 연결 됐으므로, 모듈러 연산 사용
                nx = (j + weight_x) % n;ny = (i + weight_y) % n
                #board 의 양 옆, 위 아래는 연결 됐으므로, 음수일 경우 이를 전체 길이에서 빼서 위치를 구한다.
                if nx < 0:
                    nx = n - nx
                if ny < 0:
                    ny = n - ny
                #새로운 위치에 구름위치 표시
                new_cloud[ny][nx] = True
    #새로운 구름 위치 반환
    return new_cloud


#메인 함수
def main():
    #n x n 크기의 board , m개의 명령
    n,m = map(int,input().split())
    #board값 입력
    board = [list(map(int,input().split())) for _ in range(n)]
    #구름의 위치를 저장 할 2차원 리스트
    cloud = [[False for _ in range(n)] for _ in range(n)]
    
    #초기 구름 세팅
    cloud[n-1][0] = True
    cloud[n-1][1] = True
    cloud[n-2][0] = True
    cloud[n-2][1] = True
    
    #m개의 명령 입력
    for _ in range(m):
        #방향 dir, 거리 s 값 입력
        dir,s = map(int,input().split())
        #구름을 해당 방향으로 s만큼 이동시킨 위치로 업데이트
        cloud = move_cloud(cloud,dir,s,n)
        #비가 내리기
        #비가 내린 곳을 저장할 리스트 -> 물 복사를 위해
        tmp = []
        #물의 양이 2이상인 곳의 위치를 저장할 리스트 -> 구름이 생기고 해당 칸의 물의 양에 -2 하기 위해
        remove_list = []
        #board를 순회하며 구름이 있는 곳에 + 1 한다. (비가 왔다.)
        for i in range(n):
            for j in range(n):
                if cloud[i][j]:
                    board[i][j] += 1
                    #바로 대각선을 더하지 않는 이유는 비 온 곳이 다 처리되지 않았으므로 정확하지 않은 데이터가 저장될 수 있으므로
                    tmp.append((i,j))
                    #비가 내렸으므로 해당 구름 위치는 False로 구름이 제거됨을 표시
                    cloud[i][j] = False
                #else문을 통해 구름이 있었던 곳은 구름이 다시 안 생기도록 함.
                else:
                    #해당 위치의 물이 2이상이면
                    if board[i][j] >= 2:
                        #구름이 생겼다고 표시
                        cloud[i][j] = True
                        #마찬가지로 지금 물의 양을 줄인다면, 물 복사 할 때, 정확하지 않은 데이터가 저장될 수 있음.
                        remove_list.append((i,j))
        #물복사
        #비가 내렸던 곳을 저장하는 tmp리스트를 순회
        for y,x in tmp:
            #2,4,6,8은 위의 방향 리스트에서 대각선 이동을 저장한다.
            for i in [2,4,6,8]:
                #대각선의 위치 nx,ny
                nx = x + dx[i];ny = y + dy[i]
                #물 복사 시 board는 양 옆, 위 아래 이어지지 않음. 물의 양이 1 이상일 때
                if 0 <= nx < n and 0 <= ny < n and board[ny][nx] >= 1:
                    #그 곳의 개수만큼 +1
                    board[y][x] += 1
        #구름이 생긴 곳의 위치에 물의 양 -2를 물 복사를 한 후 해준다.
        for y,x in remove_list:
            board[y][x] -= 2
    #결과 값을 저장할 변수 res
    res = 0
    #board를 순회하면서 모두 더한다.
    for b in board:
        res += sum(b)
    #결과값 출력
    print(res)

if __name__ == "__main__":
    main()