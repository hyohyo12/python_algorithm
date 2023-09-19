import sys
input = sys.stdin.readline
n = int(input())
nList = list(map(int,input().split()))
m = int(input())
mList = list(map(int,input().split()))
nList.sort()
for i in mList:
    left = 0
    right = n-1
    isExist = False
    while left <= right:
        mid = (left+right) // 2
        if i == nList[mid]:
            print(1)
            isExist = True
            break
        elif i < nList[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if isExist == False:
        print(0)