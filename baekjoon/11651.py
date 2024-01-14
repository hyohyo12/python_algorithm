#11651 / 좌표 정렬하기2
import sys
input = sys.stdin.readline
coordinate = []
for i in range(int(input())):
    coordinate.append(list(map(int,input().split())))
coordinate.sort(key=lambda x : x[0])
coordinate.sort(key=lambda x : x[1])
for i in coordinate:
    print("{0} {1}".format(i[0],i[1]))