import sys
input = sys.stdin.readline


#명령에 따른 이동 방향
dir = {
    'R':[0,1],
    'L':[0,-1],
    'B':[1,0],
    'T':[-1,0],
    'RT':[-1,1],
    'LT':[-1,-1],
    'RB':[1,1],
    'LB':[1,-1]
}

#8 x 8 크기 board에서 유효한 인덱스인지 검사하는 함수
def is_valid_loc(y:int,x:int):
    if 0 <= y < 8 and 0 <= x < 8:
        return 1
    return 0

#출력 형식에 맞는 좌표로 다시 변환해주는 함수
def format_loc(location:tuple):
    y,x = location
    return chr(x + 65) + str(abs(y - 8))


def main():
    #입력
    #킹, 돌의 좌표 str자료형으로 입력 받음
    #n -> 명령의 개수
    king,stone,n = input().strip().split()
    
    #전처리(X축은 알파벳으로 입력받기 때문에(A -> 0 , B -> 1,...,h -> 7) 정수형 숫자 매핑 시키고, y축 또한 인덱스 맞추고 정수형으로 형변환)
    king = (abs(int(king[1]) - 8),ord(king[0])-65)
    stone = (abs(int(stone[1]) - 8),ord(stone[0])-65)
    
    #n개의 명령을 입력 받고 명령 수행
    for _ in range(int(n)):
        #이동 방향 딕셔너리에서 입력된 명령의 이동 방향을 각각 dy,dx에 저장
        dy,dx = dir[input().strip()]
        ny_k,nx_k = king[0] + dy, king[1] + dx
        if is_valid_loc(ny_k,nx_k):
            if stone != (ny_k,nx_k):
                king = (ny_k,nx_k)
            else:
                ny_s,nx_s = stone[0] + dy, stone[1] + dx
                if is_valid_loc(ny_s,nx_s):
                    stone = (ny_s,nx_s)
                    king = (ny_k,nx_k)
    
    #킹의 좌표 출력
    print(format_loc(king))
    #돌의 좌표 출력
    print(format_loc(stone))
    
if __name__ == "__main__":
    main()