import sys
input = sys.stdin.readline

#정답 함수
def sol(seq:list[int],n:int,m:int)->int:
    #처음 1부터 매우 큰 수까지 찾기
    left,right = 1,int(1e9)
    #정답을 저장할 변수
    answer = 0
    #이분(이진)탐색 시작
    while left <= right:
        #중간값
        mid = (left+right)//2
        #과자의 길이를 나눈 값을 저장할 c
        c = 0
        for num in seq:
            #현재 탐색 값으로 각 과자를 나눈 값 저장
            c += (num//mid)
        #해당 값이 m보다 크거나 같다면(m명의 조카에게 배분가능)
        if c >= m:
            #정답을 최대 값으로 갱신
            answer = max(answer,mid)
            #왼쪽 값을 mid+1값으로
            left = mid+1
        else:
            #그외(배분이 불가능)상황에선 나누는 작아 작아져야하므로
            right = mid-1
    return answer


if __name__ == "__main__":
    #입력
    #m->조카 수, n-> 과자 수
    m,n = map(int,input().split())
    #seq->각 과자 길이 저장
    seq = list(map(int,input().split()))
    print(sol(seq,n,m))