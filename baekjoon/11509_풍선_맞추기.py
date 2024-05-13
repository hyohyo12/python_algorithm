import sys
input = sys.stdin.readline

#메인 함수
def main():
    #n -> 풍선의 개수 입력
    n = int(input())
    #풍선의 높이를 저장하는 seq리스트 입력
    seq = list(map(int,input().split()))
    #풍선이 가질 수 있는 높이 만큼 리스트를 생성하고
    #각 높이의 풍선이 존재하는지를 저장할 리스트
    visited = [[] for _ in range(1000001)]
    #res -> 정답 최소한의 화살의 개수를 저장할 변수
    res = 1
    #0번째 풍선에 해당하는 높이의 칸에 1(그냥 표시) 추가
    visited[seq[0]].append(1)
    #1번째 부터 n번째 풍선까지 반복
    for i in range(1,n):
        #현재 풍선에서 높이가 1 높은 풍선을 방문한 이력이있다면
        if len(visited[seq[i]+1]):
            #해당 화살 재활용
            visited[seq[i]+1].pop()
            #현재 풍선의 높이에 방문 추가
            visited[seq[i]].append(1)
        #방문한 이력이 없다는 것은 전 풍선 중 현재 풍선 높이보다 1만큼 높은 풍선이 없다는 뜻
        else:
            #새로 화살을 쏴야함.
            res += 1
            #현재 새로운 화살의 높이 저장
            visited[seq[i]].append(1)
    #결과 값 출력
    print(res)

if __name__ == "__main__":
    main()