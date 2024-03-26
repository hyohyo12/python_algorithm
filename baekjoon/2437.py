import sys
input = sys.stdin.readline




if __name__ == "__main__":
    #입력
    #n(추의 개수)
    n = int(input())
    #추의 무게들을 저장하는 리스트
    seq = list(map(int,input().split()))
    #추들을 오름차순으로 정렬(작은 값부터 큰값으로 검색을 위해)
    seq.sort()
    #커버 불가능한 무게
    target = 1
    #무게 추 탐색
    for idx,num in enumerate(seq):
        #현재 무게 추가 커버 불가능한 곳보다 크면
        if num > target:
            #커버 가능하지 못한 곳이 생기므로 그 값이 답
            break
        #커버 불가능 한 곳 갱신
        target += num
    print(target)
