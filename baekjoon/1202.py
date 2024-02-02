import sys
import heapq
input = sys.stdin.readline


if __name__ == "__main__":
    n,k = map(int,input().split())
    
    dia_seq = [tuple(map(int,input().split())) for _ in range(n)]
    bag_seq = [int(input()) for _ in range(k)]
    dia_seq.sort();bag_seq.sort() #다이아의 무게와 가방의 용량 오름차순 정렬
    
    tmp = [] #다이아의 가치를 저장할 우선순위 큐
    ans = 0
    for w in bag_seq: #가방을 탐색하며
        while dia_seq and dia_seq[0][0] <= w: #다이아가 남아있고, 다이아의 무게가 현재 가방의 용량보다 작을 때까지 탐색
            heapq.heappush(tmp,-dia_seq[0][1]) #tmp에 최대 힙을 구성하기위해 음수로 변환된 다이아의 가치를 저장한다.
            heapq.heappop(dia_seq) #다이아 리스트에 해당하는 값을 삭제한다.
        if tmp : ans -= heapq.heappop(tmp) #tmp에 값이 있다면 제일 가치가 높은 값을 ans(정답변수에 저장)
    print(ans)
    #가방과 다이아몬드의 무게 모두 오름차순으로 정렬하였다. while문의 조건때문에 tmp에는 w보다 큰 무게의 다이아는 들어가지 않는다. 이 떄문에 다음 가방에서 tmp에서 무게를 무시하고 제일 큰 값을 
    #heappop하여 쓰면 된다는 뜻이다.