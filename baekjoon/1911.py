import math
def min_board(n:int,l:int,seq)->int:
    seq.sort()#정렬
    count = 0 #개수 저장할 변수
    cover = 0 #어디까지 커버가 가능한지 저장한 변수
    for start,end in seq: #웅덩이 루프
        start = max(start,cover) #거버가능한 곳 안에 start가 있는지
        tmp = math.ceil((end-start)/l) #현재 값에 대해 커버를 해야하므로 올림을 해서 널빤지를 씀
        cover = start+(tmp*l) #하지만 그래도 다음값을 커버 할 수 있는지를 담기위해 계산을 한 번 더 해
        count += tmp #개수 합하자
    return count
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    n,l = map(int,input().split())
    seq = []
    for i in range(n):
        seq.append(list(map(int,input().split())))
    print(min_board(n,l,seq))