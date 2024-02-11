import sys
input = sys.stdin.readline

def sol(seq:list[int],n:int,m:int)->int:
    left,right = 1,int(1e9)
    answer = 0
    while left <= right:
        mid = (left+right)//2
        c = 0
        for num in seq:
            c += (num//mid)
        if c >= m:
            answer = max(answer,mid)
            left = mid+1
        else:
            right = mid-1
    return answer


if __name__ == "__main__":
    m,n = map(int,input().split())
    seq = list(map(int,input().split()))
    print(sol(seq,n,m))