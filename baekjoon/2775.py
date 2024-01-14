import sys
input = sys.stdin.readline
tc = int(input())
for i in range(tc):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    else:
        temp = [i for i in range(1,n+1)]
        for j in range(k):
            floor = []
            for y in range(n):
                floor.append(sum(temp[:y+1]))
            temp = floor.copy()
        print(floor[-1])
            