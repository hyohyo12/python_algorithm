#일단 보류
import sys
input = sys.stdin.readline

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


#중력에따라 클러스터가 바닥으로 이동 함수
def gravity(board:list[list[str]],r:int,c:int):
    for i in range(r):
        for j in range(c):
            pass


#메인 함수
def main():
    #rxc모양의
    r,c = map(int,input().split())
    #r개 줄을 입력받아 저장할 board
    board = [list(input().strip()) for _ in range(r)]
    #던진 창의 개수 n
    n = int(input())
    #입력된 창의 개수 만큼 높이 입력
    h = list(map(int,input().split()))
    

if __name__ == "__main__":
    main()