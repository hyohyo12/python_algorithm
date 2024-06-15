import sys
# from collections import defaultdict
input = sys.stdin.readline


mapping = {
    0:'N',
    1:'W',
    2:'S',
    3:'E'
}


dir = {
    'N':[-1,0],
    'W':[0,-1],
    'E':[0,1],
    'S':[1,0]
}


#동,서,남,북 을 연산하기 쉽게 숫자에 매핑해주는 함수
def mapping_dir(d:str):
    if d == 'N':
        return 0
    elif d == 'W':
        return 1
    elif d == 'S':
        return 2
    else:
        return 3


#명령 L,R 을 repeat만큼 반복한 후의 방향을 리턴하는 함수
#L -> 왼쪽으로 이동, R -> 오른쪽으로 이동
def c_L_R(command:str,dir:int,repeat:int):
    if command == 'L':
        return (dir + repeat) % 4
    return (dir - repeat) % 4

#F명령 수행하는 함수
#F-> 로봇의 방향에 따라 이동하는 명령
def c_F(board:list[list[int]],robot_dict:dict,num:int,repeat:int,hight:int,width:int):
    #robot_dict에서 현재 명령을 수행할 로봇의 위치정보 및 방향정보 가져옴
    y,x,d = robot_dict[num]
    #각 방향에 따른 이동리스트를 dir 딕셔너리에서 가져옴
    dy,dx = dir[mapping[d]]
    board[y][x] = 0
    
    for _ in range(repeat):
        y,x = y + dy, x + dx
        if 0 <= y < hight and 0 <= x < width:
            if board[y][x] != 0:
                return (-1,board[y][x])
        else:
            return (-2,-1)
    board[y][x] = num
    robot_dict[num][0] = y;robot_dict[num][1] = x
    return (1,-1)


def main():
    #초기화
    #각 번호의 로봇의 위치와 방향을 저장할 dict
    robot_dict = dict()
    #명령들을 입력받을 리스트 commands
    commands = []


    #입력
    #width -> 가로, hight -> 세로
    width,hight = map(int,input().split())
    #가로와 세로 길이에 맞게 board 초기화
    board = [[0 for _ in range(width)] for _ in range(hight)]


    #n -> 로봇의 개수, m -> 명령의 개수
    n,m = map(int,input().split())
    #n개의 로봇의 초기 위치와 방향 입력
    for i in range(1,n+1):
        #y -> 세로, x -> 가로, d -> 초기 방향
        x,y,d = input().strip().split()
        #y,x 정수형으로 형 변환
        y = int(y)
        #x는 1부터 인덱스 시작하므로 맞추기위해 - 1
        x = int(x) - 1
        #y축 입력 값이 인덱스와 반대이므로 맞춰줌
        y = abs(y-hight)
        #i번 로봇의 정보를 딕셔너리에 저장
        #방향을 숫자에 매핑하여 저장
        robot_dict[i] = [y,x,mapping_dir(d)]
        #board에 i번째 로봇 표시
        board[y][x] = i


    #m개의 명령 입력
    for _ in range(m):
        #in_num -> 명령을 수행할 로봇의 번호, in_command -> 수행해야할 명령의 종류, repeat -> 명령의 반복 횟수
        in_num,in_command,in_repeat = input().strip().split()
        #in_num,in_repeat을 정수형으로 형변환
        in_num = int(in_num)
        in_repeat = int(in_repeat)
        #명령을 저장하는 commands 리스트에 튜플 형식으로 입력 값 저장
        commands.append((in_num,in_command,in_repeat))
    #각 명령을 수행
    #num -> 명령을 수행할 로봇 번호, command -> 명령 종류(F,L,R), repeat -> 명령의 반복 횟수
    for num,command,repeat in commands:
        #num 번 로봇의 위치 정보 y,x값과 방향 정보 d를 언패킹
        y,x,d = robot_dict[num]
        #진행해야하는 연산이 L연산 또는 R연산일 때
        if (command == 'L' or command == 'R'):
            new_d = c_L_R(command,d,repeat)
            robot_dict[num][2] = new_d
        else:
            result,other = c_F(board,robot_dict,num,repeat,hight,width)
            if result == -1:
                print("Robot {0} crashes into robot {1}".format(num,other))
                return
            elif result == -2:
                print("Robot {0} crashes into the wall".format(num))
                return
    print("OK")
    return

if __name__ == "__main__":
    main()