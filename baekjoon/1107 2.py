import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    if m != 0:
        break_seq = list(map(int,input().split()))
        res = abs(n-100)
        is_broken = [False for _ in range(10)]
        for i in break_seq:
            is_broken[i] = True
        for i in range(1000001):
            for num in str(i):
                if is_broken[int(num)]:  
                    break
            else:
                res = min(res,abs(n-i)+len(str(i)))
        print(res)
    else:
        print(len(str(n)))