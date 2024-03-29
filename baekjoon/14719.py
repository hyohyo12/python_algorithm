import sys
input = sys.stdin.readline

#메인 함수
def main():
    #h -> 높이, w-> 가로
    h,w = map(int,input().split())
    #각 벽의 높이를 저장하는 리스트
    seq = list(map(int,input().split()))
    #빗물이 고인 곳을 쉽게 파악하기위한 리스트
    board = [[0 for _ in range(w)] for _ in range(h)]
    
    #모든 높이에 대한 가로 탐색
    for i in range(h):
        #가로 양 옆(첫번째,끝)은 빗물이 고일 수 없으므로 1~w-1까지 순회
        for j in range(1,w-1):
            #해당하는 곳에 벽이 있다면
            if seq[j] != 0:
                #해당 벽이 높이보다 작다면 빗물이 고일 가능성 있음.
                if i >= seq[j]:
                    #양 옆 벽의 높이가 현재 높이보다 높다면
                    if max(seq[:j]) > i and max(seq[j+1:]) > i:
                        #빗물이 고이므로 표시
                        board[i][j] = '#'
            #해당하는 곳에 벽의 높이가 0이라면
            else:
                #양 옆 벽의 높이 비교 후 빗물 표시
                if max(seq[:j]) > i and max(seq[j+1:]) > i:
                    board[i][j] = '#'
    #빗물 고인 곳 출력
    print(sum(board[i].count('#') for i in range(h)))

if __name__ == "__main__":
    main()
