import sys
input = sys.stdin.readline
n = int(input())
sCards = sorted(list(map(int,input().split())))
m = int(input())
cards = list(map(int,input().split()))
for i in cards:
    right = n-1
    left  = 0
    isExist = False
    while left <= right:
        mid = (left + right) // 2
        if sCards[mid] == i:
            isExist = True
            break
        elif sCards[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    print(1 if isExist else 0, end = ' ')