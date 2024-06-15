import sys
from collections import deque,defaultdict
input = sys.stdin.readline


def left(num:int):
    return num//1000 + (num%1000*10)
def right(num:int):
    return num//10 + (num%10)*1000
def d_cal(num:int):
    return (num*2)%10000
def s_cal(num:int):
    return (num-1)%10000



def bfs(origin:int,target:int)->str:
    visited = defaultdict(int)
    q = deque([(origin,'')])
    visited[origin] = 1
    while q:
        cur,commands = q.popleft()
        if cur == target:
            return commands
        d = d_cal(cur)
        if visited[d] == 0:
            visited[d] = 1
            q.append((d,commands+'D'))
        s = s_cal(cur)
        if visited[s] == 0:
            visited[s] = 1
            q.append((s,commands+'S'))
        l = left(cur)
        if visited[l] == 0:
            visited[l] = 1
            q.append((l,commands+'L'))
        r = right(cur)
        if visited[r] == 0:
            q.append((r,commands+'R'))
            visited[r] = 1



def main():
    #입력
    #입력받은 숫자 만큼 반복문 실행
    for _ in range(int(input())):
        origin,target = map(int,input().split())
        c = bfs(origin,target)
        print(c)




if __name__ == '__main__':
    #메인 함수 호출
    main()