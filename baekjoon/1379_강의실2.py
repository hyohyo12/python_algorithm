import sys,heapq
input = sys.stdin.readline

#메인 함수
def main():
    #입력
    #필요한 방의 개수
    room = 1
    #n개의 강의 n -> 입력
    n = int(input())
    #각 강의 번호가 배정받을 강의실 번호 저장할 리스트
    loc_room = [0 for _ in range(n+1)]
    #n개의 강의들의 정보를 입력 받음
    lectures = [list(map(int,input().split())) for _ in range(n)]
    #강의를 1번째(시작 시간),2번째(끝나는 시간)을 기준으로 정렬
    lectures.sort(key= lambda x:(x[1],x[2]))
    
    #우선순위 큐
    q = []
    #큐에 가장 빨리 시작하는 강의의 끝나는 시간과 방번호를 함께 저장
    heapq.heappush(q,(lectures[0][2],room))
    #해당 강의의 방번호 배정
    loc_room[lectures[0][0]] = room
    
    #첫번째 강의부터 끝까지
    for i in range(1,n):
        #큐에서 가장 빨리 끝나는 강의가 현재 i번째 강의 시작시간보다 크다면 -> 현재 진행중인강의 중 끝나는 시간이 모두 현재 강의 시작 시간 이후
        if q[0][0] > lectures[i][1]:
            #방 한 개 더 배정
            room += 1
            #해당 강의에 최신화된 방 배정
            loc_room[lectures[i][0]] = room
            #큐에 (끝나는 시간,방번호) 저장
            heapq.heappush(q,(lectures[i][2],room))
        #i번째 강의의 시작 시간이 큐에 있는 시간이 더 크다면 -> i번째 강의의 시작 시간이 큐에 있는 끝나는 시간이 가장 빠른 강의의 끝나는 시간보다 느리거나 같음.
        else:
            #tmp에 큐에서 heapop결과 저장
            tmp = heapq.heappop(q)
            #i번째강의의 방 배정
            loc_room[lectures[i][0]] = tmp[1]
            #큐에 i번째 강의의 끝나는 시각과 방번호 저장
            heapq.heappush(q,(lectures[i][2],tmp[1]))
    #필요한 방의 개수 출력
    print(room)
    #배정된 방번호 각각 출력
    for j in loc_room[1:]:
        print(j)

if __name__ == "__main__":#
    main()