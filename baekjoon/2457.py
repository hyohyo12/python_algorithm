# import sys
# input = sys.stdin.readline


# if __name__ == "__main__":
#     n = int(input())
    
#     flowers = []
#     for _ in range(n):
#         start_month,start_date,end_month,end_date = map(int,input().split()) 
#         flowers.append((start_month*100+start_date,end_month*100+end_date))# 계산 편하기위해 달* 100 + 일 하여 튜플로 저장
#     flowers.sort() #시작하는 날 기준 정렬
    
#     end_date = 301 #3월 1일부터 피면 되므로 301(3월 1일) 저장 밑에 while문에서 처음 꽃이 피는 날이 3월 1일 이하면 되므로 301 설정.
#     count = 0 #정답을 저장할 변수
    
#     while flowers: #을 저장한 리스트를 탐색
#         if end_date >= 1201 or end_date < flowers[0][0]: #끝나는 날이 이제 11월 30일까지는 꽃이 펴야하므로 끝나는 지점이 1201(12월 1일) 이거나 전의 꽃이 지는날이 현재 꽃의 피는 날 보다 작으면
#             break #멈추기
#         tmp_end_date = -1 #임시로 지는날을 저장할 변수
#         for i in range(len(flowers)): #꽃들을 탐색
#             if end_date >= flowers[0][0]: #전 꽃이 지는 날이 현재 꽃이 피는날보다 크다면
#                 tmp_end_date = max(tmp_end_date,flowers[0][1]) #임시로 지는날을 저장할 변수에 있는 값과 비교하며 갱신
#                 flowers.remove(flowers[0]) #해당 꽃은 지움.
#             else: #정렬 했으므로 지는 날이 현재 꽃이 피는날보다 작다면 후에 나올 꽃보다도 모두 작다는 뜻이므로 탐색 중단
#                 break
#         end_date = tmp_end_date #꽃이 지는 날 갱신
#         count += 1 #정답 갱신
#     print(0 if end_date < 1201 else count) #마지막 탐색한 꽃의 지는날이 1201 보다 작다면 0을 print 크거나 같다면 count(정답 변수)를 print

from collections import deque
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    
    flowers = []
    for _ in range(n):
        start_month,start_date,end_month,end_date = map(int,input().split())
        flowers.append((start_month*100+start_date,end_month*100+end_date))
    flowers.sort()
    #동일
    
    flowers = deque(flowers) #flowers 를 큐로 변환한다.
    end_date = 301 
    flowers = deque(flowers)
    end_date = 301
    count = 0
    while flowers:
        if end_date >= 1201 or end_date < flowers[0][0]:
            break
        tmp_end_date = -1
        for i in range(len(flowers)):
            if end_date >= flowers[0][0]:
                tmp_end_date = max(tmp_end_date,flowers[0][1])
                flowers.popleft() #remove함수보다 popleft를 써 O(1)의 시간으로 단축하였다
            else:
                break
        end_date = tmp_end_date
        count += 1
    print(0 if end_date < 1201 else count)