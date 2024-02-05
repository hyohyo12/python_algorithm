import sys
inf = sys.maxsize
if __name__ == "__main__":
    input = sys.stdin.readline
    
    n,s = map(int,input().split())
    seq = list(map(int,input().split()))

    tmp = 0
    left,right = 0,0
    
    ans = inf
    
    while True:
        if tmp >= s:
            ans = min(ans,right-left)
            tmp -= seq[left]
            left += 1
        elif right == n:
            break
        else:
            tmp += seq[right]
            right += 1
    print(0 if ans == inf else ans)