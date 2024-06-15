import sys
from collections import defaultdict
input = sys.stdin.readline

#방향 리스트
dx = [0,-1,0,1,-1,0,1,-1,0,1]
dy = [0,1,1,1,0,0,0,-1,-1,-1]

#종수 아두이노 이동 함수
def move_jongsu(index:tuple[int],dir:int)->tuple:
    global board
    if dir == 5:
        return(True,index)
    y,x = index
    #종수 아두이노 다음 좌표 ny,nx
    ny,nx = y+dy[dir], x+dx[dir]
    #board를 벗어나는 입력은 주어지지 않으므로 인덱스 유효 검사 불필요
    #이동한 곳에 미친 아두이노가 존재시 게임은 종료된다.
    if board[ny][nx] == 'R':
        board[y][x] = '.'
        return (False,index)
    #해당하는 곳이 빈칸이라면 이동
    else:
        board[ny][nx] = 'I'
        board[y][x] = '.'
        return (True,(ny,nx))
    
#미친 아두이노 이동시키는 함수
def move_crazy(indices:list[tuple[int]],jongsu:tuple):
    global board
    visited = defaultdict(int)
    jy,jx = jongsu
    #미친 아두이노의 갱신된 좌표를 저장할 set 
    new_crazy = set()
    #미친 아두이노의 위치가 겹칠경우 들어갈 set
    remove = set()
    for y,x in indices:
        min_distance = sys.maxsize
        for i in range(1,10):
            ny,nx = y + dy[i], x + dx[i]
            if not 0 <= ny < len(board) or not 0 <= nx < len(board[0]):
                continue
            distance = abs(jy - ny) + abs(jx - nx)
            if distance <= min_distance:
                min_distance = distance
                dir = i
        ny,nx = y + dy[dir],x +dx[dir]
        if board[ny][nx] == 'I':
            return (False,[])
        if visited[(ny,nx)] == 1:
            remove.add((ny,nx))
        visited[(ny,nx)] = 1
        new_crazy.add((ny,nx))
        board[ny][nx] = 'R'
        board[y][x] = '.'
    new_crazy -= remove
    new_crazy = list(new_crazy)
    for y,x in new_crazy:
        board[y][x] = 'R'
    for y,x in remove:
        board[y][x] = '.'
    return (True,new_crazy)
    
    
#메인 함수
def main():
    #글로벌 변수 board
    global board
    #미친 아두이노의 시작지점들 저장할 리스트 선언
    crazy = []
    #입력
    r,c = map(int,input().split())
    for i in range(r):
        #한 줄씩 입력 받음
        row = list(input().strip())
        #입력받은 row를 탐색하여 종수의 아두이노와 미친 아두이노의 시작 좌표를 저장함
        for j in range(c):
            #종수의 아두이노
            if row[j] == 'I':
                start = (i,j)
            #미친 아두이노
            elif row[j] == 'R':
                crazy.append((i,j))
        board.append(row)
    #명령들 입력
    commands = list(input().strip())
    
    if r == 1:
        print('I')
    else:
        for idx,command in enumerate(commands):
            #종수의 아두이노 이동
            flag,start = move_jongsu(start,int(command))
            #반환된 튜플의 첫번째 값이 False -> 종수가 미친 아두이노가 있는 자리로 이동
            if not flag:
                print("kraj {0}".format(idx+1))
                break
            flag,crazy = move_crazy(crazy,start)
            if not flag:
                print("kraj {0}".format(idx+1))
                break
        else:
            for r in board:
                print(''.join(r))


if __name__ == "__main__":
    #모든 함수 접근을 위해 global로 선언
    board = []
    main()