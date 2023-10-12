import sys
input = sys.stdin.readline
def binarySearch(start,end,findedList,findNumber): #이분 탐색 함수
    while start <= end:#이분탐색 시작(시작이 0 끝이 리스트의 끝 인덱스 즉 시작이 인덱스랑 같거나 커지면 끝)
        mid = (start+end) // 2 # 리스트의 중간값 찾기
        if findedList[mid] == findNumber: # 탐색 성공!
            return 1 # 1 반환
        elif findedList[mid] > findNumber: # 찾고자 하는 요소가 탐색될 리스트의 현재 요소보다 작다면
            end = mid - 1 #끝 부분 조정
        else:# 크다면
            start = mid + 1 #시작부분 조정
    return 0 #탐색 실패.. 0 반환

for _ in range(int(input())): #T 만큼 반복
    lenNo1 = int(input()) #첫 번째 수첩의 크기
    no1 = sorted(list(map(int,input().split()))) #첫 번째 수첩의 요소들 리스트에 저장
    lenNo2 = int(input()) #두 번째 수첩의 크기
    no2 = list(map(int,input().split())) #두 번째 수첩의 요소들 리스트에 저장
    for num in no2: #비교 시작
        print(binarySearch(0,lenNo1-1,no1,num)) #이분 탐색 함수-> 매개변수(시작,끝,탐색 될 리스트, 찾고자하는 요소)