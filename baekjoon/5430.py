import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r_c = 0#리버스 카운트(몇번 돌렸는지 알려주는 카운터)
        command = list(input().strip()) #명령어
        n = int(input())
        seq = deque(input().strip()[1:-1].split(','))#리스트가 [1,2,3,4] 이런 식으로 입력되므로 분해해서 정수만 골라 리스트 만드는 코드
        if n == 0:#n이 0(길이가 0이라면)
            seq = deque()#빈 데크로 초기화
        for c in command:#명령어 탐색
            if c == 'R':#R(리스트 역순)명령
                r_c += 1#리버스 카운터 + 1 (그때 그때 돌리면 시간이 올래걸린다. -> 모아서 홀수면 한번 짝수면 그대로)
            elif c == 'D':#왼쪽 숫자 제거 명령
                if seq:#seq에 문자가 하나라도 있다면
                    if r_c % 2 == 0:#지금까지 몇번 돌았는지 만약 짝수면 그대로이므로 왼쪽 숫자를 빼준다.
                        seq.popleft()
                    else:seq.pop()#홀수라면 한 번 역순으로 됐다는 뜻이므로 오른쪽 값을 빼준다.
                else:#문자가 없다면 error 발생
                    print('error')
                    break#break
        else:#모든 명령 마치고 끝냈다면
            if r_c % 2 == 0:#리버스 카운터가 짝수면
                print('['+','.join(seq)+']')#그냥 출력
            else:#홀수라면
                seq.reverse()#한번 역순 정렬 후
                print('['+','.join(seq)+']')#출력
        