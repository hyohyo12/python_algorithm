import sys
input = sys.stdin.readline
n, m = map(int,input().split())
if n != 0:
    weight = list(map(int,input().split()))
    box = 1
    rest = m
    for i in range(0,n):
        # 나머지가 m을 초과하는 경우 (박스를 초과하는 경우)
        if rest - weight[i] < 0:
            box+=1
            rest = m - weight[i]
        # 나머지가 0일 경우 (박스에 딱 맞을 경우)
        elif rest - weight[i] == 0:
            rest = 0
        #나머지가 m보다 작을 경우(박스가 남을 경우)
        else:
            rest = rest - weight[i]
    print(box)
else:
    print(0)