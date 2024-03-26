import sys
input = sys.stdin.readline

def find_two_num(seq:list[int],n:int):
    seq.sort()
    left,right = 0,n-1
    
    res = abs(seq[left]+seq[right])
    tmp = (seq[left],seq[right])
    
    while left < right:
        left_val,right_val = seq[left], seq[right]
        
        cur = left_val + right_val
        if abs(cur) < res:
            res = abs(cur)
            tmp = (left_val,right_val)
            if cur == 0:
                break
        if cur < 0:
            left += 1
        else:
            right -= 1
    print(tmp[0],tmp[1])


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int,input().split()))
    find_two_num(seq,n)