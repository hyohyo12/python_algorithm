import sys
import heapq as hq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    station = [tuple(map(int,input().split())) for _ in range(n+1)]
    #주유소의 위치에 대해 정렬
    station.sort()
    #주유소 몇 번 들렸는지 저장하는 변수
    cnt = 0
    #현재 위치를 저장하는 변수 (초기 위치 0)
    cur = 0
    #초기 연료 마지막 줄의 1번째 요소이다
    fuel  =station[n][1]
    
    #각 주유소의 주입가능한 연료량을 우선순위 큐로 저장(연료 부족할 때마다 탐욕적으로 제일 많은 연료량을 주유하기 위함.)
    q = []
    #각 주유소 마지막으로 도착지까지 순회하므로 (n+1)만큼 순회
    for i in range(n+1):
        #거리 (다음 주유소 위치 - 현재 위치)
        distance = station[i][0] - cur
        #현재 위치 업데이트
        cur = station[i][0]
        #연료가 현재위치 까지 가지 못한다면
        if fuel < distance:
            #그 거리만큼 갈 수 있는 연료가 있을 때만큼 우선순위 큐(전 주유소에서 얻을 수 있는 연료량 중) 최대를 선택(탐욕적 선택)
            while fuel < distance:
                #q에 남은 연료가 있을 때만 큐에서 빼오고 cnt(주유소를 들린 수) 증가
                if len(q):
                    cnt += 1
                    fuel += (-1 * hq.heappop(q))
                #연료가 부족한데 주유소에서 얻을 수 있는 연료가 없을 때
                else:
                    #cnt 를 -1 로 설정하고 break
                    cnt = -1
                    break
            #연료를 충전해도 다음 거리만큼 못 간다면 마을까지 갈 수 있는 방법이 없으므로 -1을 출력 후 반복 종료
            if cnt == -1:
                print(-1)
                break
        #현재 주유소의 최대힙을 구현하기위해 음수 -1 을 곱해 저장
        hq.heappush(q,-1 * station[i][1])
        #연료를 거리만큼 빼준다
        fuel -= distance
    else:
        print(cnt)