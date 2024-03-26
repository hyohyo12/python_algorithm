import sys
from collections import deque
input = sys.stdin.readline

#구슬이 중력에 의해 움직이는 함수
def move(y,x,dx,dy):
    #만약 두 구슬이 겹친다면 어느 구슬이 더 앞에 있는지 검사하기 위한 변수
    cnt = 0
    # 다음 이동이 '#'(벽)을 만날 때까지 아니면 현재 구멍을 만날 때까지
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        #y는 dy방향으로 증가
        y += dy
        #x는 dx방향으로 증가
        x += dx
        #몇 번 움직였는지 체크
        cnt += 1
    #현재위치(y,x)와 몇 번 움직여는지 리턴
    return y,x,cnt

#이동 리스트
dx = [0,0,-1,1]
dy = [1,-1,0,0]
#board 탐색을 위한 BFS
def bfs(ry,rx,by,bx):
    count = 1
    #탐색을 위한 큐
    q = deque([(ry,rx,by,bx,count)])
    #중복 방문을 방지하기 위한 방문 set
    visited = set()
    #방문 set에 현재 위치 추가
    visited.add((ry,rx,by,bx))
    #bfs시작
    while q:
        #rx-> 빨간공 x값, ry-> 빨간 공 y값, bx->파란 공 x값, by -> 파란 공 y값,count-> 몇 번 굴렸는지.
        ry,rx,by,bx,count = q.popleft()
        # 공들을 굴린 횟수가 10번이 넘어가면 -1 리턴하도록 break
        if count > 10:
            break
        #4방향 검사
        for i in range(4):
            #빨간 공이 해당 이동리스트의 방향으로 움직인 위치 및 이동 횟수 저장
            nry,nrx,r_cnt = move(ry,rx,dx[i],dy[i])
            #파란 공도 마찬가지로 움직인 위치 및 이동 횟수 저장
            nby,nbx,b_cnt = move(by,bx,dx[i],dy[i])
            #파란 공이 구멍에 없다면
            #이 조건을 만족해야 아래 코드가 실행되는이유
            #해당 경로(파란 공이 구멍에 들어간 경로)가 더 이상 정답이 될 수 없으므로.
            if board[nby][nbx] != 'O':
                #위 조건을 만족하는데, 빨간공이 구멍에 있으면(성공하는 경우)
                if board[nry][nrx] == 'O':
                    #몇 번째 이동인지 리턴
                    return count
                #두 공의 위치가 겹칠 때
                if nrx == nbx and nry == nby:
                    #방금 전 몇 번 움직였는지에 따라 더 많이 움직인 공이 뒤로간다.
                    if r_cnt > b_cnt:
                        nrx -= dx[i]; nry -= dy[i]
                    else:
                        nbx -= dx[i]; nby -= dy[i]
                #방문 set에서 해당 ry,rx,by,bx값이 있는지 확인
                if not (nry,nrx,nby,nbx) in visited:
                    #다음 탐색을 위해 큐에 저장.
                    q.append((nry,nrx,nby,nbx,count+1))
                    #방문 처리
                    visited.add((nry,nrx,nby,nbx))
    return -1
if __name__ == "__main__":
    #입력
    #nxm 모양
    n,m = map(int,input().split())
    #board 입력
    board = []
    for i in range(n):
        tmp = list(input().rstrip())
        #파란색 공, 빨간색 공 시작점 찾기
        for j in range(m):
            if tmp[j] == 'B':
                by,bx = i,j
            elif tmp[j] == 'R':
                ry,rx = i,j
        #board에 삽입
        board.append(tmp)
    print(bfs(ry,rx,by,bx))

