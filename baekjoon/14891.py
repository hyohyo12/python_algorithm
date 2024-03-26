import sys
input = sys.stdin.readline

#리스트를 오른쪽으로 한칸 이동하고 해당 리스트를 다시 리턴하는 함수
def right_rotate(gear:list[str]):
    return gear[-1:]+gear[:7]
#리스트를 왼쪽으로 한칸 이동하고 해당 리스트를 다시 리턴하는 함수
def left_rotate(gear:list[str]):
    return gear[1:]+gear[:1]

#해당 톱니바퀴를 dir->1(시계방향) or dir->-1(반시계방향) 으로 돌리는 명령 실행하는 함수
def exc_command(n:int,dir:int):
    global gears
    #변경 사항을 한번에 반영하기위해 선언한 딕셔너리 key:인덱스, value:변경된 리스트
    change = dict()
    #왼쪽,오른쪽 각각 계속해서 갱신될 방향을 저장할 변수
    l_dir,r_dir = dir,dir
    #인덱스에 맞게 n값 조정
    n -= 1
    #전 값의 변경 유무 저장하는 flags리스트
    flags = [False for _ in range(4)]
    flags[n] = True
    #n번째 톱니바퀴로부터 오른쪽 변경점 저장
    for i in range(n+1,4):
        #전 톱니바퀴가 돌았을 때
        if flags[i-1]:
            #맞다은 부분의 극이 서로 같을 때
            if gears[i][6] != gears[i-1][2]:
                #시계 or 반시계 방향으로 회전
                if l_dir == 1:
                    #전 톱니바퀴의 방향 반대로
                    #변경 딕셔너리에 회전한 리스트를 저장
                    change[i] = left_rotate(gears[i])
                    #현재 회전 방향으로 방향 변수 갱신
                    l_dir = -1
                    #현재 톱니바퀴의 flag True로 갱신
                    flags[i] = True
                elif l_dir == -1:
                    change[i] = right_rotate(gears[i])
                    l_dir = 1
                    flags[i] = True
            #전 톱니바퀴가 돌지 않았다면 앞으로의 톱니바퀴는 돌아가지 않으므로
        else:
            #변경종료
            break
    #n번째 톱니바퀴 왼쪽 변경 사항 저장
    for i in range(n-1,-1,-1):
        #오른쪽 톱니바퀴(전 톱니바퀴) 가 돌아갔을 때
        if flags[i+1]:
            #전 톱니바퀴와 현재 톱니바퀴 맞다은 부분이 다를 때
            if gears[i][2] != gears[i+1][6]:
                #방향에 따라 변경 사항 딕셔너리에 저장
                if r_dir == 1:
                    change[i] = left_rotate(gears[i])
                    r_dir = -1
                    flags[i] = True
                elif r_dir == -1:
                    change[i] = right_rotate(gears[i])
                    r_dir = 1
                    flags[i] = True
        else:
            break
    #n번째 톱니바퀴 방향에 따라 상태 갱신
    if dir == 1:
        gears[n] = right_rotate(gears[n])
    elif dir == -1:
        gears[n] = left_rotate(gears[n])
    #나머지 톱니바퀴 변경사항에 따라 갱신
    for k,v in change.items():
        gears[k] = v


if __name__ == "__main__":
    #입력
    #톱니바퀴의 상태를 2차원 리스트로 저장
    gears = [list(input().rstrip()) for _ in range(4)]
    #실행할 명령의 개수
    k = int(input())
    
    #명령의 개수만큼 반복
    for _ in range(k):
        #n -> 변경할 톱니바퀴의 번호(1,2,3,4),dir 1-> 시계(오른쪽으로 로테이트), dir -1 -> 반시계(왼쪽으로 로테이트)
        n,dir = map(int,input().split())
        #명령 실행
        exc_command(n,dir)
    #점수계산
    #점수 저장할 변수(정답)
    score = 0
    #1,2,4,8 순으로 점수 배점
    w = 1
    #톱니바퀴 탐색
    for g in gears:
        #0번 인덱스-> 12시 방향 톱니바퀴의 상태
        #1(s극)일때만 점수를 부여하므로 상태확인
        if g[0] == '1':
            #배점 부여
            score += w
        #배점 갱신
        w *= 2
    #점수 출력
    print(score)