import sys
from collections import defaultdict
input = sys.stdin.readline
if __name__ == "__main__":
    #입력
    #숫자의 개수
    n = int(input())
    #최빈값을 찾기위한 defaultdict
    counter = defaultdict(int)
    #최빈값이 빈도 수
    max_count = 0
    #숫자들을 저장할 리스트
    seq = []
    #숫자의 합을 저장할 변수
    all_sum = 0
    #n개의 숫자 입력 받으므로 n번 반복
    for _ in range(n):
        #tmp -> 숫자 입력
        tmp = int(input())
        #해당 숫자 빈도 수 갱신
        counter[tmp] += 1
        #seq에 tmp 저장
        seq.append(tmp)
        #all_sum에 tmp 합
        all_sum += tmp
        #최빈값의 빈도 수 갱식
        max_count = max(max_count,counter[tmp])
    #평균 출력(반올림)
    print(round(all_sum/n))
    #중앙값 찾기 위해 정렬
    seq.sort()
    #중앙값 출력
    print(seq[n//2])
    #최고 빈도 수를 가지는 key값을 저장할 리스트
    k_seq = []
    #빈도수 딕셔너리 탐색
    for k,v in counter.items():
        #최고 빈도 수를 가지는 value값 k_seq리스트에 저장
        if v == max_count:
            k_seq.append(k)
    #최빈수가 여러개면 2번째로 작은 수 출력해야 하므로 정렬
    k_seq.sort()
    #최빈 수가 하나라면 그냥 0번째(최빈수) 출력 여러개면 1번인덱스 값(2번째로 작은 값) 출력
    print(k_seq[0] if len(k_seq) == 1 else k_seq[1])
    #젤 큰값과 젤 작은 값 차(범위) 출력
    print(abs(seq[0]-seq[-1]))