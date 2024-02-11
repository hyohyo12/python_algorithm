import sys
input = sys.stdin.readline
#deque의 rotate보다 단순한 rotate 무조건 1번 돌아가는 로테이트
def my_rotate(seq:list[int]):
    seq = [seq[-1]] + seq[:-1]
    return seq
# if __name__ == "__main__":
#     n,k = map(int,input().split())
#     seq = [0]+list(map(int,input().split()))
    
#     count = 0
#     tmp = 0
    # occupy = [None]+[None for _ in range(2*n)]
    # while count != k:
    #     i = (2*n)
    #     while i >= 0:
    #         if occupy[i] != None:
    #             idx = (i+1)%(2*n)
    #             if seq[idx] != 0:
    #                 occupy[i] -= 1
    #                 if occupy[i] == 0:
    #                     occupy[i] = None
    #                     continue
    #                 occupy[idx] = occupy[i]
    #                 occupy[i] = None
    #                 seq[idx] -= 1
    #                 i -= 2
    #                 if seq[idx] == 0:
    #                     count -= 1
    #         else: i -= 1
        
    #     if seq[start] != 0:
    #         if occupy[start] == None:
    #             tmp += 1
    #             occupy[start] = n
    #             seq[start] -= 1
    #             if seq[start] == 0:
    #                 count += 1
    #     start -= 1
    #     if start <= 0:
    #         start = n*2
if __name__ == "__main__":
    n,k = map(int,input().split())
    seq = list(map(int,input().split()))
    occupy = [False for _ in range(n)]#현재 점유하고 있는가 나타내는 리스트
    count = 0#몇 번째 인지 나타내는 변수
    
    while True:
        count += 1
        occupy = my_rotate(occupy)#점유 리스트를 한 번 돌린다
        seq = my_rotate(seq) #내구성 리스트를 한 번 돌린다
        
        occupy[n-1] = False #n-1(n번째 요소) 는 내린다
        
        for i in range(n-2,-1,-1):#리스트에 있는 물건들의 위치 오른쪽으로
            if occupy[i]:#만약 점유하고 있다면
                if not occupy[i+1] and seq[i+1] != 0:#i+1번째 물건이 점유하지 않고, 내구성이 0이 아니면
                    #위치 스와핑
                    occupy[i+1] = True
                    occupy[i] = False
                    seq[i+1] -= 1
        #모두 작업이 끝난 후 n번째 있는 요소는 내린다.
        occupy[n-1] = False
        #시작 지점에 물건 놓기
        if seq[0] > 0 and not occupy[0]:#시작지점에 물건이 없고, 내구성이 0이 아니라면
            seq[0] -= 1#내구성 감소시키고
            occupy[0] = True#점유 리스트 해당값 True
        if seq.count(0) >= k:#만약 내구성이 0인 요소가 k개 이상이면
            break#그만둔다
    print(count)#몇번째인지 출력