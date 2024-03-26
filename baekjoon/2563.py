import sys
input = sys.stdin.readline




if __name__ == "__main__":
    #도화지 크기
    board = [[0]*100 for _ in range(100)]
    #결과 값을 담을 변수
    res = 0
    #도화지에 놓을 색종이의 개수
    n = int(input())
    #색종이 개수 만큼 반복
    for _ in range(n):
        x,y = map(int,input().split())
        #도화지에 해당 색종이의 크기 만큼 1로 채우기
        for i in range(y,y+10):
            for j in range(x,x+10):
                board[i][j] = 1
    #1의 개수->넓이
    for i in board:
        res+=i.count(1)
    #넓이 출력
    print(res)