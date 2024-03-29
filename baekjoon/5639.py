import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def post_order(arr):
    if len(arr) == 0:
        return
    
    left,right = [],[]
    mid = arr[0]
    for i in range(1,len(arr)):
        if mid < arr[i]:
            right = arr[i:]
            left = arr[1:i]
            break
    else:
        left = arr[1:]
    post_order(left)
    post_order(right)
    print(mid)
    

if __name__ == "__main__":
    arr = []
    while True:
        try:
            arr.append(int(input()))
        except:
            break
    
    post_order(arr)