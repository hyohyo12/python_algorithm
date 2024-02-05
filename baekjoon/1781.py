import heapq
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    
    seq = [tuple(map(int,input().split())) for _ in range(n)]
    #(마감일, 컵라면 수) 튜플로 입력
    seq.sort()#마감일로 정렬
    
    q = [] #우선순위 큐
    
    for deadline,score in seq: #리스트 탐색
        heapq.heappush(q,score) #우선순위 큐에 score(컵라면 수)를 저장한다.
        if len(q) > deadline: #현재 마감일이 큐의 길이(누적된 업무 일)보다 크다면
            heapq.heappop(q) #우선순위 큐에서 제일 작은 값 pop
    print(sum(q)) #q를 모두 합한 값을 출력
