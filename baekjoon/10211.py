import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    matrix = list(map(int,input().split()))
    sumList = [matrix[0]]
    for j in range(1,n):
        big = max(sumList[j-1]+matrix[j],matrix[j])
        sumList.append(big)
    print(max(sumList))